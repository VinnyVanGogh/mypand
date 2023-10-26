import subprocess
from src.file_ops.html_base_64_handler import b64_conversion
from src.file_ops.dir_and_file_handler import remove_temp_file
from src.debugging.debug_wrapper import echo
from src.file_ops.metadata_handler import process_metadata
from src.pand_engine.setup_handler import html_setup, pdf_setup, pdf_and_html_setup, metadata_setup


@echo
def convert_md_to_html(file_path):
    temp_file, html_dir_path, html_file_path = html_setup(file_path)
    metadata_args, temp_file_path = pdf_and_html_setup(file_path)
    command = ["pandoc", temp_file_path, "-o", html_file_path, "--toc", "-s", "--css=/Users/vincevasile/Documents/configs/templates/github-darkmode-markdown.css"] + metadata_args
    subprocess.run(command)
    remove_temp_file(temp_file_path)
    print(html_file_path)

    return html_file_path

@echo
def convert_md_to_pdf(file_path):
    pdf_file_path = pdf_setup(file_path)
    metadata_args, temp_file_path = pdf_and_html_setup(file_path)
    command = ["pandoc", temp_file_path, "-o", pdf_file_path, "--toc", "-s", "--pdf-engine=pdflatex"] + metadata_args
    subprocess.run(command)
    remove_temp_file(temp_file_path)
    print(pdf_file_path)
    
    return pdf_file_path

@echo
def convert_md_to_b64_html(file_path):
    temp_file, html_dir_path, html_file_path = html_setup(file_path)
    b64_conversion(file_path, temp_file)
    metadata_args = metadata_setup(temp_file)
    process_metadata(temp_file)
    
    pandoc_command = ["pandoc", temp_file, "-o", html_file_path, "--toc", "-s", "--css=/Users/vincevasile/Documents/configs/templates/github-darkmode-markdown.css"] + metadata_args
    subprocess.run(pandoc_command)
    remove_temp_file(temp_file)
    print(html_file_path)
    
    return html_file_path
