#!/usr/bin/env python3
"""
Fix assets issue by copying assets directory to build output
"""

import shutil
import os
from pathlib import Path

# Get the directory paths
repo_root = Path(__file__).parent
assets_src = repo_root / "assets"
build_assets_dst = repo_root / "_build" / "html" / "assets"

print(f"Copying assets from {assets_src} to {build_assets_dst}")

# Create the destination directory if it doesn't exist
build_assets_dst.parent.mkdir(parents=True, exist_ok=True)

# Copy the assets directory
if assets_src.exists():
    if build_assets_dst.exists():
        shutil.rmtree(build_assets_dst)
    shutil.copytree(assets_src, build_assets_dst)
    print("Assets copied successfully!")
else:
    print(f"Source assets directory {assets_src} not found!")

# List the contents to verify
if build_assets_dst.exists():
    print("Assets in build directory:")
    for item in build_assets_dst.iterdir():
        print(f"  - {item.name}")