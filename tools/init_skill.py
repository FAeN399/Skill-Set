#!/usr/bin/env python3
"""
Skill Initialization Script
Creates a new skill directory with proper structure for Claude Code skills.
"""

import os
import sys
import argparse
from pathlib import Path


SKILL_TEMPLATE = """---
name: {skill_name}
description: "Describe what this skill does and when to use it. Include key trigger phrases and contexts. Be comprehensive yet concise (75+ characters)."
---

# {skill_title}

## Prerequisites

{prerequisites_section}

## Overview

[What this skill does, 2-3 sentences]

## When to Use This Skill

[Specific triggers and contexts - be explicit about when Claude should invoke this skill]

## Core Workflows

### Workflow 1: [Name]

1. Step 1
2. Step 2
3. Step 3

## References

{references_section}

## Skill Chain Position

This skill is part of a chain:
{chain_position}

**Comes after:** {comes_after}
**Enables:** {enables}
"""


def create_skill_structure(skill_path: Path, skill_name: str, is_foundation: bool = False):
    """Create the directory structure for a skill."""
    skill_path.mkdir(parents=True, exist_ok=True)

    # Create subdirectories
    (skill_path / "scripts").mkdir(exist_ok=True)
    (skill_path / "references").mkdir(exist_ok=True)
    (skill_path / "assets").mkdir(exist_ok=True)

    # Create .gitkeep files for empty directories
    (skill_path / "scripts" / ".gitkeep").touch()
    (skill_path / "references" / ".gitkeep").touch()
    (skill_path / "assets" / ".gitkeep").touch()

    return True


def create_skill_md(skill_path: Path, skill_name: str, skill_number: int, is_foundation: bool = False):
    """Create the SKILL.md file with appropriate template."""

    # Format skill title (convert hyphens to spaces and title case)
    skill_title = skill_name.replace("-", " ").title()

    # Determine prerequisites section
    if is_foundation:
        prerequisites_section = "[This is a foundation skill - no prerequisites]"
        comes_after = "None (foundation skill)"
        enables = "All subsequent skills in the chain"
    else:
        prerequisites_section = """This skill requires:
- [00_foundation]: [brief reason]
- [Add other prerequisite skills]: [brief reason]"""
        comes_after = "[List previous skills]"
        enables = "[List skills that build on this one]"

    # Determine references section
    references_section = """- See `references/examples.md` for detailed examples
- See `references/patterns.md` for common patterns
- See `references/api_docs.md` for API documentation (if applicable)"""

    # Chain position
    if is_foundation:
        chain_position = f"""**→ {skill_number:02d}_{skill_name}** (foundation)
   ↓
01_[next-skill]
   ↓
..."""
    else:
        chain_position = f"""00_foundation
   ↓
...
   ↓
**→ {skill_number:02d}_{skill_name}** (current)
   ↓
..."""

    skill_content = SKILL_TEMPLATE.format(
        skill_name=skill_name,
        skill_title=skill_title,
        prerequisites_section=prerequisites_section,
        references_section=references_section,
        chain_position=chain_position,
        comes_after=comes_after,
        enables=enables
    )

    skill_md_path = skill_path / "SKILL.md"
    skill_md_path.write_text(skill_content)

    return skill_md_path


def create_reference_templates(skill_path: Path):
    """Create template reference files."""

    examples_content = """# Examples

## Example 1: [Title]

**Context:** [When to use this]

**Input:**
```
[Example input]
```

**Process:**
1. Step 1
2. Step 2

**Output:**
```
[Example output]
```

## Example 2: [Title]

[Add more examples as needed]
"""

    patterns_content = """# Common Patterns

## Pattern 1: [Pattern Name]

**When to use:** [Context]

**Implementation:**
```
[Code or steps]
```

**Notes:**
- [Important consideration 1]
- [Important consideration 2]

## Pattern 2: [Pattern Name]

[Add more patterns as needed]
"""

    api_docs_content = """# API Documentation

## Function/Method 1

**Description:** [What it does]

**Parameters:**
- `param1` (type): [Description]
- `param2` (type): [Description]

**Returns:** [Return type and description]

**Example:**
```
[Usage example]
```

## Function/Method 2

[Add more API documentation as needed]
"""

    (skill_path / "references" / "examples.md").write_text(examples_content)
    (skill_path / "references" / "patterns.md").write_text(patterns_content)
    (skill_path / "references" / "api_docs.md").write_text(api_docs_content)


def main():
    parser = argparse.ArgumentParser(
        description="Initialize a new skill directory structure for Claude Code skills."
    )
    parser.add_argument(
        "skill_name",
        help="Name of the skill (lowercase with hyphens, e.g., 'data-extraction')"
    )
    parser.add_argument(
        "--number",
        type=int,
        default=0,
        help="Skill number in the chain (e.g., 0 for foundation, 1 for first dependent skill)"
    )
    parser.add_argument(
        "--output-dir",
        default="./skills",
        help="Output directory for skills (default: ./skills)"
    )
    parser.add_argument(
        "--foundation",
        action="store_true",
        help="Create as foundation skill (no prerequisites)"
    )

    args = parser.parse_args()

    # Validate skill name format
    if not args.skill_name.replace("-", "").replace("_", "").isalnum():
        print(f"Error: Skill name must contain only letters, numbers, and hyphens/underscores")
        sys.exit(1)

    if not args.skill_name.islower():
        print(f"Warning: Skill name should be lowercase. Converting to: {args.skill_name.lower()}")
        args.skill_name = args.skill_name.lower()

    # Create skill directory name
    skill_dir_name = f"{args.number:02d}_{args.skill_name}"
    skill_path = Path(args.output_dir) / skill_dir_name

    if skill_path.exists():
        print(f"Error: Skill directory already exists: {skill_path}")
        sys.exit(1)

    print(f"Creating skill: {skill_dir_name}")
    print(f"Location: {skill_path}")
    print()

    # Create structure
    create_skill_structure(skill_path, args.skill_name, args.foundation)
    print("✓ Created directory structure")

    # Create SKILL.md
    skill_md = create_skill_md(skill_path, args.skill_name, args.number, args.foundation)
    print(f"✓ Created {skill_md}")

    # Create reference templates
    create_reference_templates(skill_path)
    print("✓ Created reference templates")

    print()
    print(f"✓ Skill initialized successfully!")
    print()
    print("Next steps:")
    print(f"1. Edit {skill_path}/SKILL.md to define your skill")
    print(f"2. Add examples to {skill_path}/references/examples.md")
    print(f"3. Add scripts to {skill_path}/scripts/ (if needed)")
    print(f"4. Add assets/templates to {skill_path}/assets/ (if needed)")
    print(f"5. Validate with: python tools/quick_validate.py {skill_path}")
    print(f"6. Package with: python tools/package_skill.py {skill_path} dist/")


if __name__ == "__main__":
    main()
