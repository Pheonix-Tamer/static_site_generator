import unittest

from block_markdown import *

class TestDocToBlockMD(unittest.TestCase):
    def test_doc_to_blocks_list(self):
        raw_doc = """This is **bolded** paragraph

This is another paragraph with *italic* text and `code` here
This is the same paragraph on a new line

* This is a list
* with items"""
        self.assertListEqual(
            [
                "This is **bolded** paragraph", 
                "This is another paragraph with *italic* text and `code` here\nThis is the same paragraph on a new line", 
                "* This is a list\n* with items"
            ],
            markdown_to_blocks(raw_doc)
        )

    
    def test_multiple_newlines(self):
        raw_doc = ("This is **bolded** text\n\n\n\n\n\n\n"
                   "with too many newlines inbetween")
        self.assertListEqual(
            [
                "This is **bolded** text",
                "with too many newlines inbetween"
            ],
            markdown_to_blocks(raw_doc)
        )


    def test_long_paragraph(self):
        raw_doc = """This block will be a **really** *long* paragraph
in which *a lot* of text will be given as well as **multiple** lines
If the `lines are seperated` its no longer a `block`
which would be sad of course
this cannot be allowed to happen you see
so we must keep the really long paragraph a single block
or all logic will break down

In conclusion this is a seperate block"""
        self.assertListEqual(
            [
                """This block will be a **really** *long* paragraph
in which *a lot* of text will be given as well as **multiple** lines
If the `lines are seperated` its no longer a `block`
which would be sad of course
this cannot be allowed to happen you see
so we must keep the really long paragraph a single block
or all logic will break down""",
                "In conclusion this is a seperate block"
            ],
            markdown_to_blocks(raw_doc)
        )


    def test_block_type_heading(self):
        block_text = "### Headin 3"
        self.assertEqual(
            block_to_block_type(block_text),
            "heading"
        )
    

    def test_block_type_code(self):
        block_text = "```code block```"
        self.assertEqual(
            block_to_block_type(block_text),
            "code"
        )
    

    def test_block_type_quote(self):
        block_text = ">This is a quote\n>on multiple lines"
        self.assertEqual(
            block_to_block_type(block_text),
            "quote"
        )
    

    def test_block_type_unordered_list(self):
        block_text = "* this is a list\n* with items"
        self.assertEqual(
            block_to_block_type(block_text),
            "u_list"
        )
    

    def test_block_type_ordered_list(self):
        block_text = "1. this is ordered\n2. with numbers"
        self.assertEqual(
            block_to_block_type(block_text),
            "o_list"
        )
    

    def test_block_type_paragraph(self):
        block_text = "This should result in paragraph"
        self.assertEqual(
            block_to_block_type(block_text),
            "paragraph"
        )