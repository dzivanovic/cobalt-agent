# check_gemini_models.py

## Overview

The `check_gemini_models.py` script is a diagnostic utility designed to verify the availability and responsiveness of Google's Gemini AI models. It performs health checks against the Gemini API to ensure that model endpoints are accessible and functioning correctly before they are needed by Cobalt's AI-powered components.

## Purpose

This script serves as a pre-flight check tool for:
- Validating Gemini API connectivity
- Testing model endpoint responsiveness
- Diagnosing authentication and configuration issues
- Ensuring AI model availability before critical operations

## Location

```
dev_utils/check_gemini_models.py
```

## Dependencies

- `google-generativeai` - Google's official Gemini SDK
- Standard Python libraries: `os`, `sys`, `pathlib`

## How It Works

The script performs the following operations:

1. **API Configuration Check**: Verifies that the `GEMINI_API_KEY` environment variable is set
2. **Model Endpoint Testing**: Attempts to connect to configured Gemini model endpoints
3. **Response Validation**: Checks that API responses are valid and models are operational
4. **Error Reporting**: Provides detailed error messages for troubleshooting

## Usage

### Prerequisites

1. Set your Gemini API key as an environment variable:
```bash
export GEMINI_API_KEY="your-api-key-here"
```

### Running the Script

Navigate to the `dev_utils` directory and execute:

```bash
cd dev_utils
python check_gemini_models.py
```

Or from the project root:

```bash
uv run dev_utils/check_gemini_models.py
```

## Expected Output

On successful execution, the script will display:
- Status of each tested model endpoint
- Response times and latency metrics
- Confirmation of API connectivity

On failure, it will provide:
- Specific error messages indicating the root cause
- Suggestions for troubleshooting (e.g., API key validity, network connectivity)

## Troubleshooting

| Issue | Possible Cause | Solution |
|-------|---------------|----------|
| API Key Error | `GEMINI_API_KEY` not set or invalid | Verify environment variable is exported correctly |
| Connection Timeout | Network issues or API endpoint down | Check internet connectivity and Gemini service status |
| Model Not Found | Incorrect model name/configuration | Verify the model name matches available Gemini models |

## Related Documentation

- [LLM Module](llm.md) - Core LLM integration details
- [Configuration](config.md) - Environment setup guidelines

## Maintenance Notes

This script should be run:
- Before deploying new AI-powered features
- When troubleshooting Gemini API connectivity issues
- Periodically as part of system health checks