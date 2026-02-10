"""
Cobalt Agent - Interactive CLI Interface
Provides a rich terminal interface for interacting with the agent.
"""

from rich.console import Console
from rich.table import Table
from rich.prompt import Prompt
from loguru import logger
from rich.markdown import Markdown

# Type hinting to avoid circular imports
from typing import Optional, TYPE_CHECKING
if TYPE_CHECKING:
    from cobalt_agent.brain.cortex import Cortex

from cobalt_agent.tools.search import SearchTool
from cobalt_agent.tool_manager import ToolManager

class CLI:
    """Interactive command-line interface for Cobalt Agent."""
    
    # <--- UPDATE: Added 'cortex' parameter
    def __init__(self, memory_system, llm, system_prompt, tool_manager, cortex=None):
        """Initialize the CLI with console and tools."""
        self.console = Console()
        self.tool_manager = tool_manager
        self.memory = memory_system
        self.llm = llm
        self.system_prompt = system_prompt
        self.cortex = cortex  # <--- STORE CORTEX

        logger.info("CLI initialized with Brain connected")
    
    def start(self):
        """Start the interactive CLI loop."""
        self.console.print("\n[bold green]🤖 Cobalt Agent Interface[/bold green]")
        self.console.print(f"[dim]Model: {self.llm.model_name}[/dim]")
        self.console.print("[dim]Type 'exit' or 'quit' to leave[/dim]\n")
        
        while True:
            try:
                # Get user input
                user_input = Prompt.ask("[bold cyan]Cobalt >[/]")
                user_input = user_input.strip()
                
                if not user_input:
                    continue

                # Check for exit commands
                if user_input.lower() in ['exit', 'quit']:
                    self.console.print("[yellow]Shutting down Cobalt Agent...[/yellow]")
                    break
                
                # Log user input to memory
                self.memory.add_log(user_input, source="User")

                # ---------------------------------------------------------
                # 1. CORTEX CHECK (The New Logic)
                # Check if this is a Scribe command (Save/Log) BEFORE checking tools
                # ---------------------------------------------------------
                handled_by_cortex = False
                if self.cortex:
                    specialist_response = self.cortex.route(user_input)
                    if specialist_response:
                        # Cortex handled it (e.g. Saved a note)
                        self.console.print(f"\n[bold purple]🤖 Cortex:[/bold purple] {specialist_response}")
                        self.memory.add_log(specialist_response, source="System")
                        handled_by_cortex = True
                
                if handled_by_cortex:
                    continue  # Skip the rest of the loop
                
                # ---------------------------------------------------------
                # 2. MANUAL COMMANDS (Your Custom Triggers)
                # ---------------------------------------------------------
                if user_input.lower().startswith('search '):
                    query = user_input[7:]
                    self._handle_search(query)
                
                elif user_input.lower().startswith('visit '):
                    url = user_input[6:]
                    self._handle_visit(url)
                
                elif user_input.lower().startswith('ticker '):
                    symbol = user_input[7:]
                    self._handle_finance(symbol)
                
                # ---------------------------------------------------------
                # 3. AUTONOMOUS CHAT (Your ReAct Loop)
                # ---------------------------------------------------------
                else:
                    self._handle_chat(user_input)
                    
            except KeyboardInterrupt:
                self.console.print("\n[yellow]Interrupted. Shutting down...[/yellow]")
                break
            except Exception as e:
                logger.error(f"CLI error: {str(e)}", exc_info=True)
                self.console.print(f"[red]Error: {str(e)}[/red]")
    
    def _handle_chat(self, user_input: str):
        """
        Autonomous Agent Loop (ReAct Pattern).
        """
        self.console.print(f"[dim]Thinking...[/dim]")
        
        turn_history = [] 
        current_input = user_input
        
        MAX_TURNS = 5
        
        for turn in range(MAX_TURNS):
            # 1. Get Context
            context = self.memory.get_context()
            
            # 2. Ask Brain (History + Current Input)
            full_context = context + turn_history if turn > 0 else context
            
            response = self.llm.think(
                user_input=current_input,
                system_prompt=self.system_prompt,
                memory_context=full_context
            )
            
            # 3. Check for ACTION
            if "ACTION:" in response:
                try:
                    # Parse the action
                    lines = response.split('\n')
                    action_line = next(line for line in lines if "ACTION:" in line)
                    parts = action_line.replace("ACTION:", "").strip().split(" ", 1)
                    
                    if len(parts) < 2:
                        tool_name = parts[0]
                        query = ""
                    else:
                        tool_name, query = parts
                    
                    self.console.print(f"[bold yellow]⚡ Auto-Tool:[/bold yellow] {tool_name} -> {query}")
                    self.memory.add_log(f"Agent Thought: {response}", source="Assistant")
                    
                    # Execute Tool
                    result = self.tool_manager.execute_tool(tool_name.lower(), {"query": query})
                    
                    # Format Observation
                    if result.success:
                        # Truncate for console, keep full for LLM
                        observation_preview = str(result.output)[:500] + "..." if len(str(result.output)) > 500 else str(result.output)
                        self.console.print(f"[dim cyan]{observation_preview}[/dim cyan]") 
                        
                        # Full observation for the LLM
                        observation = f"System Observation from {tool_name}: {str(result.output)}"
                    else:
                        observation = f"System Observation: Error - {result.error}"
                        self.console.print(f"[red]{observation}[/red]")
                    
                    # Log history
                    turn_history.append({"role": "assistant", "content": response})
                    turn_history.append({"role": "user", "content": observation})
                    
                    # Update input to prompt the next step
                    current_input = "(Observation provided above. Analyze it and continue.)"
                    
                except Exception as e:
                    self.console.print(f"[red]Auto-Loop Error: {e}[/red]")
                    break
            else:
                # Final Answer
                self.memory.add_log(response, source="Assistant")
                self.console.print(f"\n[bold green]Cobalt:[/bold green]")
                self.console.print(Markdown(response))
                self.console.print()
                break
        
    def _handle_search(self, query: str):
        """Handle search command, display results table, AND summarize."""
        if not query:
            self.console.print("[red]Please provide a search query[/red]")
            return
        
        self.console.print(f"\n[bold]Searching for:[/bold] {query}")
        logger.info(f"User search query: {query}")
        self.memory.add_log(f"Executing SearchTool: {query}", source="System")

        tool_result = self.tool_manager.execute_tool("search", {"query": query})
        
        if not tool_result.success:
            self.console.print(f"[red]Tool Execution Failed: {tool_result.error}[/red]")
            return
            
        results = tool_result.output
        if not results:
            self.console.print("[yellow]No results found[/yellow]\n")
            return
        
        # Log full results to memory
        self.memory.add_log(f"Search returned {len(results)} results", source="System", data={"tool": "search", "query": query})

        # Create Table
        table = Table(title=f"Search Results ({len(results)} found)", show_header=True, header_style="bold magenta")
        table.add_column("#", style="dim", width=3)
        table.add_column("Title", style="cyan", width=40)
        table.add_column("URL", style="blue", width=50)
        table.add_column("Snippet", style="green", width=60)
        
        for i, result in enumerate(results, 1):
            title = result.get('title', 'N/A')
            url = result.get('href', 'N/A')
            snippet = result.get('body', 'N/A')
            
            if len(snippet) > 150: snippet = snippet[:147] + "..."
            if len(url) > 60: url = url[:57] + "..."
            if len(title) > 50: title = title[:47] + "..."
            
            table.add_row(str(i), title, url, snippet)
        
        self.console.print(table)
        self.console.print()

        # Synthesis
        self.console.print("[dim]Analyzing search results...[/dim]")
        search_context_str = "\n".join([f"- {r['title']}: {r['body']}" for r in results])
        
        summary = self.llm.think(
            user_input=f"Summarize these search results for query: '{query}'. Provide key takeaways.",
            system_prompt=self.system_prompt,
            search_context=search_context_str
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
             
        content = result.output
        
        self.console.print(f"\n[green]--- Page Content ({len(content)} chars) ---[/green]")
        self.console.print(content[:1000] + "...\n[dim](content truncated)[/dim]")
        
        self.console.print("\n[dim]Reading page...[/dim]")
        summary = self.llm.think(
            user_input=f"Analyze this webpage content from {url}. What are the key points?",
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
             
        data = result.output
        
        self.console.print(f"\n[green]--- Market Report ---[/green]")
        self.console.print(Markdown(data))
        self.console.print()
        
        self.console.print("[dim]Analyzing market data...[/dim]")
        analysis = self.llm.think(
            user_input=f"Analyze this stock data for {ticker}. Is it bullish or bearish right now?",
            system_prompt=self.system_prompt,
            search_context=data
        )
        
        self.console.print(f"\n[bold green]Cobalt Analysis:[/bold green]")
        self.console.print(Markdown(analysis))
        self.console.print()
        self.memory.add_log(analysis, source="Assistant")