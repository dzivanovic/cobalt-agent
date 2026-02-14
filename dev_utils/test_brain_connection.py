import os
import sys

# Add project root to path so we can import 'cobalt_agent'
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from dotenv import load_dotenv
from cobalt_agent.llm import LLM

# 1. Load the secrets
load_dotenv()

# 2. Get the model name from .env
# NOTE: We force the 'ollama/' prefix to test the local routing logic
model_name = os.getenv("OLLAMA_MODEL", "qwen2.5:14b")
if not model_name.startswith("ollama/"):
    full_model = f"ollama/{model_name}"
else:
    full_model = model_name

print(f"🧠 Testing Connection to: {full_model}")
print(f"📡 Target URL: {os.getenv('OLLAMA_BASE_URL', 'Not Set')}")

try:
    # 3. Initialize the Brain
    brain = LLM(model_name=full_model)

    # 4. Ask a question
    response = brain.ask("Are you running on the Mac Studio?")

    print("\n--- RESPONSE ---")
    print(response)
    print("----------------")
    print("✅ SUCCESS: The Brain is Online.")

except Exception as e:
    print(f"\n❌ FAILED: {e}")
    print("Tip: Check if Ollama is running and OLLAMA_HOST=0.0.0.0 is set if remote.")