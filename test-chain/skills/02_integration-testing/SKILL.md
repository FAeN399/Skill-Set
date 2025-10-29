---
name: api-integration-testing
description: "Tests multi-endpoint workflows and data flow across API operations. Combines foundation test patterns with endpoint testing strategies to validate complete user journeys, transaction flows, and system integrations. Use when testing workflows that span multiple endpoints, validating data consistency, or testing complex business processes. Requires both foundation and endpoint-testing skills."
---

# API Integration Testing

## Prerequisites

This skill requires:
- **00_api-testing-foundation**: Provides test structure patterns and assertion strategies used throughout integration tests
- **01_endpoint-testing**: Provides individual endpoint testing patterns that are combined into workflows

## Overview

This skill combines concepts from both foundation and endpoint-testing skills to test complete workflows across multiple API endpoints. It validates data flow, state management, and business logic that spans multiple operations.

## When to Use This Skill

Use this skill when:
- Testing complete user workflows (signup → login → create resource → update → delete)
- Validating data consistency across multiple endpoints
- Testing transaction flows with multiple steps
- Verifying system integrations and data propagation
- Testing complex business processes that involve multiple API calls

**Important:** This skill assumes you understand both the foundation test patterns AND individual endpoint testing strategies.

## Core Workflows

### Workflow 1: Basic Integration Test Flow

Combining foundation's arrange-act-assert with endpoint-testing's strategies:

1. **Arrange**: Set up test environment (from foundation skill)
   - Prepare authentication
   - Set up initial test data
   - Define the workflow endpoints sequence

2. **Act**: Execute multi-step workflow
   - Use endpoint-testing patterns for each step
   - Capture state/data from each response
   - Pass data between requests (e.g., created ID)

3. **Assert**: Validate workflow outcomes
   - Apply foundation's assertion patterns at each step
   - Verify final system state
   - Confirm data consistency across endpoints

### Workflow 2: CRUD Integration Test

Using endpoint-testing skills in sequence with foundation patterns:

1. **Create**: POST new resource (using endpoint-testing POST pattern)
   - Capture created resource ID
   - Verify 201 status (foundation assertion)

2. **Read**: GET the created resource (using endpoint-testing GET pattern)
   - Use ID from step 1
   - Verify 200 status and data matches creation

3. **Update**: PUT/PATCH the resource (using endpoint-testing patterns)
   - Modify specific fields
   - Verify 200 status and updated fields

4. **Delete**: DELETE the resource (using endpoint-testing patterns)
   - Verify 204 No Content

5. **Verify Deletion**: GET the deleted resource
   - Verify 404 Not Found (foundation status validation)

### Workflow 3: Transaction Flow Testing

As established in foundation and endpoint-testing skills:

1. Test each transaction step using endpoint patterns
2. Validate data propagation between steps
3. Test rollback scenarios (if applicable)
4. Verify error handling in multi-step flows
5. Use foundation's status code and body validation throughout

## References

- See `references/examples.md` for detailed examples
- See `references/patterns.md` for common patterns
- See `references/api_docs.md` for API documentation (if applicable)

## Skill Chain Position

This skill is part of a chain:
00_api-testing-foundation - HTTP concepts and test patterns
   ↓
01_endpoint-testing - Testing individual endpoints
   ↓
**→ 02_integration-testing** (current) - Testing multi-endpoint workflows

**Comes after:** 00_api-testing-foundation (uses test patterns), 01_endpoint-testing (combines endpoint patterns into workflows)
**Enables:** Further skills could include performance testing, load testing, or automated test reporting
