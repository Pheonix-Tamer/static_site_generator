import re

from test_textnode import TestTextNode
from textnode import (
    text_type_text,
    text_type_bold,
    text_type_italic,
    text_type_code,
    text_type_image,
    text_type_link,
    TextNode
)

# text_list = node.text.split(delimiter)
def split_nodes_delimiter(old_nodes: list, delimiter: str, text_type):
    new_nodes = []
    for node in old_nodes:
        if node.text_type != text_type_text:
            new_nodes.append(node)
            continue
        split_nodes = []
        sections = node.text.split(delimiter)
        if len(sections) % 2 == 0:
            raise ValueError("Not proper markdown")
        for i in range(len(sections)):
            if sections[i] == "":
                continue
            if i % 2 == 0:
                split_nodes.append(TextNode(sections[i], text_type_text))
            elif i % 2 == 1:
                split_nodes.append(TextNode(sections[i], text_type))
        new_nodes.extend(split_nodes)
        
    return new_nodes


def extract_markdown_images(text):
    matches = re.findall(r"!\[(.*?)\]\((.*?)\)", text)
    return matches


def extract_markdown_links(text):
    matches = re.findall(r"(?<!!)\[(.*?)\]\((.*?)\)", text)
    return matches


def split_nodes_image(old_nodes: list) -> list:
    """Function to take a list of nodes and extract the image "links" from them
        and return a new list of nodes with the correctly parsed outputs

    Args:
        old_nodes (list): List of TextNode objects
    """
    new_nodes = []
    for node in old_nodes:
        if node.text_type != text_type_text:
            new_nodes.append(node)
            continue
        original_text = node.text
        if original_text == "":
            continue
        images_data = extract_markdown_images(original_text)
        if images_data is None:
            new_nodes.append(node)
        new_text = original_text
        split_nodes = []

        for image_tup in images_data:
            split_text = new_text.split(f"![{image_tup[0]}]({image_tup[1]})", 1)
            if split_text[0] != "":
                split_nodes.append(TextNode(split_text[0], text_type_text))
            split_nodes.append(TextNode(image_tup[0], text_type_image, image_tup[1]))
            new_text = split_text[1]
        if new_text != "":
            split_nodes.append(TextNode(new_text, text_type_text))
        new_nodes.extend(split_nodes)

    return new_nodes
            


def split_nodes_link(old_nodes: list) -> list:
    """Function to split an input of text which contains markdown links and retuns a list of nodes with their respective text_type

    Args:
        old_nodes (list): A list of TextNode objects
    """
    new_nodes = []
    for node in old_nodes:
        if node.text_type != text_type_text:
            new_nodes.append(node)
            continue
        original_text = node.text
        if original_text == "":
            continue
        links_data = extract_markdown_links(original_text)
        if links_data is None:
            new_nodes.append(node)
        iter_text = original_text
        split_nodes = []
        for link_tup in links_data:
            split_text = iter_text.split(f"[{link_tup[0]}]({link_tup[1]})", 1)
            if split_text[0] != "":
                split_nodes.append(TextNode(split_text[0], text_type_text))
            split_nodes.append(TextNode(link_tup[0], text_type_link, link_tup[1]))
            iter_text = split_text[1]
        if iter_text != "":
            split_nodes.append(TextNode(iter_text, text_type_text))
        new_nodes.extend(split_nodes)

    return new_nodes


def text_to_textnodes(raw_text):
    raw_textnode = TextNode(raw_text, text_type_text)
    nodes = [raw_textnode]
    nodes = split_nodes_delimiter(nodes, "**", text_type_bold)
    nodes = split_nodes_delimiter(nodes, "*", text_type_italic)
    nodes = split_nodes_delimiter(nodes, "`", text_type_code)
    nodes = split_nodes_image(nodes)
    nodes = split_nodes_link(nodes)
    return nodes