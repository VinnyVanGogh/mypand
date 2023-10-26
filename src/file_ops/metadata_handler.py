import re
from datetime import datetime
import getpass
from src.file_ops.dir_and_file_handler import format_name_with_spaces
from src.debugging.debug_wrapper import echo
import locale

@echo
def get_default_metadata(file_path, format_name_with_spaces):
    """
    Get default metadata values.
    """
    default_metadata = {
        "title": format_name_with_spaces(file_path),
        "author": getpass.getuser(),
        "keywords": "document, auto-generated, pandoc, pip, python, markdown, md, html, pdf, vince, github, darkmode, css, vinnyvangogh",
        "subtitle": "This is an auto-converted document, from markdown.",
        "description": "This is an auto-generated document.",
        "lang": locale.getdefaultlocale()[0],
        "date": datetime.now().strftime("%Y-%m-%d")
    }
    return default_metadata


@echo
def extract_metadata(file_path):
    metadata = get_default_metadata(file_path, format_name_with_spaces)

    with open(file_path, 'r') as file:
        lines = file.readlines()

    for line in lines:
        match = re.match(r'^#\s*([a-zA-Z]+)\s*:\s*(.+)\s*$', line.strip())
        if match:
            key = match.group(1).strip().lower()
            value = match.group(2).strip()
            metadata[key] = value

    return metadata

    
@echo
def process_metadata(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
    
    new_lines = [line for line in lines if not re.match(r'^# (Subtitle|Author|Keywords|Title|Description|Date|Language):', line)]
    
    with open(file_path, 'w') as file:
        file.writelines(new_lines)
     
@echo   
def generate_metadata_args(metadata):
    args = []
    for key, value in metadata.items():
        args.append(f'--{key.lower()}')
        args.append(value)
    return args

@echo
def generate_pandoc_args(metadata):
    args = []
    for key, value in metadata.items():
        args.append(f"--metadata={key}={value}")
    return args

@echo
def add_title_line_to_md(file_path, title_line):
    with open(file_path, 'r') as file:
        lines = file.readlines()

    if title_line not in lines:
        lines.insert(0, f"{title_line}\n")

        with open(file_path, 'w') as file:
            file.writelines(lines)
