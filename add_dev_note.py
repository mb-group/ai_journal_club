#!/usr/bin/env python3
"""
Script to add a development note to all markdown files in the project.
"""

import os
import re
from pathlib import Path

# The note to add
DEV_NOTE = """
```{note}
**This page is incomplete and under active development.** We welcome your suggestions and feedback! Please feel free to contribute or reach out with ideas for improvement.
```

"""

def process_markdown_file(filepath):
    """Add development note to a markdown file if it doesn't already have it."""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Check if the note already exists
        if 'This page is incomplete and under active development' in content:
            print(f"Skipping {filepath} - note already exists")
            return False
        
        # Find the first heading line
        lines = content.split('\n')
        insert_position = 0
        
        # Look for the first heading (line starting with #)
        for i, line in enumerate(lines):
            if line.strip().startswith('#'):
                insert_position = i + 1
                break
        
        # Insert the note after the first heading
        if insert_position > 0:
            lines.insert(insert_position, DEV_NOTE)
            new_content = '\n'.join(lines)
            
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(new_content)
            
            print(f"✓ Added note to {filepath}")
            return True
        else:
            # If no heading found, add at the beginning
            new_content = DEV_NOTE + content
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(new_content)
            print(f"✓ Added note to beginning of {filepath}")
            return True
            
    except Exception as e:
        print(f"✗ Error processing {filepath}: {e}")
        return False

def main():
    """Process all markdown files in the project."""
    base_dir = Path('/research_jude/rgs01_jude/groups/babugrp/projects/tian_ai/babugrp/ai_journal_club')
    
    # Find all markdown files
    md_files = list(base_dir.rglob('*.md'))
    
    print(f"Found {len(md_files)} markdown files")
    print("=" * 80)
    
    processed = 0
    skipped = 0
    
    for md_file in sorted(md_files):
        if process_markdown_file(md_file):
            processed += 1
        else:
            skipped += 1
    
    print("=" * 80)
    print(f"Processed: {processed} files")
    print(f"Skipped: {skipped} files")
    print(f"Total: {len(md_files)} files")

if __name__ == '__main__':
    main()
