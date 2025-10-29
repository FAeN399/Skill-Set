# Claude Code: Interdependent Skills Toolkit

A framework for creating chains of interdependent skills for Claude Code. This toolkit provides tools and templates for building sophisticated skill ecosystems where each skill builds upon previous ones, creating powerful compound workflows.

## What is This?

This repository is a **meta-toolkit** - it's not a specific skill chain, but rather a complete framework for *creating* skill chains. It provides:

- **Tool scripts** for initializing, validating, and packaging skills
- **Templates** that follow Anthropic's skill creation standards
- **Example skill chain** demonstrating interdependency patterns
- **Documentation** on best practices for skill chain architecture

## Why Skill Chains?

Traditional skills are independent - each skill works alone. **Skill chains** create interdependency where:

- A **foundation skill** establishes core concepts and terminology
- **Subsequent skills** build on these foundations without duplicating knowledge
- Each skill focuses on ONE specific aspect of a domain
- Skills explicitly reference and extend previous skills
- The result is more powerful than individual skills

### Example: Document Processing Chain

```
00_foundation (Document Structure & Loading)
    ↓ establishes document terminology, loading patterns
01_extraction (Data Extraction)
    ↓ uses foundation patterns to extract structured data
02_analysis (Content Analysis)
    ↓ analyzes extracted data for insights
```

Each skill assumes knowledge from previous skills, avoiding duplication and creating a progressive learning path.

## Quick Start

### 1. Create Your First Foundation Skill

```bash
python3 tools/init_skill.py my-foundation --number 0 --foundation --output-dir skills
```

This creates:
```
skills/00_my-foundation/
├── SKILL.md              # Main skill definition
├── scripts/              # Reusable code
├── references/           # Extended documentation
└── assets/               # Templates and resources
```

### 2. Edit the Generated SKILL.md

Edit `skills/00_my-foundation/SKILL.md` to define:
- What the skill does
- Core concepts and terminology
- Base workflows
- When to use it

### 3. Create Dependent Skills

```bash
python3 tools/init_skill.py data-extraction --number 1 --output-dir skills
```

Edit the new skill to:
- List prerequisites (requires 00_foundation)
- Reference foundation concepts: "As established in the foundation skill..."
- Extend rather than duplicate workflows

### 4. Validate Your Skills

```bash
python3 tools/quick_validate.py skills/00_my-foundation
python3 tools/quick_validate.py skills/01_data-extraction
```

### 5. Package for Distribution

```bash
python3 tools/package_skill.py skills/00_my-foundation dist/
python3 tools/package_skill.py skills/01_data-extraction dist/
```

This creates `.skill` files (zip archives) ready for distribution.

## Repository Structure

```
Skill-Set/
├── README.md                          # This file
├── ARCHITECTURE.md                    # Framework architecture
├── claude_code_skill_chain_prompt.md  # Original prompt/specification
├── tools/                             # Toolkit scripts
│   ├── init_skill.py                  # Initialize new skill
│   ├── package_skill.py               # Package and validate skill
│   ├── quick_validate.py              # Validate skill structure
│   └── check_dependencies.py          # Analyze dependencies & install order
├── examples/                          # Example skill chains
│   └── document-processing/           # Complete example
│       ├── README.md
│       └── skills/
│           ├── 00_foundation/
│           ├── 01_extraction/
│           └── 02_analysis/
└── dist/                              # Packaged .skill files

# Your skills go here (not included):
skills/                                # Your skill chain directory
├── 00_your-foundation/
├── 01_your-skill/
└── 02_your-skill/
```

## Tool Reference

### init_skill.py

Initialize a new skill with proper structure.

```bash
python3 tools/init_skill.py SKILL_NAME --number N [--foundation] [--output-dir DIR]

Options:
  --number N          Skill number in chain (0 for foundation, 1, 2, 3...)
  --foundation        Create as foundation skill (no prerequisites)
  --output-dir DIR    Where to create skill (default: ./skills)
```

