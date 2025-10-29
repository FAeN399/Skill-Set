# Claude Code: Interdependent Skills Repository Generator

## Overview

You will create a GitHub repository that contains a chain of interdependent skills for a specific task domain. Each skill will be packaged as a complete, distributable .skill file following Anthropic's skill creation standards.

## Repository Structure

Create the following structure:

```
[repo-name]/
├── README.md                           # Overview of the skill chain
├── ARCHITECTURE.md                     # How skills interconnect
├── skills/
│   ├── 00_foundation/                  # Foundation skill (independent)
│   │   ├── SKILL.md
│   │   ├── scripts/
│   │   ├── references/
│   │   └── assets/
│   ├── 01_[skill-name]/                # Second skill (uses foundation)
│   │   ├── SKILL.md
│   │   ├── scripts/
│   │   ├── references/
│   │   └── assets/
│   ├── 02_[skill-name]/                # Third skill (uses foundation + 01)
│   │   └── ...
│   └── ...
├── dist/                               # Packaged .skill files
│   ├── 00_foundation.skill
│   ├── 01_[skill-name].skill
│   └── ...
└── tools/
    ├── init_skill.py                   # Skill initialization script
    ├── package_skill.py                # Skill packaging script
    └── quick_validate.py               # Validation script
```

## Critical Requirements

### 1. Skill Chain Architecture

