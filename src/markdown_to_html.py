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
from htmlnode import ParentNode
from markdown_parse import text_to_textnodes
from textnode import text_node_to_html_node

file_path = "src/markdown/testing_markdown.md"
# Convert markdown to html format

def markdown_to_html_node(markdown):
    blocks = markdown_to_blocks(markdown)
    all_nodes = []
    for block in blocks:
        block_type = block_to_block_type(block)
        if block_type == block_type_heading:
            all_nodes.append(heading_block_to_html(block))
        elif block_type == block_type_code:
            all_nodes.append(code_block_to_html(block))
        elif block_type == block_type_quote:
            all_nodes.append(quote_block_to_html(block))
        elif block_type == block_type_ulist:
            all_nodes.append(ulist_block_to_html(block))
        elif block_type == block_type_olist:
            all_nodes.append(olist_block_to_html(block))
        elif block_type == block_type_paragraph:
            all_nodes.append(paragraph_block_to_html(block))
    return ParentNode("div", all_nodes)


def block_text_to_html_nodes(block) -> list:
    nodes = text_to_textnodes(block)
    leafnodes = []
    for node in nodes:
        leafnodes.append(text_node_to_html_node(node))
    return leafnodes


def heading_block_to_html(block) -> ParentNode:
    num_hash = 0
    for char in block:
        if char == '#':
            num_hash += 1
        elif char == ' ':
            break
    leafnodes = block_text_to_html_nodes(block[num_hash + 1:])
    match num_hash:
        case 1:
            heading = ParentNode("h1", leafnodes)
        case 2:
            heading = ParentNode("h2", leafnodes)
        case 3:
            heading = ParentNode("h3", leafnodes)
        case 4:
            heading = ParentNode("h4", leafnodes)
        case 5:
            heading = ParentNode("h5", leafnodes)
        case 6:
            heading = ParentNode("h6", leafnodes)
    return heading


def code_block_to_html(block):
    block = block.strip("`")
    leafnodes = block_text_to_html_nodes(block)
    code = ParentNode("code", leafnodes)
    return ParentNode("pre", [code])



def quote_block_to_html(block):
    lines = block.splitlines()
    lines_strip = []
    for line in lines:
            lines_strip.append(line[1:])
    leafnodes = block_text_to_html_nodes("\n".join(lines_strip))
    return ParentNode("blockquote", leafnodes)
        




def ulist_block_to_html(block):
    lines = block.splitlines()
    list_parents = []
    for line in lines:
        leafnodes = block_text_to_html_nodes(line[2:])
        list_parents.append(ParentNode("li", leafnodes))
    return ParentNode("ul", list_parents)





def olist_block_to_html(block):
    lines = block.splitlines()
    list_parents = []
    for line in lines:
        leafnodes = block_text_to_html_nodes(line[3:])
        list_parents.append(ParentNode("li", leafnodes))
    return ParentNode("ol", list_parents)



def paragraph_block_to_html(block):
    leafnodes = block_text_to_html_nodes(block)
    return ParentNode("p", leafnodes)