**Examples:**
```bash
# Create foundation skill
python3 tools/init_skill.py api-foundation --number 0 --foundation

# Create dependent skill
python3 tools/init_skill.py api-authentication --number 1
```

### quick_validate.py

Validate skill structure and content.

```bash
python3 tools/quick_validate.py SKILL_PATH [--strict] [--quiet]

Options:
  --strict    Treat warnings as errors
  --quiet     Only show errors and warnings
```

**Checks:**
- Valid YAML frontmatter
- Required fields (name, description)
- Description length (75+ chars recommended)
- Required sections (Overview, When to Use)
- Referenced files exist
- Naming conventions

### package_skill.py

Package a skill into distributable .skill file.

```bash
python3 tools/package_skill.py SKILL_PATH OUTPUT_DIR [--force] [--validate-only]

Options:
  --force           Overwrite existing .skill file
  --validate-only   Only validate, don't package
```

Creates a `.skill` file (zip archive) containing the complete skill.

### check_dependencies.py

Analyze skill chain dependencies and determine installation order.

```bash
python3 tools/check_dependencies.py SKILLS_DIR [--install-order-only] [--check]

Options:
  --install-order-only    Only show installation order
  --check                 Check for missing prerequisites
```

**Example output:**
```
SKILL CHAIN DEPENDENCY ANALYSIS
══════════════════════════════════════════════════════════

🔷 FOUNDATION [00] 00_api-testing-foundation
    Name: api-testing-foundation
    Prerequisites: None
    ↓
◆ [01] 01_endpoint-testing
    Name: api-endpoint-testing
    Prerequisites: 00_api-testing-foundation
    ↓
◆ [02] 02_integration-testing
    Name: api-integration-testing
    Prerequisites: 00_api-testing-foundation, 01_endpoint-testing

RECOMMENDED INSTALLATION ORDER
══════════════════════════════════════════════════════════
1. claude-code install 00_api-testing-foundation.skill  # REQUIRED
2. claude-code install 01_endpoint-testing.skill  # OPTIONAL
3. claude-code install 02_integration-testing.skill  # OPTIONAL
```

Use this tool to help users understand which skills to install and in what order.

## Creating a Skill Chain

### Step 1: Plan Your Chain

Before creating any skills, plan your chain in an ARCHITECTURE.md file:

1. **Define the domain** - What task area are these skills for?
2. **Break it down** - What are 3-7 logical progression steps?
3. **Define dependencies** - What does each skill need from previous ones?
4. **Name your skills** - Clear, descriptive names (lowercase-with-hyphens)

Example domains:
- API development workflow (design → implement → test → document)
- Data pipeline (extract → validate → transform → load)
- Testing workflow (unit → integration → e2e → reporting)
- Content creation (research → draft → edit → publish)

### Step 2: Create Foundation Skill

The foundation skill is special:
- **No prerequisites** - it's self-contained
- **Establishes terminology** that other skills will use
- **Defines base patterns** that others will extend
- **Comprehensive** - includes core concepts for the domain

```bash
python3 tools/init_skill.py foundation --number 0 --foundation
```

### Step 3: Create Dependent Skills

Each subsequent skill:
- **Lists prerequisites explicitly** in SKILL.md
- **References previous skills**: "As established in [skill-name]..."
- **Extends, doesn't duplicate** - assumes prerequisite knowledge
- **Focuses on ONE aspect** of the domain

```bash
python3 tools/init_skill.py next-skill --number 1
```

### Step 4: Document Interdependencies

In each skill's SKILL.md:

```markdown
## Prerequisites

This skill requires:
- **00_foundation**: [why you need it]
- **01_previous**: [what it provides]

## Core Workflows

As established in the foundation skill, first [base workflow], then:
1. [New step]
2. [Extension]
```

### Step 5: Validate and Package

```bash
# Validate all skills
for skill in skills/*/; do
  python3 tools/quick_validate.py "$skill"
done

# Package all skills
for skill in skills/*/; do
  python3 tools/package_skill.py "$skill" dist/
done
```

