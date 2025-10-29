#!/usr/bin/env python3
"""
Skill Dependency Checker
Analyzes skill files to show installation order and dependencies.
"""

import sys
import argparse
import yaml
import re
from pathlib import Path
from typing import Dict, List, Set, Tuple


def extract_prerequisites(skill_md_content: str) -> List[str]:
    """Extract prerequisite skills from SKILL.md content."""
    prerequisites = []

    # Look for Prerequisites section
    match = re.search(r'## Prerequisites\s*\n(.*?)(?=\n## |\Z)', skill_md_content, re.DOTALL)
    if not match:
        return prerequisites

    prereq_section = match.group(1)

    # Extract skill references like "**00_foundation**" or "00_foundation"
    skill_refs = re.findall(r'\*?\*?(\d{2}_[\w\-]+)\*?\*?', prereq_section)

    # Filter out the placeholder text
    for ref in skill_refs:
        if 'foundation' in ref or 'previous' in ref or ref.startswith('0'):
            if ref not in prerequisites:
                prerequisites.append(ref)

    return prerequisites


def analyze_skill_file(skill_path: Path) -> Dict:
    """Analyze a skill directory or .skill file."""
    skill_info = {
        'name': None,
        'number': None,
        'description': None,
        'prerequisites': [],
        'is_foundation': False
    }

    # Determine if it's a directory or .skill file
    if skill_path.is_dir():
        skill_md = skill_path / 'SKILL.md'
    else:
        # It's a .skill file - would need to unzip, skip for now
        print(f"Skipping {skill_path.name} - .skill files need to be extracted first")
        return None

    if not skill_md.exists():
        return None

    content = skill_md.read_text()

    # Extract YAML frontmatter
    parts = content.split('---', 2)
    if len(parts) >= 3:
        try:
            frontmatter = yaml.safe_load(parts[1])
            skill_info['name'] = frontmatter.get('name')
            skill_info['description'] = frontmatter.get('description', '')
        except yaml.YAMLError:
            pass

    # Get skill number from directory name
    dir_name = skill_path.name
    match = re.match(r'(\d{2})_', dir_name)
    if match:
        skill_info['number'] = int(match.group(1))

    # Extract prerequisites
    skill_info['prerequisites'] = extract_prerequisites(content)

    # Check if it's a foundation skill
    if 'no prerequisites' in content.lower() or skill_info['number'] == 0:
        skill_info['is_foundation'] = True

    return skill_info


def build_dependency_graph(skills_dir: Path) -> Dict[str, Dict]:
    """Build dependency graph from skills directory."""
    skills = {}

    # Find all skill directories
    for skill_path in sorted(skills_dir.iterdir()):
        if not skill_path.is_dir():
            continue

        if not re.match(r'\d{2}_', skill_path.name):
            continue

        skill_info = analyze_skill_file(skill_path)
        if skill_info and skill_info['name']:
            skills[skill_path.name] = skill_info

    return skills


def determine_install_order(skills: Dict[str, Dict]) -> List[str]:
    """Determine correct installation order based on dependencies."""
    # Sort by skill number (foundation skills first)
    return sorted(skills.keys(), key=lambda x: skills[x]['number'])


def display_dependency_tree(skills: Dict[str, Dict], install_order: List[str]):
    """Display the dependency tree visually."""
    print("\n" + "="*70)
    print("SKILL CHAIN DEPENDENCY ANALYSIS")
    print("="*70 + "\n")

    for i, skill_dir in enumerate(install_order):
        skill = skills[skill_dir]
        number = skill['number']
        name = skill['name']

        # Display skill
        if skill['is_foundation']:
            marker = "🔷 FOUNDATION"
        else:
            marker = "◆"

        print(f"{marker} [{number:02d}] {skill_dir}")
        print(f"    Name: {name}")

        if skill['prerequisites']:
            print(f"    Prerequisites: {', '.join(skill['prerequisites'])}")
        else:
            print(f"    Prerequisites: None")

        if skill['description']:
            # Truncate description
            desc = skill['description'][:100]
            if len(skill['description']) > 100:
                desc += "..."
            print(f"    Description: {desc}")

        # Show dependency arrow to next skill
        if i < len(install_order) - 1:
            print("    ↓")

        print()


def display_install_instructions(skills: Dict[str, Dict], install_order: List[str]):
    """Display installation instructions."""
    print("="*70)
    print("RECOMMENDED INSTALLATION ORDER")
    print("="*70 + "\n")

    print("Install skills in this order to satisfy dependencies:\n")

    for i, skill_dir in enumerate(install_order, 1):
        skill = skills[skill_dir]
        status = "REQUIRED" if skill['is_foundation'] else "OPTIONAL"
        print(f"{i}. claude-code install {skill_dir}.skill  # {status}")

    print("\n" + "-"*70)
    print("NOTE: Foundation skills (00_*) are required by dependent skills.")
    print("You can skip optional skills if you don't need their functionality.")
    print("-"*70 + "\n")


def check_missing_prerequisites(skills: Dict[str, Dict]) -> List[Tuple[str, List[str]]]:
    """Check for skills that reference non-existent prerequisites."""
    issues = []
    skill_dirs = set(skills.keys())

    for skill_dir, skill in skills.items():
        if skill['prerequisites']:
            for prereq in skill['prerequisites']:
                if prereq not in skill_dirs:
                    issues.append((skill_dir, prereq))

    return issues


def main():
    parser = argparse.ArgumentParser(
        description="Analyze skill chain dependencies and determine installation order."
    )
    parser.add_argument(
        "skills_dir",
        help="Directory containing skill subdirectories"
    )
    parser.add_argument(
        "--install-order-only",
        action="store_true",
        help="Only show installation order"
    )
    parser.add_argument(
        "--check",
        action="store_true",
        help="Check for missing prerequisites"
    )

    args = parser.parse_args()

    skills_dir = Path(args.skills_dir)

    if not skills_dir.exists():
        print(f"Error: Directory does not exist: {skills_dir}")
        sys.exit(1)

    if not skills_dir.is_dir():
        print(f"Error: Not a directory: {skills_dir}")
        sys.exit(1)

    # Build dependency graph
    skills = build_dependency_graph(skills_dir)

    if not skills:
        print(f"No skills found in {skills_dir}")
        sys.exit(1)

    # Determine installation order
    install_order = determine_install_order(skills)

    if args.check:
        # Check for issues
        issues = check_missing_prerequisites(skills)
        if issues:
            print("⚠️  WARNING: Missing prerequisites detected:")
            for skill_dir, missing_prereq in issues:
                print(f"  {skill_dir} requires {missing_prereq} (not found)")
            print()

    if args.install_order_only:
        # Just show the order
        print("Installation order:")
        for i, skill_dir in enumerate(install_order, 1):
            print(f"{i}. {skill_dir}")
    else:
        # Full analysis
        display_dependency_tree(skills, install_order)
        display_install_instructions(skills, install_order)


if __name__ == "__main__":
    main()
