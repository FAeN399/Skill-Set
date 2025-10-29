---
name: document-processing-foundation
description: "Foundation skill for document processing workflows. Establishes core concepts for handling various document formats (PDF, DOCX, TXT), defines document structure terminology (sections, metadata, content blocks), and provides base patterns for reading, parsing, and organizing document data. Use when starting any document processing task."
---

# Document Processing Foundation

## Prerequisites

[This is a foundation skill - no prerequisites]

## Overview

This skill establishes the foundational concepts and patterns for processing documents programmatically. It defines terminology, data structures, and base workflows that all subsequent document processing skills will build upon.

## When to Use This Skill

Use this skill when:
- Starting any document processing workflow
- Need to understand document structure terminology
- Setting up initial document parsing infrastructure
- Defining how to represent documents in memory
- Establishing error handling patterns for document operations

## Core Workflows

### Workflow 1: Document Loading

1. Identify document format (by extension or content analysis)
2. Select appropriate parser for the format
3. Load document into memory with error handling
4. Extract basic metadata (title, author, creation date)
5. Return structured document object

### Workflow 2: Document Structure Analysis

1. Parse document into logical sections
2. Identify content blocks (paragraphs, headings, lists, tables)
3. Build document tree structure
4. Extract section hierarchy
5. Return structured representation

### Workflow 3: Error Handling Pattern

1. Attempt document operation
2. Catch format-specific errors
3. Log error with context
4. Attempt fallback strategy if available
5. Return result or meaningful error message

## References

- See `references/examples.md` for detailed examples
- See `references/patterns.md` for common patterns
- See `references/api_docs.md` for API documentation (if applicable)

## Skill Chain Position

This skill is part of a chain:
**→ 00_foundation** (foundation) - Document structure and base patterns
   ↓
01_extraction - Extract specific data from documents
   ↓
02_analysis - Analyze extracted content

**Comes after:** None (foundation skill)
**Enables:** extraction, analysis, and all other document processing skills
