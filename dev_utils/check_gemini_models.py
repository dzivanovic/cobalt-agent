uv run python -c "
import google.generativeai as genai
import getpass

api_key = getpass.getpass('Paste your Gemini API Key and hit Enter (input is hidden): ').strip()

if not api_key:
    print('No key provided. Exiting.')
    exit(1)

try:
    genai.configure(api_key=api_key)
    print('\nQuerying Google Servers...')
    
    models = [m.name for m in genai.list_models() if 'generateContent' in m.supported_generation_methods]
    
    print('\n--- Authorized Models ---')
    for model in models:
        print(model)
        
except Exception as e:
    print(f'\nAPI Error: {e}')
"