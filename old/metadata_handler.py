import re
import os
from collections import defaultdict
from dir_handler import create_target_directory
from src.settings.config import DEFAULT_TITLE, DEFAULT_AUTHOR, DEFAULT_KEYWORDS, DEFAULT_SUBTITLE, DEFAULT_DESCRIPTION, DEFAULT_LANGUAGE, DEFAULT_DATE

# Global variable to store metadata
metadata = defaultdict(str)

def format_name(file_path):
    base_name = os.path.basename(file_path).replace('.md', '')
    name_with_spaces = base_name.replace('_', ' ')
    return name_with_spaces.title()

def extract_metadata(file_path):
    global metadata
    with open(file_path, 'r') as file:
        lines = file.readlines()
    
    for line in lines:
        match = re.match(r'^# ([a-zA-Z]*):(.+)$', line.strip())
        if match:
            key = match.group(1).strip()
            value = match.group(2).strip()
            metadata[key] = value
    
    # Fallback to defaults if not set
    metadata["Title"] = metadata.get("Title", DEFAULT_TITLE)
    metadata["Author"] = metadata.get("Author", DEFAULT_AUTHOR)
    metadata["Keywords"] = metadata.get("Keywords", DEFAULT_KEYWORDS)
    metadata["Subtitle"] = metadata.get("Subtitle", DEFAULT_SUBTITLE)
    metadata["Description"] = metadata.get("Description", DEFAULT_DESCRIPTION)
    metadata["Language"] = metadata.get("Language", DEFAULT_LANGUAGE)
    metadata["Date"] = metadata.get("Date", DEFAULT_DATE)


def process_metadata(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
    
    new_lines = [line for line in lines if not re.match(r'^# (Subtitle|Author|Keywords|Title|Description|Date|Language):', line)]
    
    with open(file_path, 'w') as file:
        file.writelines(new_lines)

def generate_metadata_args():
    global metadata
    metadata_args = {
        "date": metadata["Date"],
        "subtitle": metadata["Subtitle"],
        "keywords": metadata["Keywords"],
        "title": metadata["Title"],
        "description": metadata["Description"],
        "lang": metadata["Language"]
    }
    return metadata_args

if __name__ == "__main__":
    file_path = 'your_file.md'
    DEFAULT_TITLE = format_name(file_path)
    extract_metadata(file_path)
    create_target_directory('html_directory', 'last_folder', 'pdf_directory')
    process_metadata(file_path)
    metadata_args = generate_metadata_args()
    print(metadata_args)
