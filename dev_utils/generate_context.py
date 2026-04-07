#!/usr/bin/env python3
"""
Script to generate targeted context files for architectural review.
Uses CLI arguments to isolate specific directories, trees, or file types.
"""

import os
import argparse
from pathlib import Path

# Exclusions: files/dirs starting with . or __, plus venv and uv.lock
EXCLUDED_PREFIXES = ('.', '__')
EXCLUDED_NAMES = {'venv', 'uv.lock', 'node_modules'}

def is_excluded(path: Path, base: Path) -> bool:
    """Check if a path should be excluded based on naming rules."""
    rel_path = path.relative_to(base)
    for part in rel_path.parts:
        if part.startswith(EXCLUDED_PREFIXES) or part in EXCLUDED_NAMES:
            return True
    if path.name == 'uv.lock':
        return True
    return False

def get_file_extension(file_path: Path) -> str:
    return file_path.suffix.lower()

def should_process_file(file_path: Path, args) -> bool:
    """Check if a file should be processed based on requested filters."""
    ext = get_file_extension(file_path)
    
    docs_extensions = {'.md', '.txt'}
    code_extensions = {'.py', '.yaml', '.yml', '.toml', '.base', '.sql'}
    
    # If specific filters are applied
    if args.docs and args.code:
        return ext in docs_extensions or ext in code_extensions
    elif args.docs:
        return ext in docs_extensions
    elif args.code:
        return ext in code_extensions
    else:
        # Default: all allowed extensions
        return ext in docs_extensions.union(code_extensions).union({'.log'})

def read_file_content(file_path: Path) -> str:
    """Read file content. For .log files, only read last 200 lines."""
    try:
        with open(file_path, 'r', encoding='utf-8', errors='replace') as f:
            if get_file_extension(file_path) == '.log':
                lines = f.readlines()
                return ''.join(lines[-200:])
            else:
                return f.read()
    except Exception as e:
        return f"[Error reading file: {e}]"

def generate_directory_tree(base_path: Path, target_path: Path, args, indent: str = '') -> str:
    """Generate a text-based directory tree, respecting exclusions."""
    tree_lines = []
    tree_lines.append(f"{target_path.name}/")
    
    def walk_directory(path: Path, prefix: str):
        try:
            entries = sorted(path.iterdir(), key=lambda x: (x.is_file(), x.name))
            for entry in entries:
                if is_excluded(entry, base_path):
                    continue
                
                if entry.is_dir():
                    tree_lines.append(f"{prefix}├── {entry.name}/")
                    walk_directory(entry, prefix + "│   ")
                else:
                    if should_process_file(entry, args):
                        tree_lines.append(f"{prefix}├── {entry.name}")
        except PermissionError:
            tree_lines.append(f"{prefix}├── [Permission denied]")
            
    walk_directory(target_path, '')
    return '\n'.join(tree_lines)

def collect_files(base_path: Path, target_path: Path, args) -> list:
    """Collect all files that should be processed within the target directory."""
    files = []
    for root, dirs, filenames in os.walk(target_path):
        root_path = Path(root)
        dirs[:] = [d for d in dirs if not is_excluded(root_path / d, base_path)]
        
        for filename in filenames:
            file_path = root_path / filename
            if is_excluded(file_path, base_path):
                continue
            if should_process_file(file_path, args):
                files.append(file_path)
    return sorted(files)

def main():
    parser = argparse.ArgumentParser(description="Generate targeted context for LLM analysis.")
    parser.add_argument('-d', '--dir', type=str, default='.', help="Target directory to parse (e.g., src/cobalt_agent/brain)")
    parser.add_argument('-t', '--tree', action='store_true', help="Output ONLY the directory tree (no file contents)")
    parser.add_argument('--docs', action='store_true', help="Include ONLY documentation files (.md, .txt)")
    parser.add_argument('--code', action='store_true', help="Include ONLY code/config files (.py, .yaml, .toml)")
    parser.add_argument('-o', '--out', type=str, default='cobalt_context.txt', help="Output file name")
    args = parser.parse_args()

    base_path = Path.cwd()
    target_path = (base_path / args.dir).resolve()
    output_file = base_path / args.out

    if not target_path.exists():
        print(f"Error: Target directory {target_path} does not exist.")
        return

    print(f"Targeting: {target_path}")
    print(f"Outputting to: {output_file.name}")
    
    tree_content = generate_directory_tree(base_path, target_path, args)
    
    with open(output_file, 'w', encoding='utf-8') as out_f:
        out_f.write("PROJECT DIRECTORY STRUCTURE\n")
        out_f.write("=" * 80 + "\n\n")
        out_f.write(tree_content + "\n\n")
        
        if not args.tree:
            files = collect_files(base_path, target_path, args)
            print(f"Found {len(files)} files to process.")
            
            for file_path in files:
                rel_path = file_path.relative_to(base_path)
                content = read_file_content(file_path)
                out_f.write(f"\n\n========================================\n")
                out_f.write(f"FILE: {rel_path}\n")
                out_f.write(f"========================================\n\n")
                out_f.write(content)
        else:
            print("Tree-only mode active. Skipping file contents.")

    print(f"Context successfully generated.")

if __name__ == '__main__':
    main()