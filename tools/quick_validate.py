#!/usr/bin/env python3
"""
Quick Skill Validation Script
Validates skill structure and content without packaging.
"""

import sys
import argparse
import yaml
import re
from pathlib import Path
from typing import List, Tuple


class SkillValidator:
    """Validates Claude Code skill structure and content."""

    def __init__(self, skill_path: Path):
        self.skill_path = skill_path
        self.errors = []
        self.warnings = []
        self.info = []

    def validate_all(self) -> Tuple[List[str], List[str], List[str]]:
        """Run all validation checks."""
        self.validate_structure()
        self.validate_skill_md()
        self.validate_scripts()
        self.validate_references()
        self.validate_naming()

        return self.errors, self.warnings, self.info

    def validate_structure(self):
        """Check that basic directory structure exists."""
        if not self.skill_path.exists():
            self.errors.append(f"Skill directory does not exist: {self.skill_path}")
            return

        if not self.skill_path.is_dir():
            self.errors.append(f"Not a directory: {self.skill_path}")
            return

        # Check for SKILL.md
        if not (self.skill_path / "SKILL.md").exists():
            self.errors.append("Missing SKILL.md file")

        # Check for standard directories (optional but recommended)
        for dir_name in ["scripts", "references", "assets"]:
            dir_path = self.skill_path / dir_name
            if dir_path.exists():
                self.info.append(f"✓ Has {dir_name}/ directory")
            else:
                self.warnings.append(f"Missing {dir_name}/ directory (optional but recommended)")

    def validate_skill_md(self):
        """Validate SKILL.md content and structure."""
        skill_md = self.skill_path / "SKILL.md"
        if not skill_md.exists():
            return  # Already reported in validate_structure

        content = skill_md.read_text()
        line_count = len(content.splitlines())

        # Check line count
        if line_count > 500:
            self.warnings.append(f"SKILL.md is long ({line_count} lines). Consider moving details to references/")
        else:
            self.info.append(f"✓ SKILL.md length is good ({line_count} lines)")

        # Validate YAML frontmatter
        if not content.startswith("---"):
            self.errors.append("SKILL.md missing YAML frontmatter (must start with '---')")
            return

        parts = content.split("---", 2)
        if len(parts) < 3:
            self.errors.append("SKILL.md has malformed YAML frontmatter")
            return

        # Parse frontmatter
        try:
            frontmatter = yaml.safe_load(parts[1])

            # Validate name field
            if "name" not in frontmatter:
                self.errors.append("Missing 'name' in frontmatter")
            elif not frontmatter["name"]:
                self.errors.append("'name' field is empty")
            elif not isinstance(frontmatter["name"], str):
                self.errors.append("'name' field must be a string")
            else:
                name = frontmatter["name"]
                # Check naming convention
                if not re.match(r'^[a-z0-9\-]+$', name):
                    self.warnings.append(f"Skill name '{name}' should be lowercase with hyphens only")
                self.info.append(f"✓ Skill name: {name}")

            # Validate description field
            if "description" not in frontmatter:
                self.errors.append("Missing 'description' in frontmatter")
            elif not frontmatter["description"]:
                self.errors.append("'description' field is empty")
            elif not isinstance(frontmatter["description"], str):
                self.errors.append("'description' field must be a string")
            else:
                desc = frontmatter["description"]
                desc_len = len(desc)
                if desc_len < 75:
                    self.warnings.append(f"Description is short ({desc_len} chars). Aim for 75+ chars for better discoverability")
                else:
                    self.info.append(f"✓ Description length: {desc_len} chars")

                # Check for generic descriptions
                generic_phrases = ["this skill", "helps with", "allows you to"]
                if any(phrase in desc.lower() for phrase in generic_phrases):
                    self.warnings.append("Description may be too generic. Be specific about triggers and use cases")

        except yaml.YAMLError as e:
            self.errors.append(f"SKILL.md frontmatter is not valid YAML: {e}")
            return

        # Check for required sections
        body = parts[2]
        required_sections = ["## Overview", "## When to Use This Skill"]
        recommended_sections = ["## Core Workflows", "## Prerequisites"]

        for section in required_sections:
            if section not in body:
                self.errors.append(f"Missing required section: {section}")
            else:
                self.info.append(f"✓ Has {section}")

        for section in recommended_sections:
            if section not in body:
                self.warnings.append(f"Missing recommended section: {section}")
            else:
                self.info.append(f"✓ Has {section}")

        # Check for referenced files
        ref_matches = re.findall(r'references/([a-zA-Z0-9_\-\.]+)', body)
        if ref_matches:
            for ref_file in set(ref_matches):
                ref_path = self.skill_path / "references" / ref_file
                if not ref_path.exists():
                    self.errors.append(f"Referenced file does not exist: references/{ref_file}")
                else:
                    self.info.append(f"✓ Referenced file exists: references/{ref_file}")

    def validate_scripts(self):
        """Validate scripts directory."""
        scripts_dir = self.skill_path / "scripts"
        if not scripts_dir.exists():
            return

        scripts = list(scripts_dir.glob("*.py")) + list(scripts_dir.glob("*.sh"))

        if not scripts:
            self.info.append("ℹ️  scripts/ directory is empty")
            return

        for script in scripts:
            # Check if executable (on Unix systems)
            if script.suffix == ".sh":
                if not os.access(script, os.X_OK):
                    self.warnings.append(f"Script {script.name} is not executable")

            # Check if script is documented in SKILL.md
            skill_md = self.skill_path / "SKILL.md"
            if skill_md.exists():
                content = skill_md.read_text()
                if script.name not in content:
                    self.warnings.append(f"Script {script.name} is not mentioned in SKILL.md")

            self.info.append(f"✓ Found script: {script.name}")

    def validate_references(self):
        """Validate references directory."""
        refs_dir = self.skill_path / "references"
        if not refs_dir.exists():
            return

        ref_files = list(refs_dir.glob("*.md"))

        if not ref_files:
            self.warnings.append("references/ directory exists but has no .md files")
            return

        # Check if references are mentioned in SKILL.md
        skill_md = self.skill_path / "SKILL.md"
        if skill_md.exists():
            skill_content = skill_md.read_text()

            for ref_file in ref_files:
                if ref_file.name == ".gitkeep":
                    continue

                if f"references/{ref_file.name}" not in skill_content:
                    self.warnings.append(f"Reference file {ref_file.name} is not mentioned in SKILL.md")
                else:
                    self.info.append(f"✓ Reference {ref_file.name} is mentioned in SKILL.md")

    def validate_naming(self):
        """Validate skill directory naming convention."""
        dir_name = self.skill_path.name

        # Check for number prefix
        if not re.match(r'^\d{2}_', dir_name):
            self.warnings.append(f"Directory name '{dir_name}' should start with a two-digit number (e.g., '00_', '01_')")

        # Check for lowercase with hyphens
        skill_name_part = dir_name[3:] if re.match(r'^\d{2}_', dir_name) else dir_name
        if not re.match(r'^[a-z0-9\-]+$', skill_name_part):
            self.warnings.append(f"Skill name '{skill_name_part}' should be lowercase with hyphens only")


