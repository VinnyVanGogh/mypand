
# This is your src.settings.configuration file for the pandoc conversion script, anything that you want to change should be changed here.
LOG_STEP_COUNTER = 0
LOG_NAME = "ViNmap_debug.log"
LOGGING_DIR = "logging/"


# Pandoc Arguments
PANDOC_HTML_ARGS = "--toc -s -f markdown -t html5 --css='/Users/vincevasile/Documents/src.settings.configs/templates/github-darkmode-markdown.css'" # Change this to your desired HTML arguments by default it uses github darkmode css
PANDOC_PDF_ARGS = "--toc -s -f markdown -t pdf --pdf-engine=pdflatex" # Change this to your desired PDF arguments by default it uses pdflatex


# URL for downloading the custom CSS file
FILE_URL = "https://api.github.com/repos/OzakIOne/markdown-github-dark/contents/github-markdown.css" # Change this to your desired URL by default it uses the github darkmode css

