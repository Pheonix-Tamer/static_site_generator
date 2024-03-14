from typing import Literal
from block_markdown import (
    block_type_paragraph,
    block_type_code,
    block_type_heading,
    block_type_olist,
    block_type_quote,
    block_type_ulist,
    block_to_block_type,
    markdown_to_blocks,
)
from markdown_parse import text_to_textnodes

file_path = "src/markdown/testing_markdown.md"
# Convert markdown to html format

def markdown_to_html_node(markdown):
    blocks = markdown_to_blocks(markdown)
    # blocks_tag = []
    for block in blocks:
        block_type = block_to_block_type(block)
        # print(block_type)
        # blocks_tag.append((block, block_type))
        if block_type == block_type_heading:
            heading_block_to_html(block)
        elif block_type == block_type_code:
            code_block_to_html(block)
        elif block_type == block_type_quote:
            quote_block_to_html(block)
        elif block_type == block_type_ulist:
            ulist_block_to_html(block)
        elif block_type == block_type_olist:
            olist_block_to_html(block)
        elif block_type == block_type_paragraph:
            paragraph_block_to_html(block)


def heading_block_to_html(block):
    nodes = text_to_textnodes(block)
    print(nodes)


def code_block_to_html(block):
    print("code")


def quote_block_to_html(block):
    pass


def ulist_block_to_html(block):
    pass


def olist_block_to_html(block):
    pass


def paragraph_block_to_html(block):
    pass


with open(file_path, "r") as f:
    md_doc = f.read()

markdown_to_html_node(md_doc)