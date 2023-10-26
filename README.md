# mypand

## Table of Contents

- [Prerequisites](#prerequisites)
- [Description](#description)
- [Installation and Setup](#installation-and-setup)
  - [Requirements.txt](#requirements.txt)
  - [Virtual Environment](#virtual-environment)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## Prerequisites

- [Python 3.8 or higher](https://www.python.org/downloads/)
- [Pandoc](https://pandoc.org/installing.html)

## Description

A pandoc wrapper for converting markdown files to html and pdf files. Adds github css, allows for b64 encoding of html, and allows for pdf conversion. Makes sharing markdown files easier.
Stay tuned for more features.

- The only requirements are Python 3.8 and Pandoc.

## Installation and Setup

1. Clone the repository

```shell
git clone https://github.com/VinnyVanGogh/mypand.git
```

2. CD into the directory

```shell
cd mypand
```

3. Run the project:
- -b for b64 encoded html, -g for github html, and -p for pdf
  - All converted from markdown files through pandoc

```shell
python3 <-b -g or -p> </path/to/file.md>
```

## Usage

**A pretty simple shell application that allows you to convert markdown files to html and pdf files.**

- There are three ways to run the project:
  - -b for b64 encoded html, -g for github html, and -p for pdf
    - All converted from markdown files through pandoc

### Markdown to Base64 Encoded HTML
- Run the project, specifying base64 encoded images, and html with github darkmode css(You will not have to upload your files, the html is completely self contained):

```shell
python3 -b </path/to/file.md>
```

### Markdown to Github HTML
- Run the project, specifying html with github darkmode css (you will have to upload your images with your html and make sure they are in the same dir structure as your markdown file):

```shell
python3 -g </path/to/file.md>
```

### Markdown to PDF
- Run the project, specifying pdf(You will not have to upload your files, the pdf is completely self contained however the output is not as clean as the html, and pandoc does some funky things with moving images around in pdfs...):

```shell
python3 -p </path/to/file.md>
```

## Contributing

We welcome contributions to improve mypand. To contribute, follow these steps:

1. Fork this repository.

2. Create a branch for your changes:

```shell
git checkout -b '<branch_name>'
```

3. Make your changes and commit them: 

```shell
git commit -m 'Your commit message'
```

4. After you have committed your changes, push to the original branch:

```shell
git push origin <branch_name>
```

5. Create a pull request on the original repository and describe your changes.

## License

This project is licensed under the [MIT License](LICENSE). You can find the full text of the license in the [LICENSE](LICENSE) file.