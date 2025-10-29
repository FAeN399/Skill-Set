---
name: document-content-analysis
description: "Analyzes content extracted from documents to identify patterns, trends, and insights. Performs sentiment analysis, keyword extraction, topic modeling, and statistical analysis on document data. Use when you need to understand document content beyond basic extraction - finding themes, comparing documents, or generating summaries. Requires foundation and extraction skills."
---

# Document Content Analysis

## Prerequisites

This skill requires:
- **00_foundation**: Provides document structure terminology and error handling patterns
- **01_extraction**: Provides structured data that this skill analyzes

## Overview

This skill analyzes content extracted via the extraction skill to generate insights, identify patterns, and produce analytical summaries. It extends the extraction workflow by adding analytical processing to the structured data.

## When to Use This Skill

Use this skill when:
- Analyzing sentiment or tone in documents
- Identifying key themes and topics
- Comparing multiple documents for similarities/differences
- Generating executive summaries from extracted data
- Finding statistical patterns in document collections

**Important:** This skill assumes you have already extracted structured data using the extraction skill's workflows.

## Core Workflows

### Workflow 1: Content Analysis Pipeline

Using data extracted from the extraction skill:

1. Load extracted structured data (from extraction skill output)
2. Apply analysis methods (sentiment, keywords, topics)
3. Aggregate results across document sections
4. Identify patterns and outliers
5. Generate analysis report with visualizations

### Workflow 2: Comparative Analysis

Extending the foundation skill's document structure with extraction skill's data:

1. Load multiple document datasets (using extraction skill patterns)
2. Normalize data for comparison
3. Apply similarity metrics
4. Identify key differences and commonalities
5. Generate comparison report

## References

- See `references/examples.md` for detailed examples
- See `references/patterns.md` for common patterns
- See `references/api_docs.md` for API documentation (if applicable)

## Skill Chain Position

This skill is part of a chain:
00_foundation - Document structure and base patterns
   ↓
01_extraction - Extract specific data
   ↓
**→ 02_analysis** (current) - Analyze extracted content

**Comes after:** 00_foundation (uses structure/error patterns), 01_extraction (analyzes extracted data)
**Enables:** Further skills could include reporting, visualization, or automated decision-making based on analysis
