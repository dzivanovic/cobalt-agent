# lightspeed_formatter.py

## Overview

The `lightspeed_formatter.py` script is a rapid output formatting utility designed to generate structured, presentation-ready content from Cobalt's analysis results. It provides templated output formats for reports, summaries, and actionable intelligence.

## Purpose

This script serves the following functions:
- Formats analysis output into consistent, readable formats
- Generates structured reports from raw data
- Supports multiple output templates for different use cases
- Enables quick export of findings in various formats

## Location

```
dev_utils/lightspeed_formatter.py
```

## Dependencies

- Standard Python libraries for text processing and formatting
- Rich library for terminal output styling

## How It Works

The formatter operates through the following process:

1. **Input Reception**: Accepts raw data or analysis results
2. **Template Selection**: Applies appropriate formatting template based on content type
3. **Structure Generation**: Organizes content into predefined sections
4. **Output Rendering**: Displays formatted result in terminal or exports to file

## Usage

### Running the Script

From the project root:

```bash
uv run dev_utils/lightspeed_formatter.py --input <data_source> --template <template_name>
```

### Available Templates

| Template | Description | Use Case |
|----------|-------------|----------|
| `summary` | Concise executive summary | Quick briefings |
| `report` | Full structured report | Detailed analysis |
| `actionable` | Action-oriented format | Trading decisions |
| `technical` | Technical specification format | Engineering docs |

### Command-Line Arguments

| Argument | Description | Required |
|----------|-------------|----------|
| `--input` | Input data source (file path or stdin) | Yes |
| `--template` | Formatting template to apply | No (default: summary) |
| `--output` | Output file path (optional, defaults to stdout) | No |

## Expected Output

On successful execution, the script will display:
- Formatted content with proper structure and styling
- Section headers and organized data presentation

On failure, it will provide:
- Error messages indicating input or template issues
- Suggestions for correcting the input format

## Troubleshooting

| Issue | Possible Cause | Solution |
|-------|---------------|----------|
| Template Not Found | Invalid template name | Verify template exists in formatter configuration |
| Input Parse Error | Malformed input data | Check input format matches expected schema |
| Output Encoding Issue | Character encoding mismatch | Specify explicit encoding for output file |

## Related Documentation

- [Scribe](scribe.md) - Automated documentation generation
- [Briefing](briefing.md) - Daily briefing generation

## Maintenance Notes

This script should be used:
- When generating reports from analysis results
- For creating consistent output across different Cobalt modules
- During presentations or stakeholder reviews requiring formatted output