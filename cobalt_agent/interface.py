"""
Cobalt Agent - Interactive CLI Interface
Refactored to enforce System Prompt Rules (rules.yaml) during tool analysis.
"""

from rich.console import Console
from rich.table import Table
from rich.prompt import Prompt
from loguru import logger
from rich.markdown import Markdown

# Type hinting
from typing import Optional, TYPE_CHECKING, Any, List
if TYPE_CHECKING:
    from cobalt_agent.brain.cortex import Cortex

from cobalt_agent.tool_manager import ToolManager

class CLI:
    """Interactive command-line interface for Cobalt Agent."""
    
    def __init__(self, memory_system, llm, system_prompt, tool_manager, cortex=None):
        self.console = Console()
        self.tool_manager = tool_manager
        self.memory = memory_system
        self.llm = llm
        self.system_prompt = system_prompt
        self.cortex = cortex 

        logger.info("CLI initialized with Brain connected")
    
    def start(self):
        """Start the interactive CLI loop."""
        self.console.print("\n[bold green]🤖 Cobalt Agent Interface[/bold green]")
        self.console.print(f"[dim]Model: {self.llm.model_name}[/dim]")
        self.console.print("[dim]Type 'exit' or 'quit' to leave[/dim]\n")
        
        while True:
            try:
                user_input = Prompt.ask("[bold cyan]Cobalt >[/]")
                user_input = user_input.strip()
                
                if not user_input: continue

                if user_input.lower() in ['exit', 'quit']:
                    self.console.print("[yellow]Shutting down Cobalt Agent...[/yellow]")
                    break
                
                self.memory.add_log(user_input, source="User")

                # 1. CORTEX CHECK
                handled_by_cortex = False
                if self.cortex:
                    specialist_response = self.cortex.route(user_input)
                    if specialist_response:
                        self.console.print(f"\n[bold purple]🤖 Cortex:[/bold purple] {specialist_response}")
                        self.memory.add_log(specialist_response, source="System")
                        handled_by_cortex = True
                
                if handled_by_cortex: continue 
                
                # 2. MANUAL COMMANDS
                if user_input.lower().startswith('search '):
                    self._handle_search(user_input[7:])
                elif user_input.lower().startswith('visit '):
                    self._handle_visit(user_input[6:])
                elif user_input.lower().startswith('ticker '):
                    self._handle_finance(user_input[7:])
                
                # 3. AUTONOMOUS CHAT
                else:
                    self._handle_chat(user_input)
                    
            except KeyboardInterrupt:
                self.console.print("\n[yellow]Interrupted. Shutting down...[/yellow]")
                break
            except Exception as e:
                logger.error(f"CLI error: {str(e)}", exc_info=True)
                self.console.print(f"[red]Error: {str(e)}[/red]")
    
    def _format_tool_output(self, output: Any) -> str:
        """Helper to convert Pydantic models/Lists to clean strings."""
        if isinstance(output, list):
            return "\n".join([str(item) for item in output])
        return str(output)

    def _handle_chat(self, user_input: str):
        """Autonomous Agent Loop (ReAct Pattern)."""
        self.console.print(f"[dim]Thinking...[/dim]")
        
        turn_history = [] 
        current_input = user_input
        MAX_TURNS = 5
        
        for turn in range(MAX_TURNS):
            # 1. Get Context
            context = self.memory.get_context()
            full_context = context + turn_history if turn > 0 else context
            
            # 2. Ask Brain
            response = self.llm.think(
                user_input=current_input,
                system_prompt=self.system_prompt,
                memory_context=full_context
            )
            
            # 3. Check for ACTION
            if "ACTION:" in response:
                try:
                    lines = response.split('\n')
                    action_line = next(line for line in lines if "ACTION:" in line)
                    parts = action_line.replace("ACTION:", "").strip().split(" ", 1)
                    
                    tool_name = parts[0]
                    query = parts[1] if len(parts) > 1 else ""
                    
                    self.console.print(f"[bold yellow]⚡ Auto-Tool:[/bold yellow] {tool_name} -> {query}")
                    self.memory.add_log(f"Agent Thought: {response}", source="Assistant")
                    
                    # Execute
                    result = self.tool_manager.execute_tool(tool_name.lower(), {"query": query})
                    
                    if result.success:
                        output_str = self._format_tool_output(result.output)
                        preview = output_str[:500] + "..." if len(output_str) > 500 else output_str
                        self.console.print(f"[dim cyan]{preview}[/dim cyan]") 
                        
                        observation = f"System Observation from {tool_name}: {output_str}"
                    else:
                        observation = f"System Observation: Error - {result.error}"
                        self.console.print(f"[red]{observation}[/red]")
                    
                    turn_history.append({"role": "assistant", "content": response})
                    turn_history.append({"role": "user", "content": observation})
                    
                    # <--- KEY FIX: STRICT INSTRUCTION --->
                    current_input = (
                        "(Observation provided above. Analyze this data STRICTLY according to the "
                        "protocols and formatting rules defined in your System Prompt. "
                        "Do not deviate from the agreed structure.)"
                    )
                    
                except Exception as e:
                    self.console.print(f"[red]Auto-Loop Error: {e}[/red]")
                    break
            else:
                self.memory.add_log(response, source="Assistant")
                self.console.print(f"\n[bold green]Cobalt:[/bold green]")
                self.console.print(Markdown(response))
                self.console.print()
                break
        
    def _handle_search(self, query: str):
        """Handle search command."""
        if not query: return
        self.console.print(f"\n[bold]Searching for:[/bold] {query}")
        self.memory.add_log(f"Executing SearchTool: {query}", source="System")

        tool_result = self.tool_manager.execute_tool("search", {"query": query})
        
        if not tool_result.success:
            self.console.print(f"[red]Tool Execution Failed: {tool_result.error}[/red]")
            return
            
        results = tool_result.output 
        if not results:
            self.console.print("[yellow]No results found[/yellow]\n")
            return
        
        self.memory.add_log(f"Search returned {len(results)} results", source="System", data={"tool": "search", "query": query})

        # Table Display
        table = Table(title=f"Search Results ({len(results)} found)", show_header=True, header_style="bold magenta")
        table.add_column("#", style="dim", width=3)
        table.add_column("Title", style="cyan", width=40)
        table.add_column("URL", style="blue", width=50)
        table.add_column("Snippet", style="green", width=60)
        
        search_context_list = []
        for i, item in enumerate(results, 1):
            title = getattr(item, 'title', 'N/A')
            url = getattr(item, 'href', 'N/A')
            snippet = getattr(item, 'body', 'N/A')
            
            search_context_list.append(f"- {title}: {snippet}")
            
            if len(snippet) > 150: snippet = snippet[:147] + "..."
            if len(url) > 60: url = url[:57] + "..."
            if len(title) > 50: title = title[:47] + "..."
            table.add_row(str(i), title, url, snippet)
        
        self.console.print(table)
        self.console.print()

        self.console.print("[dim]Analyzing search results...[/dim]")
        summary = self.llm.think(
            user_input=f"Summarize these search results for '{query}' using the format defined in your System Rules.",
            system_prompt=self.system_prompt,
            search_context="\n".join(search_context_list)
        )
        
        self.console.print(f"\n[bold green]Cobalt Analysis:[/bold green]")
        self.console.print(Markdown(summary))
        self.console.print()
        self.memory.add_log(summary, source="Assistant")

    def _handle_visit(self, url: str):
        """Handle manual browser request."""
        self.console.print(f"\n[bold]Visiting:[/bold] {url}")
        self.memory.add_log(f"Executing BrowserTool: {url}", source="System")

        result = self.tool_manager.execute_tool("browser", {"url": url})
        if not result.success:
             self.console.print(f"[red]Error: {result.error}[/red]")
             return
             
        page_data = result.output
        content = page_data.content
        
        self.console.print(f"\n[green]--- Page Content ({len(content)} chars) ---[/green]")
        self.console.print(content[:1000] + "...\n[dim](content truncated)[/dim]")
        
        self.console.print("\n[dim]Reading page...[/dim]")
        summary = self.llm.think(
            user_input=f"Analyze this content from {url}. Extract key insights according to System Protocols.",
            system_prompt=self.system_prompt,
            search_context=content
        )
        self.console.print(f"\n[bold green]Cobalt Analysis:[/bold green]")
        self.console.print(Markdown(summary))
        self.console.print()
        self.memory.add_log(summary, source="Assistant")

    def _handle_finance(self, ticker: str):
        """Handle manual finance tool request."""
        self.console.print(f"\n[bold]Checking Market Data:[/bold] {ticker}")
        self.memory.add_log(f"Executing FinanceTool: {ticker}", source="System")

        result = self.tool_manager.execute_tool("finance", {"ticker": ticker})
        if not result.success:
             self.console.print(f"[red]Error: {result.error}[/red]")
             return
             
        metrics = result.output
        data_str = str(metrics)
        
        self.console.print(f"\n[green]--- Market Report ---[/green]")
        self.console.print(Markdown(data_str))
        self.console.print()
        
        self.console.print("[dim]Analyzing market data...[/dim]")
        
        # <--- KEY FIX: REMOVED "Bullish/Bearish" RESTRICTION --->
        analysis = self.llm.think(
            user_input=(
                f"Analyze this stock data for {ticker}. "
                f"Apply the TRADING RULES from your System Prompt. "
                f"Provide actionable levels (Entry, Stop, Target) if the setup matches your criteria."
            ),
            system_prompt=self.system_prompt,
            search_context=data_str
        )
        
        self.console.print(f"\n[bold green]Cobalt Analysis:[/bold green]")
        self.console.print(Markdown(analysis))
        self.console.print()
        self.memory.add_log(analysis, source="Assistant")