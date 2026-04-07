import os
import sys
from loguru import logger
from src.cobalt_agent.llm import LLM

# Disable noisy logging for the test to keep output clean
logger.remove()

def run_tests():
    print("==================================================")
    print("🧪 INITIATING LLM SWITCHBOARD ROUTING TEST")
    print("==================================================")
    
    # TEST 1: The Local Route (Qwen via LM Studio)
    print("\n[TEST 1] Initializing 'coder' profile (Expected: Local/Mainframe)")
    try:
        local_llm = LLM(role="coder")
        print(f"✅ Route Resolved: {local_llm._model_name}")
        print(f"✅ API Base Resolved: {local_llm._api_base}")
        print("⏳ Pinging local model (this may take a few seconds)...")
        
        response = local_llm.generate_response_skill("Reply with exactly two words: 'Local Online'. Do not say anything else.")
        print(f"🟢 LLM RESPONSE: {response}")
    except Exception as e:
        print(f"❌ TEST 1 FAILED: {str(e)}")

    # TEST 2: The Cloud Route (Gemini via Google API)
    print("\n[TEST 2] Initializing 'researcher' profile (Expected: Cloud Gemini)")
    try:
        cloud_llm = LLM(role="researcher")
        print(f"✅ Route Resolved: {cloud_llm._model_name}")
        print(f"✅ API Base Resolved: {cloud_llm._api_base}")
        print("⏳ Pinging cloud model...")
        
        response = cloud_llm.generate_response_skill("Reply with exactly two words: 'Cloud Online'. Do not say anything else.")
        print(f"🟢 LLM RESPONSE: {response}")
    except Exception as e:
        print(f"❌ TEST 2 FAILED: {str(e)}")
        
    print("\n==================================================")
    print("🏁 TEST RUN COMPLETE")
    print("==================================================")

if __name__ == "__main__":
    run_tests()