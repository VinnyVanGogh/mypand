import os
from src.debugging.debug_wrapper import echo

@echo
def create_target_directory(file_path, dir_type=None):
    root_dir = os.path.expanduser("/Users/vincevasile")
    base_dir = os.path.dirname(file_path)
    pdf_dir = f"{root_dir}/documents/pdf/{base_dir}"
    html_dir = f"{root_dir}/documents/html/{base_dir}"
    
    if dir_type == 'html':
        if not os.path.exists(html_dir):
            os.makedirs(html_dir)
        return html_dir
    elif dir_type == 'pdf':
        if not os.path.exists(pdf_dir):
            os.makedirs(pdf_dir)
        return pdf_dir
    else:
        print("Invalid directory type.")

@echo
def get_file_name(file_path):
    return os.path.basename(file_path).replace('.md', '')

@echo
def format_name_with_spaces(file_path):
    base_name = get_file_name(file_path)
    return base_name.replace('_', ' ').title()
    
@echo
def get_file_path(file_path):
    return os.path.dirname(file_path)
