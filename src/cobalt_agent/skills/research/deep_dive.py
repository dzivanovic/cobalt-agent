"""
Deep Research Agent
Implements a "Plan -> Search -> Analyze -> Report" loop.
Strictly uses Pydantic for type-safe LLM interactions.
"""
import json
from typing import List
from loguru import logger
from pydantic import BaseModel, Field, ValidationError

from cobalt_agent.llm import LLM
from cobalt_agent.config import load_config
from cobalt_agent.tools.search import SearchTool
from cobalt_agent.tools.browser import BrowserTool
from cobalt_agent.skills.productivity.scribe import Scribe

# --- PYDANTIC SCHEMAS ---
class ResearchPlan(BaseModel):
    """The strategy for researching a topic."""
    queries: List[str] = Field(
        description="A list of 3 specific, distinct search queries to investigate the topic from different angles."
    )

class ResearchReport(BaseModel):
    """The final synthesized report structure."""
    title: str = Field(description="A clear, professional title for the report.")
    executive_summary: str = Field(description="A high-level summary of the findings.")
    key_findings: List[str] = Field(description="A list of the most important technical or financial facts found.")
    strategic_outlook: str = Field(description="Forward-looking analysis or conclusion.")

# --- AGENT ---
class DeepResearch:
    def __init__(self):
        # 1. Load Global Config
        config = load_config()
        
        # 2. Extract Model Name
        if hasattr(config.llm, "model_name"):
            self.model_name = config.llm.model_name
        else:
            self.model_name = getattr(config.llm, "model", "gpt-4o")

        # 3. Initialize Components
        self.llm = LLM(model_name=self.model_name)
        self.search = SearchTool()
        self.browser = BrowserTool()
        self.scribe = Scribe()

    def run(self, topic: str):
        """
        Executes a multi-step research plan on a complex topic.
        """
        logger.info(f"🕵️‍♂️ Starting Deep Dive on: {topic} (Model: {self.model_name})")
        
        # --- PHASE 1: PLANNING ---
        logger.info("🧠 Phase 1: Planning research strategy...")
        
        plan_prompt = f"Create a research plan for the topic: '{topic}'. Generate 3 distinct search queries."
        
        try:
            plan: ResearchPlan = self.llm.ask_structured(plan_prompt, ResearchPlan)
            queries = plan.queries
            logger.info(f"📋 Plan approved: {queries}")
        except Exception:
            logger.warning("Failed to generate structured plan. Falling back to defaults.")
            queries = [f"{topic} technology overview", f"{topic} market size", f"{topic} key players"]

        # --- PHASE 2: EXECUTION (The Loop) ---
        findings = []
        for q in queries:
            logger.info(f"🔍 Executing Step: {q}")
            try:
                # Search returns List[SearchResult] objects now
                results = self.search.run(q)
                
                # Format the Pydantic objects into a readable string for the LLM
                formatted_results = ""
                for item in results:
                    formatted_results += f"Title: {item.title}\nURL: {item.href}\nSummary: {item.body}\n---\n"
                
                if not formatted_results:
                    formatted_results = "No results found."

                findings.append(f"### Query: {q}\n{formatted_results}\n")
                
            except Exception as e:
                logger.error(f"Search step failed for '{q}': {e}")

        # --- PHASE 3: SYNTHESIS ---
        logger.info("✍️ Phase 3: Synthesizing Final Report...")
        all_data = "\n".join(findings)
        
        synthesis_prompt = f"""
        Analyze these raw notes on '{topic}' and generate a final report.
        
        RAW NOTES:
        {all_data}
        """
        
        try:
            report: ResearchReport = self.llm.ask_structured(synthesis_prompt, ResearchReport)
            
            # Convert Pydantic model to Markdown for Obsidian
            md_content = f"# {report.title}\n\n"
            md_content += f"**Date:** Today\n\n"
            md_content += f"## Executive Summary\n{report.executive_summary}\n\n"
            md_content += "## Key Findings\n"
            for item in report.key_findings:
                md_content += f"- {item}\n"
            md_content += f"\n## Strategic Outlook\n{report.strategic_outlook}"
            
        except Exception as e:
            logger.error(f"Report synthesis failed: {e}")
            md_content = f"# Research Failed\nCould not generate structured report for {topic}.\n\nRaw Data:\n{all_data}"

        # --- PHASE 4: DELIVERY ---
        filename = f"Research_{topic.replace(' ', '_')}"
        path = self.scribe.write_note(filename, md_content, folder="0 - Inbox")
        
        return path