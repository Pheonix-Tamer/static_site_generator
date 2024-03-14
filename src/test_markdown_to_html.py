import unittest

from markdown_to_html import *

with open("testing_markdown.md", "r") as f:
    md_doc = f

class TestMarkdownToHTML(unittest.TestCase):
    def test_markdown_to_html_node(self):
        markdown_to_html_node(md_doc)