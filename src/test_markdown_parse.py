import unittest

# import test_textnode
from textnode import TextNode
from markdown_parse import *

class TestMarkdownParse(unittest.TestCase):    
    def test_parse_italics(self):
        node = TextNode("This is an *italics block* word", text_type_text)
        new_nodes = split_nodes_delimiter([node], "*", text_type_italic)
        self.assertListEqual(
            [TextNode("This is an " , "text", None), TextNode("italics block", "italic", None), TextNode(" word", "text", None)],
            new_nodes
        )
        
    def test_parse_bold(self):
        node = TextNode("This is a **bold block** word", text_type_text)
        new_nodes = split_nodes_delimiter([node], "**", text_type_bold)
        self.assertListEqual(
            [TextNode("This is a " , "text", None), TextNode("bold block", "bold", None), TextNode(" word", "text", None)],
            new_nodes
        )


    def test_text_not_parsed_with_broken_markdown(self):
        node = TextNode("This is *broken markdown", text_type_text)
        # self.assertRaises(
        #     ValueError("Not proper markdown"),
        #     new_nodes = split_nodes_delimiter([node], "*", text_type_italic)
        # )
        with self.assertRaises(ValueError):
            new_nodes = split_nodes_delimiter([node], "*", text_type_italic)


    def test_image_parse(self):
        node = TextNode("This is a test for images ![test](image.link/) with multi images ![image](gooogle.com)", text_type_text)
        image_nodes = extract_markdown_images(node.text)
        self.assertListEqual(
            [("test", "image.link/"), ("image", "gooogle.com")],
            image_nodes
        )
    
    def test_link_parse(self):
        node = TextNode("This is a test for links [link](link.url.com/) with another [another](another.url.co.uk)", text_type_text)
        link_nodes = extract_markdown_links(node.text)
        self.assertListEqual(
            [("link", "link.url.com/"), ("another", "another.url.co.uk")],
            link_nodes
        )

    
    def test_image_not_parsed_as_link(self):
        node = TextNode("This text has an image ![image](image.url.com) and link [link](link.url.co.uk) in it!", text_type_text)
        link_nodes = extract_markdown_links(node.text)
        self.assertListEqual(
            [("link", "link.url.co.uk")],
            link_nodes
        )

    
    def test_image_split_into_nodes(self):
        node = TextNode("This text has an image in it ![image](image.url) With text on both sides", text_type_text)
        split_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("This text has an image in it ", text_type_text), 
                TextNode("image", text_type_image, "image.url"), 
                TextNode(" With text on both sides", text_type_text)],
            split_nodes
        )
    

    def test_link_split_into_nodes(self):
        node = TextNode("This text has an link in it [link](/) With text on both sides", text_type_text)
        split_nodes = split_nodes_link([node])
        self.assertListEqual(
            [
                TextNode("This text has an link in it ", text_type_text), 
                TextNode("link", text_type_link, "/"), 
                TextNode(" With text on both sides", text_type_text)],
            split_nodes
        )


    def test_link_with_no_other_text(self):
        node = TextNode("[link](with.Nothing)", text_type_text)
        split_nodes = split_nodes_link([node])
        self.assertListEqual(
            [TextNode("link", text_type_link, "with.Nothing")],
            split_nodes
        )

    
    def test_image_split_with_link(self):
        node = TextNode("This is text with both an image ![image](image.url/png) and a link [link](link.co.url) inside it", text_type_text)
        split_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("This is text with both an image ", text_type_text),
                TextNode("image", text_type_image, "image.url/png"),
                TextNode(" and a link [link](link.co.url) inside it", text_type_text)
            ],
            split_nodes
        )

    
    def test_link_split_with_image(self):
        node = TextNode("This is text with both an image ![image](image.url/png) and a link [link](link.co.url) inside it", text_type_text)
        split_nodes = split_nodes_link([node])
        self.assertListEqual(
            [
                TextNode("This is text with both an image ![image](image.url/png) and a link ", text_type_text),
                TextNode("link", text_type_link, "link.co.url"),
                TextNode(" inside it", text_type_text)
            ],
            split_nodes
        )

    
    def test_image_node_split_with_only_image(self):
        node = TextNode("![image](only.the.link)", text_type_text)
        split_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("image", text_type_image, "only.the.link")
            ],
            split_nodes
        )


    def test_markdown_parse(self):
        node = "This is **text** with an *italic* word and a `code block` and an ![image](image.url) and a [link](link.url.com)"
        nodes = text_to_textnodes(node)
        self.assertListEqual(
            [
                TextNode("This is ", text_type_text),
                TextNode("text", text_type_bold),
                TextNode(" with an ", text_type_text),
                TextNode("italic", text_type_italic),
                TextNode(" word and a ", text_type_text),
                TextNode("code block", text_type_code),
                TextNode(" and an ", text_type_text),
                TextNode("image", text_type_image, "image.url"),
                TextNode(" and a ", text_type_text),
                TextNode("link", text_type_link, "link.url.com"),
            ],
            nodes
        )
        
        
if __name__ == "__main__":
    unittest.main()