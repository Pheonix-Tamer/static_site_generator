import re

block_type_paragraph = "paragraph"
block_type_heading = "heading"
block_type_code = "code"
block_type_quote = "quote"
block_type_ulist = "u_list"
block_type_olist = "o_list"


def markdown_to_blocks(markdown: str):
    blocks = []
    lines = markdown.splitlines()
    curr_block = []
    for line in lines:
        if line != "":
            curr_block.append(line)
        else:
            if len(curr_block) != 0:
                blocks.append("\n".join(curr_block).strip())
                curr_block = []
    blocks.append("\n".join(curr_block).strip())
    
    return blocks


def block_to_block_type(block):
    lines = block.splitlines()
    if re.match(r"(?<!#)#{1,6} .+", block):
        return block_type_heading
    if re.match(r"^`{3}.+`{3}", block):
        return block_type_code
    if block[0] == ">":
        for line in lines:
            if not line.startswith(">"):
                break
            return block_type_quote
    if block.startswith("* "):
        for line in lines:
            if not line.startswith("* "):
                return block_type_paragraph
            return block_type_ulist
    if block.startswith("- "):
        for line in lines:
            if not line.startswith("- "):
                return block_type_paragraph
        return block_type_ulist
    if block.startswith("1. "):
        i = 1
        for line in lines:
            if not line.startswith(f"{i}. "):
                return block_type_paragraph
            i += 1
        return block_type_olist
    return block_type_paragraph
