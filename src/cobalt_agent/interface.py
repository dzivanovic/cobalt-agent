"""
Cobalt Agent - Interactive CLI Interface
Refactored: Centralized Routing + RAG (Retrieval Augmented Generation)
"""

from rich.console import Console
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
                
                # Save to Short-Term Memory immediately
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

    def _retrieve_long_term_memory(self, query: str) -> str:
        """
        RAG HOOK: Searches the Postgres DB for relevant past context.
        """
        if not hasattr(self.memory, "search"):
            return ""

        try:
            self.console.print("[dim]🧠 Recalling...[/dim]")
            
            # 1. Fetch MORE (10 instead of 3) to break through the "Echo Chamber"
            results = self.memory.search(query, limit=10)
            
            if not results:
                return ""
            
            # 2. Deduplicate & Format
            seen_content = set()
            unique_memories = []
            
            for mem in results:
                # Extract content safely
                if hasattr(mem, "content"):
                    content = mem.content
                    timestamp = getattr(mem, "timestamp", "Unknown")
                elif isinstance(mem, dict):
                    content = mem.get("content", "")
                    timestamp = mem.get("timestamp", "Unknown")
                else:
                    content = str(mem)
                    timestamp = "Unknown"
                
                # CLEANUP: Remove whitespace and skip if empty
                content = content.strip()
                if not content: continue
                
                # DEDUPLICATION: If we already saw this exact sentence, skip it.
                # This prevents "What is my favorite stock?" appearing 5 times.
                if content in seen_content:
                    continue
                
                # SELF-FILTER: Don't show the user's *current* question as a memory
                if content == query.strip():
                    continue

                seen_content.add(content)
                unique_memories.append((timestamp, content))
            
            # 3. Limit the final output to the top 5 UNIQUE results
            final_memories = unique_memories[:5]
            
            if not final_memories:
                return ""

            self.console.print(f"[dim green]Found {len(final_memories)} unique memories:[/dim green]")
            
            memory_block = "\n\n=== RELEVANT LONG-TERM MEMORY ===\n"
            for ts, text in final_memories:
                # Print preview for you
                clean_preview = text.replace("\n", " ")[:80]
                self.console.print(f"[dim]  - [{ts}] {clean_preview}...[/dim]")
                
                # Add to context
                memory_block += f"- [{ts}] {text}\n"
            
            return memory_block
            
        except Exception as e:
            logger.warning(f"Memory retrieval failed: {e}")
            return ""

    def _handle_chat(self, user_input: str):
        """Autonomous Agent Loop (ReAct Pattern) for general analysis."""
        self.console.print(f"[dim]Thinking...[/dim]")
        
        turn_history = [] 
        current_input = user_input
        MAX_TURNS = 5
        
        # --- STEP 1: RAG (Retrieval) ---
        # Fetch past memories relevant to this specific input
        long_term_context = self._retrieve_long_term_memory(user_input)
        
        # --- CRITICAL FIX: INJECT MEMORY INTO SYSTEM PROMPT ---
        # We modify the system prompt for THIS RUN ONLY.
        # This forces the LLM to treat the memory as an absolute rule/fact.
        run_specific_system_prompt = self.system_prompt
        if long_term_context:
            run_specific_system_prompt += f"\n\n{long_term_context}"
        
        for turn in range(MAX_TURNS):
            # 1. Get Short Term RAM
            short_term_context = self.memory.get_context()
            
            # Combine RAM + History (But NOT Long Term, that's in System Prompt now)
            full_history = str(short_term_context)
            if turn > 0:
                for t in turn_history:
                    full_history += f"\n{t['role']}: {t['content']}"
            
            # 2. Ask Brain
            response = self.llm.think(
                user_input=current_input,
                system_prompt=run_specific_system_prompt, # <--- The "Memory-Enhanced" Prompt
                memory_context=full_history
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