from htmlnode import LeafNode

text_type_text = "text"
text_type_bold = "bold"
text_type_italic = "italic"
text_type_code = "code"
text_type_link = "link"
text_type_image = "image"

delimiter_text_types = {
    "**": text_type_bold,
    "*": text_type_italic,
    "`": text_type_code
}

class TextNode:
    def __init__(self, text: str, text_type: str, url: str=None) -> None:
        self.text = text
        self.text_type = text_type
        self.url = url
        
    
    def __eq__(self, other) -> bool:
        if (self.text == other.text
            and self. text_type == other.text_type
            and self.url == other.url):
            return True
        return False
        
    
    
    def __repr__(self) -> str:
        return f"TextNode('{self.text}', {self.text_type}, '{self.url}')"


def text_node_to_html_node(text_node: TextNode):
    if text_node.text_type == text_type_text:
        return LeafNode(None, text_node.text)
    if text_node.text_type == text_type_bold:
        return LeafNode("b", text_node.text)
    if text_node.text_type == text_type_italic:
        return LeafNode("i", text_node.text)
    if text_node.text_type == text_type_code:
        return LeafNode("code", text_node.text)
    if text_node.text_type == text_type_link:
        return LeafNode("a", text_node.text, {"href": text_node.url})
    if text_node.text_type == text_type_image:
        return LeafNode("img", "", {"src": text_node.url, "alt": text_node.text})
    raise Exception("Not an accepted text type")
            