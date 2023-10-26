import re
import base64
import os
import sys
from src.debugging.debug_wrapper import echo

@echo
def read_file(file_path):
    try:
        with open(file_path, 'r') as file:
            return file.read(), None
    except Exception as e:
        return None, f"An error occurred while reading the file: {e}"

@echo
def write_file(new_file_path, content):
    try:
        with open(new_file_path, 'w') as file:
            file.write(content)
        return None
    except Exception as e:
        return f"An error occurred while writing to the file: {e}"

@echo
def get_image_paths(content):
    return re.findall(r'\!\[.*?\]\((.*?)\)|\[(.*?)\]\((.*?\.png|.*?\.jpg|.*?\.jpeg|.*?\.gif)\)', content)

@echo
def convert_image_to_base64(image_path):
    try:
        with open(image_path, 'rb') as image_file:
            return base64.b64encode(image_file.read()).decode('utf-8'), None
    except Exception as e:
        return None, f"An error occurred while converting the image: {e}"

@echo
def replace_images_with_base64(content, image_base64_dict):
    for image_path, base64_image in image_base64_dict.items():
        content = content.replace(f'({image_path})', f'(data:image/png;base64,{base64_image})')
    return content

@echo
def b64_conversion(file_path, new_file_path):    
    if not os.path.exists(file_path):
        print("File does not exist.")
        return
    
    content, read_error = read_file(file_path)
    if read_error:
        print(read_error)
        return

    image_paths = get_image_paths(content)
    
    image_base64_dict = {}
    for match in image_paths:
        image_path = match[0] if match[0] else match[2]
        
        if os.path.exists(image_path):
            base64_image, convert_error = convert_image_to_base64(image_path)
            if convert_error:
                print(convert_error)
                return
            image_base64_dict[image_path] = base64_image

    new_content = replace_images_with_base64(content, image_base64_dict)
    
    write_error = write_file(new_file_path, new_content)
    if write_error:
        print(write_error)
        return