**Foundation Skill (00_foundation)**
- Self-contained and independent
- Establishes core concepts, terminology, and base workflows
- Provides foundational patterns that subsequent skills will reference
- Cannot reference other skills in the chain (it's first)

**Subsequent Skills (01, 02, 03...)**
- Each skill explicitly references and builds upon previous skills
- Must include in SKILL.md: "**Prerequisites:** This skill requires [list of previous skills]"
- Reference previous skills using: "As established in the [skill-name] skill..."
- Extend functionality rather than duplicate knowledge
- Each skill focuses on ONE specific aspect of the task domain

### 2. SKILL.md Format Requirements

Each SKILL.md must contain:

```yaml
---
name: skill-name
description: "Specific description of what this skill does and when to use it. Include key trigger phrases and contexts. Be comprehensive yet concise."
---
```

Followed by markdown body:

```markdown
# [Skill Name]

## Prerequisites
[For non-foundation skills] This skill requires:
- [00_foundation]: [brief reason]
- [previous skills]: [brief reason]

## Overview
[What this skill does, 2-3 sentences]

## When to Use This Skill
[Specific triggers and contexts]

## Core Workflows
[Step-by-step instructions]

## References
[If using references/ folder, list them here]
```

### 3. Progressive Disclosure Pattern

**Keep SKILL.md concise** (under 500 lines):
- Core workflow instructions in SKILL.md
- Detailed examples in `references/examples.md`
- API documentation in `references/api_docs.md`
- Complex patterns in `references/patterns.md`

**Reference files must be explicitly mentioned** in SKILL.md with guidance on when to read them.

### 4. Skill Interdependence Rules

**How skills reference each other:**

1. **Direct Knowledge Reference:**
   ```markdown
   As defined in the foundation skill, a [concept] is...
   ```

2. **Workflow Extension:**
   ```markdown
   This skill extends the [workflow name] from the [previous skill] by adding...
   ```

3. **Tool Chain:**
   ```markdown
   Use this skill after completing the [previous skill]'s [process] to...
   ```

4. **Context Assumption:**
   ```markdown
   Assuming you have already established [concepts from foundation skill]...
   ```

### 5. Resource Organization

**scripts/** - When to include:
- Code is rewritten repeatedly
- Deterministic reliability required
- Complex operations that benefit from pre-tested implementation

**references/** - When to include:
- Documentation that should be loaded on-demand
- Examples and patterns
- API specifications
- Domain knowledge that would bloat SKILL.md

**assets/** - When to include:
- Templates to be copied/modified
- Boilerplate code
- Files used in output (not documentation)

### 6. Validation Requirements

Each skill must pass validation:
- Valid YAML frontmatter (name, description)
- Description is comprehensive (75+ chars)
- All referenced files exist
- Scripts are executable
- No duplicate content between SKILL.md and references
- Proper skill naming (lowercase, hyphens)

## Implementation Instructions

### Step 1: Initialize Repository

1. Create repository structure
2. Copy tool scripts from `/mnt/skills/public/skill-creator/scripts/`:
   - `init_skill.py`
   - `package_skill.py`
   - `quick_validate.py`

### Step 2: Define Skill Chain for Domain

Before creating any skills, document in ARCHITECTURE.md:

1. **Domain Overview:** What task domain are these skills for?
2. **Skill Breakdown:** List each skill with:
   - Name and purpose
   - What it adds to the chain
   - Dependencies on previous skills
   - Specific use cases

3. **Flow Diagram:** Show how skills connect

Example structure:
```
00_foundation (Core concepts) 
    ↓
01_data-extraction (Uses foundation concepts)
    ↓
02_data-validation (Uses extraction + foundation)
    ↓
03_data-transformation (Uses all previous)
    ↓
04_output-generation (Uses all previous)
```

### Step 3: Create Foundation Skill (00_foundation)

1. Use `init_skill.py` to create skill directory
2. Define core concepts, terminology, workflows
3. Establish patterns that subsequent skills will extend
4. Keep focused on fundamentals
5. Include comprehensive examples in references/
6. Test and validate

### Step 4: Create Subsequent Skills

For each additional skill:

1. Use `init_skill.py` to create skill directory
2. **Document prerequisites** explicitly in SKILL.md
3. **Reference foundation concepts** using: "As established in [previous skill]..."
4. **Extend, don't duplicate** - assume knowledge from previous skills
5. Focus on ONE specific aspect
6. Add only what's NEW for this skill
7. Test and validate

### Step 5: Create Interdependence Documentation

In each skill's SKILL.md, include:

```markdown
## Skill Chain Position

This skill is part of a chain:
[List skills in order with current highlighted]

**Comes after:** [Previous skills]
**Enables:** [Next skills, if known]
```

### Step 6: Package Skills

For each skill:
```bash
python tools/package_skill.py skills/[skill-folder] dist/
```

This validates and creates distributable .skill files.

### Step 7: Create Repository Documentation

**README.md** should include:
- Overview of the skill chain
- Installation instructions for each skill
- Usage order (start with foundation, progress through chain)
- Example workflows using the full chain

**ARCHITECTURE.md** should document:
- How skills interconnect
- What each skill adds
- When to use which combination of skills
- Decision tree for skill selection

## Best Practices

### Conciseness
- Assume Claude is already smart
- Add only non-obvious information
- Use examples over explanations
- Keep SKILL.md under 500 lines

### Specificity
- Each skill has ONE clear purpose
- Descriptions include specific trigger phrases
- Clear boundaries between skills

### Testability
- Include example use cases
- Provide sample inputs/outputs
- Scripts are pre-tested and working

### Discoverability
- Clear skill names
- Comprehensive descriptions
- Explicit prerequisites listed
- Reference files mentioned in SKILL.md

## Quality Checklist

Before considering the repository complete, verify:

- [ ] Each skill has valid YAML frontmatter
- [ ] Foundation skill is fully self-contained
- [ ] Each subsequent skill explicitly references prerequisites
- [ ] No duplicated content across skills
- [ ] All referenced files exist
- [ ] SKILL.md files are under 500 lines
- [ ] Each skill has specific, clear purpose
- [ ] Skills build logically on each other
- [ ] All skills validate successfully
- [ ] All skills package successfully into .skill files
- [ ] ARCHITECTURE.md documents the complete chain
- [ ] README.md provides clear usage instructions
- [ ] Example workflows demonstrate the chain

## Output Requirements

The final repository should be:
1. **Functional:** All skills validate and package
2. **Complete:** Full documentation and examples
3. **Organized:** Clear structure and naming
4. **Distributable:** .skill files ready for use
5. **Maintainable:** Clear architecture for future extensions

The user should be able to:
1. Clone the repository
2. Understand the skill chain architecture
3. Package any skill for distribution
4. Use skills individually or as a complete chain
5. Extend the chain with additional skills following the pattern

---

## Example Task Domain

[User will specify their task domain here]

When you receive the task domain, analyze it to determine:
1. How many skills are needed (typically 3-7)
2. What the foundation skill should establish
3. How each skill builds on previous ones
4. What specific functionality each skill provides

Then proceed with implementation following this prompt's structure.