def main():
    parser = argparse.ArgumentParser(
        description="Quickly validate a Claude Code skill structure and content."
    )
    parser.add_argument(
        "skill_path",
        help="Path to the skill directory"
    )
    parser.add_argument(
        "--strict",
        action="store_true",
        help="Treat warnings as errors"
    )
    parser.add_argument(
        "--quiet",
        action="store_true",
        help="Only show errors and warnings"
    )

    args = parser.parse_args()

    skill_path = Path(args.skill_path)

    print(f"Validating skill: {skill_path}")
    print("=" * 60)
    print()

    validator = SkillValidator(skill_path)
    errors, warnings, info = validator.validate_all()

    # Display results
    if errors:
        print("❌ ERRORS:")
        for error in errors:
            print(f"  • {error}")
        print()

    if warnings:
        print("⚠️  WARNINGS:")
        for warning in warnings:
            print(f"  • {warning}")
        print()

    if info and not args.quiet:
        print("ℹ️  INFO:")
        for item in info:
            print(f"  {item}")
        print()

    # Summary
    print("=" * 60)
    if errors:
        print(f"❌ Validation FAILED: {len(errors)} error(s), {len(warnings)} warning(s)")
        sys.exit(1)
    elif warnings and args.strict:
        print(f"⚠️  Validation FAILED (strict mode): {len(warnings)} warning(s)")
        sys.exit(1)
    elif warnings:
        print(f"⚠️  Validation passed with warnings: {len(warnings)} warning(s)")
        sys.exit(0)
    else:
        print("✓ Validation PASSED")
        sys.exit(0)


if __name__ == "__main__":
    main()
