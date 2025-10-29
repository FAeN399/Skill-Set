---
name: api-endpoint-testing
description: "Tests individual API endpoints using patterns from the foundation skill. Covers CRUD operations, parameter validation, authentication testing, error handling, and edge cases. Use when testing specific API endpoints, validating request/response contracts, or creating endpoint-specific test suites. Builds on foundation test structure and assertion patterns."
---

# API Endpoint Testing

## Prerequisites

This skill requires:
- **00_api-testing-foundation**: Provides the arrange-act-assert pattern, HTTP concepts, and base assertion strategies that this skill applies to specific endpoint testing scenarios

## Overview

This skill extends the foundation skill's test patterns to test individual API endpoints comprehensively. It provides specific strategies for testing CRUD operations, parameter validation, and error scenarios for single endpoints.

## When to Use This Skill

Use this skill when:
- Testing a specific API endpoint (GET /users, POST /orders, etc.)
- Validating endpoint parameter handling (query params, path params, body)
- Testing endpoint authentication and authorization
- Verifying endpoint error responses
- Creating test suites for individual endpoints

**Important:** This skill assumes you understand the arrange-act-assert pattern and HTTP concepts from the foundation skill.

## Core Workflows

### Workflow 1: Testing a GET Endpoint

Using the foundation skill's arrange-act-assert pattern:

1. **Arrange**: Set up as established in foundation skill
   - Define endpoint URL (e.g., `/api/users/{id}`)
   - Prepare authentication headers
   - Identify test data (valid/invalid IDs)

2. **Act**: Execute GET request using foundation pattern

3. **Assert**: Apply foundation's assertion strategies
   - Verify 200 status for valid ID
   - Verify 404 status for invalid ID
   - Validate response body structure
   - Check response time

### Workflow 2: Testing a POST Endpoint

Extending the foundation skill's test structure for creation:

1. **Arrange**: Prepare request body with test data
2. **Act**: Execute POST request
3. **Assert**: Using foundation assertion patterns:
   - Verify 201 Created status
   - Validate response includes created resource
   - Verify Location header if applicable
   - Test with invalid data (400 Bad Request)
   - Test duplicate creation (409 Conflict)

### Workflow 3: Parameter Validation Testing

As established in the foundation skill, structure tests for:

1. Test with valid parameters (expect success)
2. Test with missing required parameters (expect 400)
3. Test with invalid parameter types (expect 400)
4. Test with out-of-range values (expect 400)
5. Apply foundation's status code validation for each case

## References

- See `references/examples.md` for detailed examples
- See `references/patterns.md` for common patterns
- See `references/api_docs.md` for API documentation (if applicable)

## Skill Chain Position

This skill is part of a chain:
00_api-testing-foundation - HTTP concepts and test patterns
   ↓
**→ 01_endpoint-testing** (current) - Testing individual endpoints
   ↓
02_integration-testing - Testing multi-endpoint workflows

**Comes after:** 00_api-testing-foundation (uses arrange-act-assert pattern and assertion strategies)
**Enables:** 02_integration-testing (provides endpoint testing patterns for workflow testing)
