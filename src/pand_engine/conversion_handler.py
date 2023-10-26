import os
import subprocess
from src.file_ops.html_base_64_handler import b64_conversion
from src.file_ops.dir_and_file_handler import create_target_directory
from src.debugging.debug_wrapper import echo
from src.file_ops.metadata_handler import extract_metadata, process_metadata, generate_pandoc_args, add_title_line_to_md

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
    print(f'{html_file_path} is the html file path')
    return temp_file, html_dir_path, html_file_path

def pdf_setup(file_path):
    base_path = os.getcwd()
    dir_path = os.path.basename(base_path)
    pdf_file = file_path.replace('.md', '.pdf')
    pdf_dir = create_target_directory(pdf_file, 'pdf')
    pdf_dir_path = f"{pdf_dir}{dir_path}"
    pdf_file_path = f"{pdf_dir_path}/{os.path.basename(pdf_file)}"
    if not os.path.exists(pdf_dir_path):
        os.makedirs(pdf_dir_path)
    print(f'{pdf_file_path} is the pdf file path')
    return pdf_file_path

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

def remove_temp_file(temp_file_path):
    os.remove(temp_file_path)

def metadata_setup(file_path):
    title_line = "**Converted by:** _[VinnyVanGogh](https://github.com/VinnyVanGogh/mypand)_\n"
    add_title_line_to_md(file_path, title_line)
    metadata = extract_metadata(file_path)
    metadata_args = generate_pandoc_args(metadata)
    return metadata_args

@echo
def convert_md_to_html(file_path):
    temp_file, html_dir_path, html_file_path = html_setup(file_path)
    metadata_args, temp_file_path = pdf_and_html_setup(file_path)
    command = ["pandoc", temp_file_path, "-o", html_file_path, "--toc", "-s", "--css=/Users/vincevasile/Documents/configs/templates/github-darkmode-markdown.css"] + metadata_args
    subprocess.run(command)
    remove_temp_file(temp_file_path)

    return html_file_path

@echo
def convert_md_to_pdf(file_path):
    pdf_file_path = pdf_setup(file_path)
    metadata_args, temp_file_path = pdf_and_html_setup(file_path)
    command = ["pandoc", temp_file_path, "-o", pdf_file_path, "--toc", "-s", "--pdf-engine=pdflatex"] + metadata_args
    subprocess.run(command)
    remove_temp_file(temp_file_path)
    
    return pdf_file_path

@echo
def convert_md_to_b64_html(file_path):
    temp_file, html_dir_path, html_file_path = html_setup(file_path)
    b64_conversion(file_path, temp_file)
    metadata_args = metadata_setup(file_path)
    process_metadata(temp_file)
    
    pandoc_command = ["pandoc", temp_file, "-o", html_file_path, "--toc", "-s", "--css=/Users/vincevasile/Documents/configs/templates/github-darkmode-markdown.css"] + metadata_args
    subprocess.run(pandoc_command)
    remove_temp_file(temp_file)
    
    return html_file_path
