"""
Cobalt Agent - Interactive CLI Interface
Refactored: Centralized Routing via Cortex Manager.
"""

from rich.console import Console
from rich.prompt import Prompt
from loguru import logger
from rich.markdown import Markdown

# Type hinting
from typing import Optional, TYPE_CHECKING, Any
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

                # 1. CORTEX ROUTING (The Primary Brain)
                handled_by_cortex = False
                if self.cortex:
                    # Cortex decides: Tactical? Intel? Ops? Or None (General Chat)?
                    specialist_response = self.cortex.route(user_input)
                    
                    if specialist_response:
                        # Cortex returned a result (e.g., Raw Data or Note Status)
                        self.console.print(f"\n[bold purple]🤖 Cortex:[/bold purple]")
                        self.console.print(Markdown(specialist_response))
                        self.console.print()
                        
                        # Crucial: Log this to memory so the LLM "sees" it for follow-up analysis
                        self.memory.add_log(specialist_response, source="System")
                        handled_by_cortex = True
                
                # If Cortex handled it, we loop back to let user ask follow-up (e.g. "Analyze this")
                if handled_by_cortex: continue 
                
                # 2. AUTONOMOUS CHAT (The Fallback / Analyst)
                # Handles "Analyze that", "Hi", or generic questions Cortex didn't claim.
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
        """Autonomous Agent Loop (ReAct Pattern) for general analysis."""
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
            
            # 3. Check for ACTION (Tool Use by the LLM itself)
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