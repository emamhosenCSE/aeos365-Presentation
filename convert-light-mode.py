#!/usr/bin/env python3
"""Convert aeos365 presentation to light mode."""

import os
import glob
import re

slides_dir = r'd:\laragon\www\aeos365 Presentation\slides'

# Define replacement patterns - these are applied in order
replacements = [
    # Primary background colors
    (r'background-color:\s*#0f172a;', 'background-color: #ffffff;'),
    (r'background:\s*#0f172a;', 'background: #ffffff;'),
    (r'background-color:\s*#1e293b;', 'background-color: #ffffff;'),
    (r'background:\s*#1e293b;', 'background: #ffffff;'),
    (r'background-color:\s*#1a1a1a;', 'background-color: #ffffff;'),
    (r'background:\s*#1a1a1a;', 'background: #ffffff;'),
    (r'background-color:\s*#000000;', 'background-color: #ffffff;'),
    
    # Text colors - dark text
    (r'color:\s*#ffffff;', 'color: #0f172a;'),
    (r'color:\s*white;', 'color: #0f172a;'),
    (r'color:\s*#f1f5f9;', 'color: #0f172a;'),
    (r'color:\s*#e2e8f0;', 'color: #0f172a;'),
    (r'color:\s*#cbd5e1;', 'color: #374151;'),
    (r'color:\s*#94a3b8;', 'color: #64748b;'),
    
    # Dark background with opacity - convert to light
    (r'background-color:\s*rgba\(\s*30,\s*41,\s*59,\s*0\.4\);', 'background-color: #f3f4f6;'),
    (r'background-color:\s*rgba\(\s*30,\s*41,\s*59,\s*0\.3\);', 'background-color: #f3f4f6;'),
    (r'background-color:\s*rgba\(\s*30,\s*41,\s*59,\s*0\.5\);', 'background-color: #f3f4f6;'),
    (r'background-color:\s*rgba\(\s*30,\s*41,\s*59,\s*0\.6\);', 'background-color: #e2e8f0;'),
    (r'background-color:\s*rgba\(\s*15,\s*23,\s*42,\s*0\.6\);', 'background-color: #e2e8f0;'),
    
    # Light borders
    (r'border:\s*1px\s*solid\s*rgba\(\s*148,\s*163,\s*184,\s*0\.2\);', 'border: 1px solid #d1d5db;'),
    (r'border:\s*1px\s*solid\s*rgba\(\s*148,\s*163,\s*184,\s*0\.1\);', 'border: 1px solid #e2e8f0;'),
    (r'border:\s*1px\s*solid\s*rgba\(\s*0,\s*0,\s*0,\s*0\.1\);', 'border: 1px solid #e2e8f0;'),
    (r'border-color:\s*rgba\(\s*148,\s*163,\s*184,\s*0\.2\);', 'border-color: #d1d5db;'),
    
    # Geo accents and low opacity dark colors
    (r'background-color:\s*rgba\(\s*0,\s*0,\s*0,\s*0\.05\);', 'background-color: transparent;'),
    (r'background-color:\s*rgba\(\s*0,\s*0,\s*0,\s*0\.1\);', 'background-color: #f8fafc;'),
]

def process_files():
    """Process all HTML files in slides directory."""
    files = glob.glob(os.path.join(slides_dir, '*.html'))
    updated_count = 0
    
    for file_path in files:
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            original_content = content
            
            # Apply all replacements using regex
            for pattern, replacement in replacements:
                content = re.sub(pattern, replacement, content, flags=re.IGNORECASE)
            
            # Only write if changed
            if content != original_content:
                with open(file_path, 'w', encoding='utf-8') as f:
                    f.write(content)
                updated_count += 1
                filename = os.path.basename(file_path)
                print(f'✓ Updated {filename}')
        
        except Exception as e:
            print(f'✗ Error processing {file_path}: {e}')
    
    print(f'\n✅ Light mode conversion complete: {updated_count} files updated')

if __name__ == '__main__':
    process_files()
