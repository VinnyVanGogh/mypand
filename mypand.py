import sys
import argparse
from src.pand_engine.conversion_handler import convert_md_to_html, convert_md_to_pdf, convert_md_to_b64_html
from src.debugging.debug_wrapper import echo

@echo
def args_for_parser():
    parser = argparse.ArgumentParser(description='Convert markdown to html or pdf.')
    parser.add_argument('file_path', metavar='file_path', type=str, nargs=1, help='The path to the markdown file to be converted.')
    parser.add_argument('-gh', '--github', action='store_true', help='Convert to html with github darkmode css.')
    parser.add_argument('-b', '--base64', action='store_true', help='Convert images to base64.')
    parser.add_argument('-p', '--pdf', action='store_true', help='Convert to pdf instead of html.')
    return parser.parse_args()

@echo
def mypand(file_path):
    args = args_for_parser()
    if args.github and args.pdf:
        print("Invalid arguments.")
        return
    if args.github and args.base64:
        convert_md_to_b64_html(file_path)
        return
    if args.github:
        convert_md_to_html(file_path)
        return
    if args.pdf:
        convert_md_to_pdf(file_path)
        return
    if args.base64:
        convert_md_to_b64_html(file_path)
        return
    else:
        print(f"Please specify a conversion type. you entered: {args}")
        
if __name__ == "__main__":
    mypand(sys.argv[1])