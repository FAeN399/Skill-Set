---
name: api-testing-foundation
description: "Foundation skill for API testing workflows. Establishes core HTTP concepts (methods, status codes, headers), defines test structure patterns (arrange-act-assert), and provides base assertion strategies. Use when starting API testing tasks, setting up test frameworks, or defining test patterns for REST APIs."
---

# API Testing Foundation

## Prerequisites

[This is a foundation skill - no prerequisites]

## Overview

This foundation skill establishes core concepts and patterns for API testing. It defines HTTP terminology, test structure patterns, and base assertion strategies that all subsequent API testing skills will build upon.

## When to Use This Skill

Use this skill when:
- Starting any API testing project or task
- Setting up API test infrastructure
- Defining test structure and organization
- Understanding HTTP concepts for testing
- Establishing assertion patterns for API responses
- Creating base test utilities

## Core Workflows

### Workflow 1: Basic API Test Structure

1. **Arrange**: Set up test data and environment
   - Define base URL and endpoints
   - Prepare request headers (authentication, content-type)
   - Create test payload if needed

2. **Act**: Execute the API request
   - Make HTTP request (GET, POST, PUT, DELETE, etc.)
   - Capture response

3. **Assert**: Verify the response
   - Check status code (200, 201, 404, 500, etc.)
   - Validate response body structure
   - Verify response headers
   - Confirm timing/performance if needed

### Workflow 2: HTTP Status Code Validation

1. Identify expected status code for the operation
2. Execute API request
3. Assert response.status_code matches expected
4. Log meaningful error if mismatch

### Workflow 3: Response Body Validation

1. Define expected response schema or structure
2. Execute API request and get response body
3. Parse response (JSON, XML, etc.)
4. Validate structure matches expectations
5. Assert specific field values if needed

## References

- See `references/examples.md` for detailed examples
- See `references/patterns.md` for common patterns
- See `references/api_docs.md` for API documentation (if applicable)

## Skill Chain Position

This skill is part of a chain:
**→ 00_api-testing-foundation** (foundation) - HTTP concepts and test patterns
   ↓
01_endpoint-testing - Testing individual endpoints
   ↓
02_integration-testing - Testing multi-endpoint workflows

**Comes after:** None (foundation skill)
**Enables:** endpoint-testing, integration-testing, and all other API testing skills
