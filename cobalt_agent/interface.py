"""
Cobalt Agent - Interactive CLI Interface
Provides a rich terminal interface for interacting with the agent.
"""

from rich.console import Console
from rich.table import Table
from rich.prompt import Prompt
from loguru import logger
# <--- ADDED: Import Markdown for pretty printing AI responses
from rich.markdown import Markdown

from cobalt_agent.tools.search import SearchTool
from cobalt_agent.tool_manager import ToolManager

class CLI:
    """Interactive command-line interface for Cobalt Agent."""
    
    # Accept memory, llm,  system_prompt  and tool_manger arguments
    def __init__(self, memory_system, llm, system_prompt, tool_manager):

        """Initialize the CLI with console and tools."""
        self.console = Console()

        # Use the Manager instead of direct tool instantiation
        self.tool_manager = tool_manager
        
        # Store memory reference
        self.memory = memory_system

        # Store Brain and Persona
        self.llm = llm
        self.system_prompt = system_prompt

        logger.info("CLI initialized with Brain connected")
    
    def start(self):
        """Start the interactive CLI loop."""
        self.console.print("\n[bold green]🤖 Cobalt Agent Interface[/bold green]")
        self.console.print(f"[dim]Model: {self.llm.model_name}[/dim]") # <--- ADDED: Show active model
        self.console.print("[dim]Type 'exit' or 'quit' to leave[/dim]\n")
        
        while True:
            try:
                # Get user input with rich prompt
                user_input = Prompt.ask("[bold cyan]Cobalt >[/]")
                
                # Strip whitespace
                user_input = user_input.strip()
                
                # Check for exit commands
                if user_input.lower() in ['exit', 'quit']:
                    self.console.print("[yellow]Shutting down Cobalt Agent...[/yellow]")
                    break
                
                # Log user input to memory
                self.memory.add_log(user_input, source="User")

                # Check for search command
                if user_input.lower().startswith('search '):
                    query = user_input[7:]  # Remove 'search ' prefix
                    self._handle_search(query)
                # <--- ADDED: Handle 'visit' command
                elif user_input.lower().startswith('visit '):
                    url = user_input[6:]
                    self._handle_visit(url)
                # Catch-all for conversation
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
        Handle general conversation using the LLM.
        """
        # Real Thinking Logic
        self.console.print(f"[dim]Thinking...[/dim]")
        
        # 1. Retrieve Context (Short-term memory)
        context = self.memory.get_context()
        
        # 2. Ask the Brain
        response = self.llm.think(
            user_input=user_input,
            system_prompt=self.system_prompt,
            memory_context=context
        )
        
        # 3. Log the Response
        self.memory.add_log(response, source="Assistant")
        
        # 4. Display the Response (Pretty printed)
        self.console.print(f"\n[bold green]Cobalt:[/bold green]")
        self.console.print(Markdown(response))
        self.console.print()
        
    def _handle_search(self, query: str):
        """Handle search command, display results table, AND summarize."""
        if not query:
            self.console.print("[red]Please provide a search query[/red]")
            return
        
        self.console.print(f"\n[bold]Searching for:[/bold] {query}")
        logger.info(f"User search query: {query}")
        self.memory.add_log(f"Executing SearchTool: {query}", source="System")

        # Execute via Tool Manager
        # We pass the tool name "search" and the arguments dict
        tool_result = self.tool_manager.execute_tool("search", {"query": query})
        
        # Check for failure
        if not tool_result.success:
            self.console.print(f"[red]Tool Execution Failed: {tool_result.error}[/red]")
            self.memory.add_log(f"Search failed: {tool_result.error}", source="System")
            return
            
        results = tool_result.output
        
        if not results:
            self.console.print("[yellow]No results found[/yellow]\n")
            # Log empty result
            self.memory.add_log("Search returned 0 results", source="System")
            return
        
        # Log full results to memory
        self.memory.add_log(
            f"Search returned {len(results)} results", 
            source="System", 
            data={"tool": "search", "query": query, "results": results}
        )

        # Create and populate table
        table = Table(title=f"Search Results ({len(results)} found)", show_header=True, header_style="bold magenta")
        table.add_column("#", style="dim", width=3)
        table.add_column("Title", style="cyan", width=40)
        table.add_column("URL", style="blue", width=50)
        table.add_column("Snippet", style="green", width=60)
        
        for i, result in enumerate(results, 1):
            title = result.get('title', 'N/A')
            url = result.get('href', 'N/A')
            snippet = result.get('body', 'N/A')
            
            # Truncate long text
            if len(snippet) > 150:
                snippet = snippet[:147] + "..."
            if len(url) > 60:
                url = url[:57] + "..."
            if len(title) > 50:
                title = title[:47] + "..."
            
            table.add_row(str(i), title, url, snippet)
        
        # Display table
        self.console.print(table)
        self.console.print()

        # Ask the Brain to Summarize the Search Results --- AI SYNTHESIS ---    
        self.console.print("[dim]Analyzing search results...[/dim]")

        # Create a mini-prompt for synthesis
        search_context_str = "\n".join([f"- {r['title']}: {r['body']}" for r in results])
        
        summary = self.llm.think(
            user_input=f"Summarize these search results for query: '{query}'. Provide key takeaways.",
            system_prompt=self.system_prompt,
            search_context=search_context_str
        )
        
        # Display Summary
        self.console.print(f"\n[bold green]Cobalt Analysis:[/bold green]")
        self.console.print(Markdown(summary))
        self.console.print()
        
        # Log the summary
        self.memory.add_log(summary, source="Assistant")

    def _handle_visit(self, url: str):
        """Handle manual browser request."""
        self.console.print(f"\n[bold]Visiting:[/bold] {url}")
        self.memory.add_log(f"Executing BrowserTool: {url}", source="System")

        # Execute Browser Tool via Manager
        result = self.tool_manager.execute_tool("browser", {"url": url})
        
        if not result.success:
             self.console.print(f"[red]Error: {result.error}[/red]")
             return
             
        content = result.output
        
        # Display Preview (First 1000 chars)
        self.console.print(f"\n[green]--- Page Content ({len(content)} chars) ---[/green]")
        self.console.print(content[:1000] + "...\n[dim](content truncated)[/dim]")
        
        # Ask Brain to Summarize
        self.console.print("\n[dim]Reading page...[/dim]")
        
        summary = self.llm.think(
            user_input=f"Analyze this webpage content from {url}. What are the key points?",
            system_prompt=self.system_prompt,
            search_context=content  # We inject the full page text here
        )
        
        self.console.print(f"\n[bold green]Cobalt Analysis:[/bold green]")
        self.console.print(Markdown(summary))
        self.console.print()
        
        self.memory.add_log(summary, source="Assistant")