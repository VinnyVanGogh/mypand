import os
import subprocess
from src.file_ops.metadata_handler import format_name, extract_metadata, process_metadata, generate_metadata_args, metadata_args
from dir_handler import create_target_directory

RED = '\033[0;31m'

def debug_echo(message):
    print(f"{RED}{message}")

def combine_args(*args):
    last_index = len(args)
    joined_args = ""
    for i, arg in enumerate(args, 1):
        if i == last_index:
            if last_index > 1:
                joined_args += "and "
            joined_args += arg
        else:
            joined_args += f"{arg}, "
    return joined_args

def convert_md_to_html(arg, target, metadata_args, pandoc_html_args):
    md_filename = os.path.basename(arg)
    
    # Assuming generate_metadata_args and process_metadata are as previously defined
    generate_metadata_args()
    process_metadata(arg)
    
    command = ["pandoc"] + metadata_args + pandoc_html_args + ["-o", target]
    subprocess.run(command)

def convert_md_to_pdf(arg, target, metadata_args, pandoc_pdf_args):
    
    # Assuming generate_metadata_args and process_metadata are as previously defined
    generate_metadata_args()
    process_metadata(arg)
    
    command = ["pandoc"] + metadata_args + pandoc_pdf_args + ["-o", target]
    subprocess.run(command)

def prepare_conversion(arg, html_directory, pdf_directory):
    full_path = os.path.abspath(arg)
    dir_name = os.path.dirname(full_path)
    last_folder = os.path.basename(dir_name)
    
    # Assuming format_name, extract_metadata, and create_target_directory are as previously defined
    format_name(arg)
    extract_metadata(arg)
    create_target_directory(html_directory, last_folder, pdf_directory)

def github_html(args, html_directory):
    for arg in args:
        prepare_conversion(arg, html_directory, None)
        target = os.path.join(html_directory, last_folder, f"{base_name}.html")
        convert_md_to_html(arg, target, metadata_args, PANDOC_HTML_ARGS)

def pdf(args, pdf_directory):
    for arg in args:
        prepare_conversion(arg, None, pdf_directory)
        target = os.path.join(pdf_directory, last_folder, f"{base_name}.pdf")
        convert_md_to_pdf(arg, target, metadata_args, PANDOC_PDF_ARGS)

if __name__ == "__main__":
    PANDOC_HTML_ARGS = []  # Define your HTML-specific pandoc args here
    PANDOC_PDF_ARGS = []  # Define your PDF-specific pandoc args here
    
    # Example usage
    html_directory = "path/to/html_directory"
    pdf_directory = "path/to/pdf_directory"
    files = ["file1.md", "file2.md"]
    
    github_html(files, html_directory)
    pdf(files, pdf_directory)
