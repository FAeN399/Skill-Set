#!/usr/bin/env python3
"""
Initialize a new skill in the narrative ecosystem
"""
import os
import sys
from pathlib import Path

def create_skill_structure(skill_number, skill_name, base_path="."):
    """Create directory structure for a new skill"""
    skill_dir = f"{skill_number:02d}-{skill_name}"
    skill_path = Path(base_path) / "skills" / skill_dir

    # Create directories
    directories = [
        skill_path,
        skill_path / "references",
        skill_path / "scripts",
        skill_path / "assets"
    ]

    for directory in directories:
        directory.mkdir(parents=True, exist_ok=True)
        print(f"✓ Created: {directory}")

    # Create placeholder SKILL.md
    skill_md = skill_path / "SKILL.md"
    with open(skill_md, 'w') as f:
        f.write(f"""---
name: {skill_name}
description: [Description of this skill and when to use it]
---

# {skill_name.replace('-', ' ').title()}

## Prerequisites

**Required Skills:**
- `00-foundation-prime`: Provides foundational patterns

## Purpose

[What this skill teaches, both narratively and practically]

## Building on the Foundation

[How this skill extends foundation patterns]

## Workflows

### Workflow 1: [Name]
[Steps]

## Narrative Context

[How this skill fits into the story world]

## Usage Patterns

- [When this skill triggers]

## Bundled Resources

- `references/foundation-context.md`: Foundation patterns reference
- `scripts/`: Utility scripts for this skill
""")
    print(f"✓ Created: {skill_md}")

    print(f"\n✅ Skill '{skill_name}' initialized at {skill_path}")
    print(f"📝 Edit {skill_md} to customize")

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python init_skill.py <skill_number> <skill-name>")
        print("Example: python init_skill.py 3 memory-keeper")
        sys.exit(1)

    skill_num = int(sys.argv[1])
    skill_name = sys.argv[2]

    create_skill_structure(skill_num, skill_name)
