import sys
import argparse
from src.pand_engine.conversion_handler import convert_md_to_html, convert_md_to_pdf, convert_md_to_b64_html
from src.debugging.debug_wrapper import echo

@echo
def args_for_parser():
    parser = argparse.ArgumentParser(description='Convert markdown to html or pdf.')
    parser.add_argument('file_path', type=str, help='Path to markdown file.')
    parser.add_argument('-gh', '--github', action='store_true', help='Convert to html with github darkmode css.')
    parser.add_argument('-b', '--base64', action='store_true', help='Convert images to base64.')
    parser.add_argument('-p', '--pdf', action='store_true', help='Convert to pdf instead of html.')
    return parser.parse_args()

@echo
def mypand(file_path):
    args = args_for_parser()

    if args.github and args.base64:
        print("Both -gh and -b are provided. Prioritizing -b.")
        convert_md_to_b64_html(file_path)
        return

    if args.pdf:
        if args.github:
            print("Converting to HTML with GitHub style, then to PDF.")
            convert_md_to_html(file_path)
            convert_md_to_pdf(file_path)
            return
        if args.base64:
            print("Converting to HTML with Base64 images, then to PDF.")
            convert_md_to_b64_html(file_path)
            convert_md_to_pdf(file_path)
            return
        print("Converting to PDF.")
        convert_md_to_pdf(file_path)
        return

    if args.github:
        print("Converting to HTML with GitHub style.")
        convert_md_to_html(file_path)
        return

    if args.base64:
        print("Converting to HTML with Base64 images.")
        convert_md_to_b64_html(file_path)
        return

    print(f"Please specify a conversion type. You entered: {args}")

        
if __name__ == "__main__":
    args = args_for_parser()
    mypand(file_path=args.file_path)