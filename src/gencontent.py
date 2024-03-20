from genericpath import isfile
import os
from markdown_to_html import markdown_to_html_node

def extract_title(markdown):
    lines = markdown.splitlines()
    for line in lines:
        if line.startswith("# "):
            return line
    raise Exception("No h1 header in Markdown file")


def generate_page(from_path, template_path, dest_path):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")
    with open(from_path, "r") as f:
        markdown = f.read()
    with open(template_path, "r") as f:
        template = f.read()
    title = extract_title(markdown)
    # markdown = markdown.split(title)
    html = markdown_to_html_node(markdown)
    title_html = markdown_to_html_node(title)
    template = template.replace(r"{{ Title }}", title_html.to_html())
    template = template.replace(r"{{ Content }}", html.to_html())
    with open(dest_path, 'x') as h:
        h.write(template)


def generate_pages_recursively(dir_path_content, template_path, dest_dir_path):
    if not os.path.exists(dest_dir_path):
        os.mkdir(dest_dir_path)
    dest_file_name = "index.html"
    for dir in os.listdir(dir_path_content):
        current_dir = os.path.join(dir_path_content, dir)
        dest_dir = os.path.join(dest_dir_path, dest_file_name)
        if os.path.isfile(current_dir):
            generate_page(current_dir, template_path, dest_dir)
        else:
            generate_pages_recursively(current_dir, template_path, os.path.join(dest_dir_path, dir))