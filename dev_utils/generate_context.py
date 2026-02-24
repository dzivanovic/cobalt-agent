#!/usr/bin/env python3
"""
Script to generate a master context file for architectural review.
Generates cobalt_master_context.txt with directory tree and file contents.
"""

import os
from pathlib import Path

# Exclusions: files/dirs starting with . or __, plus venv and uv.lock
EXCLUDED_PREFIXES = ('.', '__')
EXCLUDED_NAMES = {'venv', 'uv.lock'}

# Inclusions: allowed file extensions
ALLOWED_EXTENSIONS = {'.py', '.md', '.yaml', '.yml', '.toml', '.log', '.txt', '.base'}


def is_excluded(path: Path, base: Path) -> bool:
    """Check if a path should be excluded based on naming rules."""
    rel_path = path.relative_to(base)
    
    # Check each component of the path
    for part in rel_path.parts:
        if part.startswith(EXCLUDED_PREFIXES) or part in EXCLUDED_NAMES:
            return True
    
    # Check for uv.lock file specifically
    if path.name == 'uv.lock':
        return True
    
    return False


def get_file_extension(file_path: Path) -> str:
    """Get the file extension."""
    return file_path.suffix.lower()


def should_process_file(file_path: Path) -> bool:
    """Check if a file should be processed based on its extension."""
    return get_file_extension(file_path) in ALLOWED_EXTENSIONS


def read_file_content(file_path: Path) -> str:
    """Read file content. For .log files, only read last 200 lines."""
    try:
        with open(file_path, 'r', encoding='utf-8', errors='replace') as f:
            if get_file_extension(file_path) == '.log':
                # For log files, only read last 200 lines
                lines = f.readlines()
                return ''.join(lines[-200:])
            else:
                return f.read()
    except Exception as e:
        return f"[Error reading file: {e}]"


def generate_directory_tree(base_path: Path, indent: str = '') -> str:
    """Generate a text-based directory tree, respecting exclusions."""
    tree_lines = []
    tree_lines.append(f"{base_path.name}/")
    
    def walk_directory(path: Path, prefix: str):
        try:
            # Get all entries, sorted
            entries = sorted(path.iterdir(), key=lambda x: (x.is_file(), x.name))
            
            for entry in entries:
                rel_path = entry.relative_to(base_path)
                
                # Skip excluded paths
                if is_excluded(entry, base_path):
                    continue
                
                if entry.is_dir():
                    tree_lines.append(f"{prefix}{entry.name}/")
                    walk_directory(entry, prefix + "    ")
                else:
                    # Check if file should be processed
                    if should_process_file(entry):
                        tree_lines.append(f"{prefix}{entry.name}")
        except PermissionError:
            tree_lines.append(f"{prefix}[Permission denied]")
    
    walk_directory(base_path, '')
    return '\n'.join(tree_lines)


def collect_files(base_path: Path) -> list:
    """Collect all files that should be processed."""
    files = []
    
    for root, dirs, filenames in os.walk(base_path):
        root_path = Path(root)
        
        # Filter out excluded directories
        dirs[:] = [d for d in dirs if not is_excluded(root_path / d, base_path)]
        
        for filename in filenames:
            file_path = root_path / filename
            
            # Skip excluded paths
            if is_excluded(file_path, base_path):
                continue
            
            # Check if file should be processed
            if should_process_file(file_path):
                files.append(file_path)
    
    return sorted(files)


def main():
    base_path = Path.cwd()
    output_file = base_path / 'cobalt_master_context.txt'
    
    print(f"Generating context file for: {base_path}")
    
    # Generate directory tree
    print("Generating directory tree...")
    tree_content = generate_directory_tree(base_path)
    
    # Collect files to process
    print("Collecting files...")
    files = collect_files(base_path)
    print(f"Found {len(files)} files to process")
    
    # Write to output file
    print(f"Writing to {output_file}...")
    with open(output_file, 'w', encoding='utf-8') as out_f:
        # Write directory tree as first section
        out_f.write("PROJECT DIRECTORY STRUCTURE\n")
        out_f.write("=" * 80 + "\n\n")
        out_f.write(tree_content)
        
        # Process each file
        for file_path in files:
            rel_path = file_path.relative_to(base_path)
            print(f"Processing: {rel_path}")
            
            content = read_file_content(file_path)
            
            out_f.write(f"\n\n========================================\n")
            out_f.write(f"FILE: {rel_path}\n")
            out_f.write(f"========================================\n\n")
            out_f.write(content)
    
    print(f"\nContext file generated: {output_file}")
    print(f"Total files processed: {len(files)}")


if __name__ == '__main__':
    main()