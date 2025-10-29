# Document Processing Skill Chain Example

This is an example skill chain demonstrating how to create interdependent skills for Claude Code. This example implements a simple document processing workflow with three interconnected skills.

## Skill Chain Overview

```
00_foundation (Document Processing Foundation)
    ↓ Establishes document structure, loading patterns, error handling
01_extraction (Document Data Extraction)
    ↓ Uses foundation patterns to extract structured data
02_analysis (Document Content Analysis)
    ↓ Analyzes extracted data to generate insights
```

## Skills in This Chain

### 00_foundation - Document Processing Foundation
- **Purpose**: Foundation skill establishing core concepts
- **What it provides**: Document loading patterns, structure analysis, error handling
- **Dependencies**: None (it's the foundation)
- **Key concepts**: Document structure, content blocks, metadata

### 01_extraction - Document Data Extraction
- **Purpose**: Extract structured data from documents
- **What it provides**: Field extraction, table parsing, entity recognition
- **Dependencies**: Requires 00_foundation
- **Extends**: Uses foundation's loading and structure analysis patterns

### 02_analysis - Document Content Analysis
- **Purpose**: Analyze extracted content for insights
- **What it provides**: Sentiment analysis, keyword extraction, comparative analysis
- **Dependencies**: Requires 00_foundation and 01_extraction
- **Extends**: Processes data extracted by 01_extraction using foundation patterns

## How Interdependency Works

This example demonstrates the key patterns for skill interdependency:

1. **Foundation Establishes Terminology**
   - The foundation skill defines terms like "content blocks" and "document structure"
   - Subsequent skills reference these terms without re-explaining them

2. **Workflows Build on Each Other**
   - Extraction skill starts with: "As established in the foundation skill, first load and parse..."
   - Analysis skill starts with: "Using data extracted from the extraction skill..."

3. **Explicit Prerequisites**
   - Each skill lists exactly which previous skills it depends on
   - Each skill explains WHY it needs each prerequisite

4. **No Duplication**
   - Extraction skill doesn't re-explain document loading (foundation covers it)
   - Analysis skill doesn't re-explain extraction (previous skill covers it)

## Using This Example

This example is meant to demonstrate the pattern. To use it:

1. Study how each skill references previous skills
2. Note the explicit prerequisite sections
3. See how workflows build incrementally
4. Observe the skill chain position documentation

## Packaging These Skills

From the repository root:

```bash
# Validate each skill
python3 tools/quick_validate.py examples/document-processing/skills/00_foundation
python3 tools/quick_validate.py examples/document-processing/skills/01_extraction
python3 tools/quick_validate.py examples/document-processing/skills/02_analysis

# Package each skill
python3 tools/package_skill.py examples/document-processing/skills/00_foundation dist/
python3 tools/package_skill.py examples/document-processing/skills/01_extraction dist/
python3 tools/package_skill.py examples/document-processing/skills/02_analysis dist/
```

This creates three `.skill` files in the `dist/` directory ready for distribution.

## Key Takeaways

When creating your own skill chain:

1. **Start with a foundation skill** that establishes core concepts
2. **Make dependencies explicit** in the Prerequisites section
3. **Reference previous skills** using phrases like "As established in..." or "Using the pattern from..."
4. **Don't duplicate knowledge** - assume users have the prerequisite skills
5. **Document the chain position** so users understand the flow
6. **Keep each skill focused** on ONE specific aspect

This example is intentionally simple to demonstrate the structure. Real skill chains can be more complex but should follow these same patterns.
