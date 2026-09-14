# LLM Switchboard Routing Test

**Source File:** `dev_utils/test_routing.py`  
**Author:** Cobalt SRE  
**Related Task:** [Task 38 - Refactor Switchboard Router](../Tasks/38%20Refactor%20Switchboard%20Router.md)  
**Sprint:** Sprint 06 - Data Engine  

---

## Overview

This integration test validates the LLM switchboard routing mechanism that dynamically selects appropriate language models based on role profiles. It verifies both local (Mainframe) and cloud-based model routing paths.

---

## Purpose

The script tests the following capabilities:

1. **Role-Based Model Resolution** - Confirms that different roles (`coder`, `researcher`) resolve to the correct model backend
2. **Local Model Connectivity** - Tests connection to locally-hosted models via LM Studio
3. **Cloud Model Connectivity** - Tests connection to cloud-based Gemini models via Google API
4. **API Base Configuration** - Verifies that correct API endpoints are resolved for each route

---

## Test Scenarios

### TEST 1: Local Route (Qwen via LM Studio)
**Profile:** `coder`  
**Expected Backend:** Local/Mainframe (LM Studio)  
**Model:** Qwen series model hosted locally  

This test validates the local inference path:
- Initializes LLM with `role="coder"`
- Resolves model name and API base from configuration
- Pings the local model to verify connectivity
- Expects response within acceptable latency

### TEST 2: Cloud Route (Gemini via Google API)
**Profile:** `researcher`  
**Expected Backend:** Cloud (Google Gemini API)  
**Model:** Gemini series model via Google API  

This test validates the cloud inference path:
- Initializes LLM with `role="researcher"`
- Resolves model name and API base from configuration
- Pings the cloud model to verify connectivity
- Expects response via Google's API endpoint

---

## Configuration Requirements

This script requires the following environment variables in `.env`:

### Local Model (LM Studio)
```bash
# LM Studio Configuration
LM_STUDIO_BASE_URL=http://localhost:1234/v1
LOCAL_MODEL=qwen
```

### Cloud Model (Google Gemini)
```bash
# Google Gemini Configuration
GOOGLE_API_KEY=<your-google-api-key>
GEMINI_MODEL=gemini-pro
```

---

## Execution

### Running the Test
```bash
cd /Users/cobalt/cobalt
python dev_utils/test_routing.py
```

### Expected Output (Success)
```
==================================================
🧪 INITIATING LLM SWITCHBOARD ROUTING TEST
==================================================

[TEST 1] Initializing 'coder' profile (Expected: Local/Mainframe)
✅ Route Resolved: qwen
✅ API Base Resolved: http://localhost:1234/v1
⏳ Pinging local model (this may take a few seconds)...
🟢 LLM RESPONSE: Local Online

[TEST 2] Initializing 'researcher' profile (Expected: Cloud Gemini)
✅ Route Resolved: gemini-pro
✅ API Base Resolved: https://generativelanguage.googleapis.com
⏳ Pinging cloud model...
🟢 LLM RESPONSE: Cloud Online

==================================================
🏁 TEST RUN COMPLETE
==================================================
```

### Expected Output (Local Model Offline)
```
[TEST 1] Initializing 'coder' profile (Expected: Local/Mainframe)
✅ Route Resolved: qwen
✅ API Base Resolved: http://localhost:1234/v1
⏳ Pinging local model (this may take a few seconds)...
❌ TEST 1 FAILED: Connection refused (LM Studio not running)
```

---

## Functions Reference

| Function | Description | Returns |
|----------|-------------|---------|
| `run_tests()` | Executes both routing test scenarios | None (prints results) |

---

## Dependencies

| Package | Purpose |
|---------|---------|
| `loguru` | Structured logging (disabled for clean output) |
| `src.cobalt_agent.llm.LLM` | Core LLM class with role-based routing |

---

## Error Handling

| Exception Type | Trigger Condition | Response |
|----------------|-------------------|----------|
| `ConnectionError` | LM Studio server offline or unreachable | Test failure with connection error details |
| `AuthenticationError` | Invalid Google API key | Test failure with auth error details |
| `TimeoutError` | Model response timeout | Test failure with timeout details |
| `Exception` | Any unexpected errors | Test failure with full error message |

---

## Exit Codes

| Code | Meaning |
|------|---------|
| `0` | All tests completed (regardless of pass/fail) |

---

## Related Documentation

- [Task 38 - Refactor Switchboard Router](../Tasks/38%20Refactor%20Switchboard%20Router.md)
- [Task 41 - Dynamic Persona Engine](../Tasks/41%20Dynamic%20Persona%20Engine.md)
- [LLM Documentation](./llm.md)
- [Sprint 06 - Data Engine](../../90%20-%20Project%20Management/Sprints/Sprint_06_Data_Engine.md)

---

## Author Notes

This test is designed to verify the dual-path architecture of Cobalt's LLM routing system. Both tests run sequentially regardless of individual test outcomes, providing a complete picture of the routing configuration. The `logger.remove()` call ensures clean output without verbose logging noise.