# app/blueprints/smart_editor/utils.py
import difflib
import os

def generate_diff(original, modified):
    original_lines = original.splitlines(keepends=True)
    modified_lines = modified.splitlines(keepends=True)
    diff = difflib.unified_diff(original_lines, modified_lines, lineterm='')
    return ''.join(diff)

def apply_diff(original, diff):
    from io import StringIO
    from patch_ng import fromstring

    patch = fromstring(diff)
    patched = patch.apply(original.splitlines(True))
    return ''.join(patched)

def list_editable_files(base_dir):
    editable_files = []
    for root, _, files in os.walk(base_dir):
        for file in files:
            if file.endswith(('.html', '.css', '.js', '.liquid')):
                editable_files.append(os.path.join(root, file))
    return editable_files
