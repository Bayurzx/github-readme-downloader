import os
import markdown2
from bs4 import BeautifulSoup


def markdown_to_plain_text(markdown_content):
    # Convert Markdown to HTML
    html_content = markdown2.markdown(markdown_content)

    # Use an HTML parser to extract plain text from HTML
    soup = BeautifulSoup(html_content, 'html.parser')

    # Get the plain text
    plain_text = soup.get_text()

    return plain_text


def convert_markdown_files_to_plain_text():
    # Get a list of Markdown files in the current directory
    markdown_files = [file for file in os.listdir() if file.endswith(".md")]

    for markdown_file in markdown_files:
        # Read the Markdown content from each file
        with open(markdown_file, "r", encoding="utf-8") as file:
            markdown_content = file.read()

        # Convert Markdown to plain text
        plain_text = markdown_to_plain_text(markdown_content)

        # Save the plain text to a corresponding text file
        text_file = markdown_file.replace(".md", ".txt")
        with open(text_file, "w", encoding="utf-8") as output_file:
            output_file.write(plain_text)


if __name__ == "__main__":
    # Call the function to convert Markdown files to plain text
    convert_markdown_files_to_plain_text()
