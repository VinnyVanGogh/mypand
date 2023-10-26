import os
from src.debugging.debug_wrapper import echo
from src.file_ops.dir_and_file_handler import create_target_directory
from src.file_ops.metadata_handler import process_metadata, extract_metadata, generate_pandoc_args, add_title_line_to_md

@echo
def html_setup(file_path):
    base_path = os.getcwd()
    dir_path = os.path.basename(base_path)
    html_file = file_path.replace('.md', '.html')
    temp_file = "temp_base64.md"
    html_dir = create_target_directory(html_file, 'html')
    html_dir_path = f"{html_dir}{dir_path}"
    html_file_path = f"{html_dir_path}/{os.path.basename(html_file)}"
    if not os.path.exists(html_dir_path):
        os.makedirs(html_dir_path)
    return temp_file, html_dir_path, html_file_path

@echo
def pdf_setup(file_path):
    base_path = os.getcwd()
    dir_path = os.path.basename(base_path)
    pdf_file = file_path.replace('.md', '.pdf')
    pdf_dir = create_target_directory(pdf_file, 'pdf')
    pdf_dir_path = f"{pdf_dir}{dir_path}"
    pdf_file_path = f"{pdf_dir_path}/{os.path.basename(pdf_file)}"
    if not os.path.exists(pdf_dir_path):
        os.makedirs(pdf_dir_path)
    return pdf_file_path

@echo
def metadata_setup(file_path):
    title_line = "**Converted by:** _[VinnyVanGogh](https://github.com/VinnyVanGogh/mypand)_\n"
    add_title_line_to_md(file_path, title_line)
    metadata = extract_metadata(file_path)
    metadata_args = generate_pandoc_args(metadata)
    return metadata_args

@echo
def pdf_and_html_setup(file_path):
    metadata_args = metadata_setup(file_path)
    lines = []
    with open(file_path, 'r') as file:
        for line in file:
            lines.append(line)
    temp_file_path = "temp_file.md"
    with open(temp_file_path, 'w') as temp_file:
        temp_file.writelines(lines)
    
    process_metadata(temp_file_path)
    return metadata_args, temp_file_path

