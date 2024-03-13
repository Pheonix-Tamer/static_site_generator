import textnode
import markdown_parse
from htmlnode import ParentNode, LeafNode

def main():
    # nodes = [
    #     textnode.TextNode("This is *a* test one", textnode.text_type_text),
    #     textnode.TextNode("This is a *test* two", textnode.text_type_text),
    #     textnode.TextNode("This **is** a test three", textnode.text_type_text)
    # ]
    # node = textnode.TextNode("This is text with an *italics block* word", textnode.text_type_text)
    # new_nodes = markdown_parse.split_nodes_delimiter([node], "*", textnode.text_type_italic)
    # # print(type(nodes[0]))
    # # if type(nodes[0]) == textnode.TextNode:
    # #     print("This is a text node")
    # # print(textnode.delimiter_text_types["*"])
    # print(new_nodes)
    test_str = textnode.TextNode("This is text with an image ![image](https://image.com/zuzuirnsi.png) woo ![another](google.com) After last image test", textnode.text_type_text)
    test_str_2 = textnode.TextNode("This is text with an image ![image](https://image.com/zuzuirnsi.png) woo ![another](google.com)", textnode.text_type_text)
    test_2 = textnode.TextNode("Text with no link or image", textnode.text_type_text)
    test_3 = textnode.TextNode("![start](start.co.uk) This text starts with a image link", textnode.text_type_text)
    print(markdown_parse.split_nodes_image([test_3]))
    text_noo = "This is a split test"
    # print(text_noo.split("!"))


main()
