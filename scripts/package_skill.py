#!/usr/bin/env python3
"""
Package a skill for distribution or deployment
"""
import os
import sys
import zipfile
from pathlib import Path

def package_skill(skill_dir, output_path="."):
    """Create a distributable package of a skill"""
    skill_path = Path("skills") / skill_dir

    if not skill_path.exists():
        print(f"❌ Error: Skill directory '{skill_path}' not found")
        sys.exit(1)

    # Create zip file
    output_file = Path(output_path) / f"{skill_dir}.zip"

    with zipfile.ZipFile(output_file, 'w', zipfile.ZIP_DEFLATED) as zipf:
        for root, dirs, files in os.walk(skill_path):
            for file in files:
                file_path = Path(root) / file
                arcname = file_path.relative_to(skill_path.parent)
                zipf.write(file_path, arcname)
                print(f"✓ Added: {arcname}")

    print(f"\n✅ Packaged: {output_file}")
    print(f"📦 Size: {output_file.stat().st_size / 1024:.2f} KB")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python package_skill.py <skill-directory-name>")
        print("Example: python package_skill.py 00-foundation-prime")
        sys.exit(1)

    skill_dir = sys.argv[1]
    package_skill(skill_dir)
