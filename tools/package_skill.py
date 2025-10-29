#!/usr/bin/env python3
"""
Skill Packaging Script
Packages a skill directory into a distributable .skill file (zip archive).
"""

import os
import sys
import argparse
import zipfile
import yaml
from pathlib import Path


def validate_skill_structure(skill_path: Path):
    """Validate that the skill has the required structure."""
    errors = []
    warnings = []

    # Check for SKILL.md
    skill_md = skill_path / "SKILL.md"
    if not skill_md.exists():
        errors.append("Missing SKILL.md file")
        return errors, warnings

    # Read and validate SKILL.md
    content = skill_md.read_text()

    # Check for YAML frontmatter
    if not content.startswith("---"):
        errors.append("SKILL.md missing YAML frontmatter")
    else:
        # Extract frontmatter
        parts = content.split("---", 2)
        if len(parts) < 3:
            errors.append("SKILL.md has malformed YAML frontmatter")
        else:
            try:
                frontmatter = yaml.safe_load(parts[1])

                # Validate required fields
                if "name" not in frontmatter:
                    errors.append("SKILL.md frontmatter missing 'name' field")
                elif not frontmatter["name"]:
                    errors.append("SKILL.md frontmatter 'name' field is empty")

                if "description" not in frontmatter:
                    errors.append("SKILL.md frontmatter missing 'description' field")
                elif not frontmatter["description"]:
                    errors.append("SKILL.md frontmatter 'description' field is empty")
                elif len(frontmatter["description"]) < 75:
                    warnings.append(f"Description is short ({len(frontmatter['description'])} chars). Aim for 75+ for better discoverability.")

            except yaml.YAMLError as e:
                errors.append(f"SKILL.md frontmatter is not valid YAML: {e}")

    # Check for standard directories
    if (skill_path / "scripts").exists():
        scripts = list((skill_path / "scripts").glob("*.py"))
        if scripts:
            warnings.append(f"Found {len(scripts)} script(s) - ensure they are tested and documented")

    if (skill_path / "references").exists():
        refs = list((skill_path / "references").glob("*.md"))
        if not refs:
            warnings.append("references/ directory exists but has no .md files")

    # Check for referenced files
    if "references/" in content:
        # Extract referenced files
        import re
        ref_matches = re.findall(r'references/([a-zA-Z0-9_\-\.]+)', content)
        for ref_file in ref_matches:
            ref_path = skill_path / "references" / ref_file
            if not ref_path.exists():
                errors.append(f"SKILL.md references missing file: references/{ref_file}")

    return errors, warnings


def package_skill(skill_path: Path, output_dir: Path, force: bool = False):
    """Package the skill directory into a .skill file."""

    # Validate first
    errors, warnings = validate_skill_structure(skill_path)

    if errors:
        print("❌ Validation errors found:")
        for error in errors:
            print(f"  - {error}")
        return False

    if warnings:
        print("⚠️  Validation warnings:")
        for warning in warnings:
            print(f"  - {warning}")
        print()

    # Get skill name from directory
    skill_dir_name = skill_path.name
    output_file = output_dir / f"{skill_dir_name}.skill"

    # Check if output file exists
    if output_file.exists() and not force:
        print(f"Error: Output file already exists: {output_file}")
        print("Use --force to overwrite")
        return False

    # Create output directory if it doesn't exist
    output_dir.mkdir(parents=True, exist_ok=True)

    # Create zip file
    print(f"Packaging {skill_path.name}...")

    with zipfile.ZipFile(output_file, 'w', zipfile.ZIP_DEFLATED) as zipf:
        # Walk through skill directory
        for root, dirs, files in os.walk(skill_path):
            # Skip __pycache__ and .git directories
            dirs[:] = [d for d in dirs if d not in ['__pycache__', '.git', '__MACOSX']]

            for file in files:
                # Skip hidden files and .pyc files
                if file.startswith('.') and file != '.gitkeep':
                    continue
                if file.endswith('.pyc'):
                    continue

                file_path = Path(root) / file
                arcname = file_path.relative_to(skill_path)

                print(f"  Adding: {arcname}")
                zipf.write(file_path, arcname)

    print(f"✓ Skill packaged successfully: {output_file}")
    print(f"  Size: {output_file.stat().st_size / 1024:.1f} KB")

    return True


def main():
    parser = argparse.ArgumentParser(
        description="Package a skill directory into a distributable .skill file."
    )
    parser.add_argument(
        "skill_path",
        help="Path to the skill directory"
    )
    parser.add_argument(
        "output_dir",
        help="Output directory for the .skill file"
    )
    parser.add_argument(
        "--force",
        action="store_true",
        help="Overwrite existing .skill file"
    )
    parser.add_argument(
        "--validate-only",
        action="store_true",
        help="Only validate, don't package"
    )

    args = parser.parse_args()

    skill_path = Path(args.skill_path)
    output_dir = Path(args.output_dir)

    if not skill_path.exists():
        print(f"Error: Skill directory does not exist: {skill_path}")
        sys.exit(1)

    if not skill_path.is_dir():
        print(f"Error: Not a directory: {skill_path}")
        sys.exit(1)

    # Validate
    print(f"Validating skill: {skill_path.name}")
    errors, warnings = validate_skill_structure(skill_path)

    if errors:
        print("❌ Validation failed:")
        for error in errors:
            print(f"  - {error}")
        sys.exit(1)

    if warnings:
        print("⚠️  Validation warnings:")
        for warning in warnings:
            print(f"  - {warning}")
        print()

    print("✓ Validation passed")
    print()

    if args.validate_only:
        sys.exit(0)

    # Package
    success = package_skill(skill_path, output_dir, args.force)
    sys.exit(0 if success else 1)


if __name__ == "__main__":
    main()