## Best Practices

### Skill Design

1. **One purpose per skill** - Each skill should have a clear, focused purpose
2. **Progressive disclosure** - Keep SKILL.md concise, details in references/
3. **Explicit dependencies** - Always list and explain prerequisites
4. **Reference, don't repeat** - Use "As established in..." to reference previous skills
5. **Comprehensive descriptions** - 75+ chars, include trigger phrases

### Content Organization

**SKILL.md** (keep under 500 lines):
- Core workflow instructions
- Clear "When to Use" section
- Explicit prerequisites
- Skill chain position documentation

**references/** (unlimited):
- `examples.md` - Detailed examples
- `patterns.md` - Common patterns
- `api_docs.md` - API documentation

**scripts/** (when needed):
- Reusable, tested code
- Pre-written for reliability
- Documented in SKILL.md

**assets/** (when needed):
- Templates to copy/modify
- Boilerplate code
- Files used in output

### Interdependency Patterns

**Direct Knowledge Reference:**
```markdown
As defined in the foundation skill, a [concept] is...
```

**Workflow Extension:**
```markdown
This skill extends the [workflow name] from [previous skill] by adding...
```

**Context Assumption:**
```markdown
Assuming you have already [previous skill's output], this skill...
```

## Example: Document Processing Chain

See `examples/document-processing/` for a complete example showing:
- Foundation skill establishing document terminology
- Extraction skill building on foundation patterns
- Analysis skill using both previous skills
- Proper interdependency documentation
- Complete skill chain architecture

Study this example to understand the patterns.

## Validation Requirements

Each skill must pass validation:
- ✓ Valid YAML frontmatter (name, description)
- ✓ Description is comprehensive (75+ chars recommended)
- ✓ All referenced files exist
- ✓ Required sections present
- ✓ Proper naming (lowercase, hyphens)
- ✓ Prerequisites documented (for non-foundation skills)

## Distribution

Once packaged, `.skill` files can be:
- Shared directly with users
- Published in skill repositories
- Installed via Claude Code
- Distributed as a complete chain

### User Control and Installation

**Users have full control** over which skills they install:

#### Installation Order

Skills should be installed in dependency order:

```bash
# Install foundation first (required by others)
claude-code install 00_api-testing-foundation.skill

# Then install dependent skills
claude-code install 01_endpoint-testing.skill
claude-code install 02_integration-testing.skill
```

#### Selective Installation

Users can choose their level of functionality:

**Full Chain** (maximum capability):
```
Install: Foundation + All dependent skills
Result: Complete workflow support
```

**Partial Chain** (selective features):
```
Install: Foundation + Only needed skills
Result: Focused functionality
Example: Foundation + endpoint-testing (skip integration-testing)
```

**Foundation Only** (basics):
```
Install: Just the foundation skill
Result: Core concepts and patterns only
```

#### How Claude Invokes Skills

Once installed, Claude Code automatically selects skills based on:
1. **Task context** - What the user is asking for
2. **Skill descriptions** - Matching trigger phrases in YAML frontmatter
3. **"When to Use" section** - Explicit use cases listed in SKILL.md

Users don't manually invoke skills - Claude chooses the best match based on the request.

#### Prerequisites

If a user installs a dependent skill without its prerequisites:
- The skill will reference concepts from the missing foundation
- This may cause confusion
- **Best practice**: Always install foundation skills first

**For Skill Creators:**
Document installation order clearly in your skill chain's README.

## Contributing

This toolkit is designed to be extended. To add new features:

1. Tool scripts are in `tools/` - written in Python 3
2. Follow the existing patterns
3. Update documentation
4. Test with example skills

## Learn More

- See `ARCHITECTURE.md` for framework internals
- See `examples/document-processing/` for complete example
- See `claude_code_skill_chain_prompt.md` for original specification

## License

This toolkit is provided as-is for creating Claude Code skill chains. Use it to build amazing skill ecosystems!