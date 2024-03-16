import unittest

from markdown_to_html import *
from textnode import TextNode
from htmlnode import LeafNode

with open("src/markdown/testing_markdown.md", "r") as f:
    md_doc = f.read()

class TestMarkdownToHTML(unittest.TestCase):
    def test_markdown_to_html_node(self):
        print(markdown_to_html_node(md_doc).to_html())
        self.assertEqual(
            ('<div><h1>This is a test markdown file</h1><p>In which multiple <b>different</b> blocks are <i>here</i></p><pre><code>With Code blocks and all</code></pre><ul><li>Lists</li><li>Galore</li></ul><ol><li>Ordered to</li><li>Or I wouldnt be here</li></ol><h2>A heading for your heading</h2><blockquote>With Quotes from such favourites as:'
'\nJesus\n'
'The man down stairs</blockquote><p>And objects <code>within</code> the lines we make</p><p>with links to google <a href="https://www.google.co.uk">link to google</a></p><p>and imagaes here <img src="https://i.imgur.com/hpiGU9U.jpeg" alt="image1"></img> there and everywhere</p><p>this is an incredibly stupid <b>Markdown</b> file but <i>IT WORKS</i></p></div>'),
            markdown_to_html_node(md_doc).to_html()
        )


    def test_heading_block_to_html(self):
        text = "## This is a level 2 heading"
        heading = heading_block_to_html(text)
        self.assertEqual(
            "<h2>This is a level 2 heading</h2>",
            heading.to_html()
        )

    
    def test_heading_block_to_html_six(self):
        text = "###### This is a level 6 heading"
        self.assertEqual(
            "<h6>This is a level 6 heading</h6>",
            heading_block_to_html(text).to_html()
        )


    def test_ulist_block_to_html(self):
        ulist = "* this *is* a list\n* with **many** lines\n* *All* of which are **important**"
        self.assertEqual(
            "<ul><li>this <i>is</i> a list</li><li>with <b>many</b> lines</li><li><i>All</i> of which are <b>important</b></li></ul>",
            ulist_block_to_html(ulist).to_html()
        )
    

    def test_olist_block_to_html(self):
        olist = "1. This is an ordered list\n2. which has **numbers** at the start of each line\n3. Meaning that its there"
        self.assertEqual(
            "<ol><li>This is an ordered list</li><li>which has <b>numbers</b> at the start of each line</li><li>Meaning that its there</li></ol>",
            olist_block_to_html(olist).to_html()
        )
    

    def test_code_block_to_html(self):
        code_block = "```This is a code block with *monospaced* characters```"
        self.assertEqual(
            f"<pre><code>This is a code block with <i>monospaced</i> characters</code></pre>",
            code_block_to_html(code_block).to_html()
        )
    

    def test_quote_block_to_html(self):
        quote = ">This is a quote\n>Directly from the bureau\n>It will self destruct"
        self.assertEqual(
            "<blockquote>This is a quote\nDirectly from the bureau\nIt will self destruct</blockquote>",
            quote_block_to_html(quote).to_html()
        )
    

    def test_paragraph_block_to_html(self):
        para = "This is a bogstandard paragraph\nComplete with newlines and all!"
        self.assertEqual(
            "<p>This is a bogstandard paragraph\nComplete with newlines and all!</p>",
            paragraph_block_to_html(para).to_html()
        )