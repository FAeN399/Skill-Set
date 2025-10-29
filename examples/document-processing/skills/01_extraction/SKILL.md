---
name: document-data-extraction
description: "Extracts structured data from documents using patterns established in the foundation skill. Handles text extraction, table parsing, metadata collection, and entity recognition. Use when you need to pull specific information from documents like names, dates, financial data, or custom fields. Builds on foundation document loading and structure analysis."
---

# Document Data Extraction

## Prerequisites

This skill requires:
- **00_foundation**: Provides document loading patterns, structure analysis, and error handling that this skill extends

## Overview

This skill extends the foundation skill's document loading and structure analysis to extract specific data elements from documents. It adds targeted extraction patterns for common data types and provides tools for custom extraction rules.

## When to Use This Skill

Use this skill when:
- Extracting specific fields from documents (names, dates, amounts)
- Parsing tables into structured data
- Collecting metadata across multiple documents
- Finding and extracting entities (people, organizations, locations)
- Building datasets from document collections

**Important:** This skill assumes you have already loaded the document using the foundation skill's loading pattern.

## Core Workflows

### Workflow 1: Field Extraction

As established in the foundation skill, first load and parse the document structure, then:

1. Define target fields and their expected formats
2. Apply extraction patterns to relevant document sections
3. Validate extracted data against expected types
4. Handle missing or malformed data using foundation error patterns
5. Return structured field data

### Workflow 2: Table Extraction

Using the foundation skill's content block identification:

1. Locate table blocks in the document structure
2. Extract table headers and data rows
3. Convert to structured format (dict, DataFrame, etc.)
4. Handle merged cells and complex layouts
5. Return tabular data with metadata

## References

- See `references/examples.md` for detailed examples
- See `references/patterns.md` for common patterns
- See `references/api_docs.md` for API documentation (if applicable)

## Skill Chain Position

This skill is part of a chain:
00_foundation - Document structure and base patterns
   ↓
**→ 01_extraction** (current) - Extract specific data
   ↓
02_analysis - Analyze extracted content

**Comes after:** 00_foundation (uses document loading and structure analysis patterns)
**Enables:** 02_analysis (provides extracted data for analysis)
