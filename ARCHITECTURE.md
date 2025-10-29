# Skill Chain Toolkit Architecture

This document explains the internal architecture of the Interdependent Skills Toolkit and the principles behind skill chain design.

## Table of Contents

- [Overview](#overview)
- [Core Concepts](#core-concepts)
- [Toolkit Components](#toolkit-components)
- [Skill Chain Patterns](#skill-chain-patterns)
- [Design Principles](#design-principles)
- [Implementation Details](#implementation-details)

## Overview

The Interdependent Skills Toolkit is a framework for creating chains of related skills for Claude Code where each skill builds upon previous ones. This creates more powerful compound workflows than independent skills can provide.

### Key Innovation

Traditional skills are **independent** - each skill contains all knowledge needed to perform its task. This leads to:
- Duplication of common knowledge across skills
- Longer skill files
- Difficulty maintaining consistency
- Limited ability to create complex workflows

Skill chains are **interdependent** - each skill assumes knowledge from previous skills. This enables:
- Progressive disclosure of complexity
- Focused, single-purpose skills
- Compound workflows that build naturally
- Reusable foundational concepts

## Core Concepts

### 1. Foundation Skill

The first skill in any chain. Special properties:
- **No prerequisites** - completely self-contained
- **Establishes terminology** - defines key concepts for the domain
- **Provides base patterns** - workflows that other skills will extend
- **Comprehensive but focused** - covers fundamentals without trying to do everything

Example: A "document-processing-foundation" skill defines what a "document structure" is, how to load documents, and basic error handling. All subsequent skills reference these concepts.

### 2. Dependent Skills

Skills that build on previous skills:
- **Explicit prerequisites** - clearly states which skills it requires
- **References without repeating** - uses phrases like "As established in..."
- **Extends base patterns** - adds new capabilities to foundation workflows
- **Focused purpose** - does ONE thing well

Example: A "document-data-extraction" skill assumes you know what "document structure" means (from foundation) and extends the loading workflow with extraction capabilities.

### 3. Skill Chain

The complete sequence of skills from foundation to specialized capabilities:
- **Linear progression** - each skill builds on all previous skills
- **3-7 skills typical** - enough to be powerful, not overwhelming
- **Domain-focused** - all skills work together for one task area
- **Documented flow** - users understand the progression

### 4. Progressive Disclosure

Information architecture principle:
- **SKILL.md** - core workflows only (under 500 lines)
- **references/** - detailed examples and patterns
- **scripts/** - pre-written, tested code
- **assets/** - templates and boilerplate

Users get exactly the information they need, when they need it.

## Toolkit Components

### init_skill.py

**Purpose**: Initialize new skill directory with proper structure

**How it works**:
1. Creates directory with naming convention: `{number:02d}_{skill-name}`
2. Sets up subdirectories: `scripts/`, `references/`, `assets/`
3. Generates `SKILL.md` from template
4. Creates reference templates (`examples.md`, `patterns.md`, `api_docs.md`)
5. Adds `.gitkeep` files for empty directories

**Templates**:
- Foundation template (no prerequisites section)
- Dependent template (with prerequisites section)
- Skill chain position diagram

**Design decisions**:
- Number prefix enforces ordering
- Lowercase with hyphens for consistency
- Standard directory structure for predictability
- Comprehensive but editable templates

### quick_validate.py

**Purpose**: Validate skill structure and content before packaging

**Validation checks**:

1. **Structure validation**:
   - SKILL.md exists
   - Standard directories present (optional but recommended)

2. **YAML frontmatter validation**:
   - Properly formatted YAML
   - Required fields: `name`, `description`
   - Name follows conventions (lowercase, hyphens)
   - Description is comprehensive (75+ chars)

3. **Content validation**:
   - Required sections present (Overview, When to Use)
   - Recommended sections present (Core Workflows, Prerequisites)
   - Referenced files actually exist
   - Line count under 500 (warning if exceeded)

4. **Script validation**:
   - Scripts are mentioned in SKILL.md
   - Shell scripts are executable (Unix)

5. **Reference validation**:
   - Reference files are mentioned in SKILL.md
   - No orphaned reference files

**Output modes**:
- Normal: Shows errors, warnings, and info
- Quiet: Shows only errors and warnings
- Strict: Treats warnings as errors (for CI/CD)

**Design decisions**:
- Fail fast on errors
- Helpful warnings for improvements
- Informational output for verification
- Strict mode for automated pipelines

### package_skill.py

**Purpose**: Package validated skill into distributable .skill file

**Process**:
1. Run validation (reuses validation logic)
2. Fail if validation errors found
3. Warn if validation warnings present
4. Create ZIP archive with `.skill` extension
5. Include all relevant files
6. Exclude development files (`.pyc`, `__pycache__`, hidden files)

**Archive structure**:
```
{number:02d}_{skill-name}.skill (ZIP archive)
├── SKILL.md
├── scripts/
│   └── [script files]
├── references/
│   └── [reference files]
└── assets/
    └── [asset files]
```

**Design decisions**:
- ZIP format (universally supported, inspectable)
- `.skill` extension (clear purpose)
- Validate before packaging (catch errors early)
- Clean archives (no development artifacts)
- Preserves directory structure

## Skill Chain Patterns

### Pattern 1: Linear Chain

Most common pattern. Each skill depends only on previous skills in sequence:

```
00_foundation (no dependencies)
    ↓
01_skill_a (depends on: 00)
    ↓
02_skill_b (depends on: 00, 01)
    ↓
03_skill_c (depends on: 00, 01, 02)
```

**When to use**: Most use cases. Clear progression, easy to understand.

**Example**: Document processing (load → extract → analyze)

### Pattern 2: Branching Chain

Foundation with multiple independent branches:

```
00_foundation
    ├→ 01_branch_a
    │      ↓
    │  02_branch_a_extended
    │
    └→ 01_branch_b
           ↓
       02_branch_b_extended
```

**When to use**: Domain has distinct sub-workflows that don't depend on each other.

**Example**: API toolkit (foundation → [authentication, rate-limiting, caching] as separate branches)

### Pattern 3: Diamond Pattern

Multiple skills converge to an integration skill:

```
00_foundation
    ├→ 01_skill_a
    └→ 01_skill_b
         ↓     ↓
       02_integration (depends on: 00, 01_a, 01_b)
```

**When to use**: Need to combine capabilities from multiple parallel skills.

**Example**: Testing (foundation → [unit tests, integration tests] → test reporting)

## Design Principles

### 1. Single Responsibility

Each skill has ONE clear purpose:
- ✓ "Extract data from documents"
- ✗ "Process documents" (too broad)

### 2. Explicit Over Implicit

Dependencies and requirements are stated clearly:
- List all prerequisites
- Explain why each is needed
- Reference specific concepts from previous skills

### 3. DRY (Don't Repeat Yourself)

Between skills in a chain:
- Define concepts once in foundation
- Reference them in later skills
- Don't re-explain what previous skills covered

### 4. Progressive Complexity

Skills build from simple to complex:
- Foundation: Core concepts, simple workflows
- Early skills: Basic extensions
- Later skills: Advanced combinations

### 5. Discoverability

Users can find and understand skills:
- Comprehensive descriptions
- Clear "When to Use" sections
- Explicit trigger phrases
- Skill chain position documented

### 6. Testability

Skills can be validated:
- Validation script checks structure
- Examples demonstrate usage
- Scripts are pre-tested
- Clear success/failure criteria

## Implementation Details

### Skill File Structure

```
XX_skill-name/
├── SKILL.md                    # 200-500 lines
│   ├── YAML frontmatter        # name, description
│   ├── Prerequisites           # what skills are required
│   ├── Overview                # 2-3 sentence summary
│   ├── When to Use             # specific triggers
│   ├── Core Workflows          # step-by-step instructions
│   ├── References              # pointer to ref files
│   └── Skill Chain Position    # where in chain
│
├── scripts/                    # Optional
│   ├── helper.py              # Pre-written utilities
│   └── example.sh             # Shell scripts
│
├── references/                 # Extended docs
│   ├── examples.md            # Detailed examples
│   ├── patterns.md            # Common patterns
│   └── api_docs.md            # API reference
│
└── assets/                     # Optional
    ├── template.txt           # File templates
    └── boilerplate.py         # Code templates
```

### YAML Frontmatter Format

```yaml
---
name: skill-name-in-kebab-case
description: "75+ character comprehensive description including what the skill does, when to use it, key trigger phrases, and how it relates to other skills in the chain."
---
```

### Interdependency Documentation Pattern

In each dependent skill's SKILL.md:

```markdown
## Prerequisites

This skill requires:
- **00_foundation**: Provides [specific concepts/patterns used]
- **01_previous**: Provides [specific outputs/capabilities needed]

## Core Workflows

### Workflow 1: [Name]

As established in the foundation skill, first [reference base workflow]:

1. [Base step from foundation]
2. [Extension specific to this skill]
3. [New capability]
```

### Skill Chain Position Pattern

```markdown
## Skill Chain Position

This skill is part of a chain:
00_foundation - [one line description]
   ↓
01_previous - [one line description]
   ↓
**→ 02_current** (current) - [one line description]
   ↓
03_next - [one line description]

**Comes after:** [list with explanations]
**Enables:** [list with explanations]
```

## Extending the Toolkit

### Adding New Validation Rules

In `quick_validate.py`, add to the `SkillValidator` class:

```python
def validate_custom_rule(self):
    """Check for custom requirement."""
    # Add validation logic
    # Append to self.errors, self.warnings, or self.info
```

Add call in `validate_all()` method.

### Adding New Templates

In `init_skill.py`, modify the `SKILL_TEMPLATE` constant or add new templates.

### Supporting New Skill Patterns

Create new initialization modes:
```python
parser.add_argument(
    "--pattern",
    choices=["linear", "branching", "diamond"],
    help="Skill chain pattern to use"
)
```

## Best Practices for Implementation

### For Toolkit Developers

1. **Keep tools simple** - Single responsibility per script
2. **Validate early** - Catch errors before packaging
3. **Provide helpful output** - Clear messages for users
4. **Follow conventions** - Consistent naming, structure
5. **Document thoroughly** - Both code and user-facing docs

### For Skill Chain Creators

1. **Plan before coding** - Design full chain first
2. **Start with foundation** - Get base concepts right
3. **Test each skill** - Validate before moving to next
4. **Document dependencies** - Explicit > implicit
5. **Provide examples** - Show, don't just tell
6. **Keep skills focused** - One purpose per skill

### For Skill Users

1. **Install in order** - Foundation first, then dependents
2. **Read prerequisites** - Understand what you need
3. **Follow examples** - Learn the patterns
4. **Combine skills** - Use the full chain for best results

## Future Enhancements

Potential additions to the toolkit:

1. **Dependency Graph Generator** - Visualize skill chains
2. **Batch Operations** - Validate/package entire chains
3. **Skill Templates** - Pre-built chains for common domains
4. **Version Management** - Track skill versions and compatibility
5. **Installation Script** - Automated skill installation
6. **Chain Validator** - Validate entire chain consistency
7. **Documentation Generator** - Auto-generate chain docs
8. **Testing Framework** - Unit tests for skills

## Conclusion

The Interdependent Skills Toolkit provides a structured approach to creating sophisticated skill ecosystems for Claude Code. By following the patterns and principles outlined here, you can create powerful, maintainable, and discoverable skill chains that enable complex workflows while remaining easy to understand and use.

The key insight is that **interdependence creates power** - by building skills that reference and extend each other, we create capabilities greater than the sum of their parts.
