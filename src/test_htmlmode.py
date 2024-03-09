import unittest

from htmlnode import HTMLNode, LeafNode, ParentNode

class TestHTMLNode(unittest.TestCase):
    def test_props_to_html(self):
        node = HTMLNode("tag", "value", props={"href": "https://www.google.com", "target": "_blank"})
        self.assertEqual(
            ' href="https://www.google.com" target="_blank"', node.props_to_html()
        )
    
    
    def test_to_html_leaf(self):
        node = LeafNode("a", "Click Me!", {"href": "https://www.google.com"})
        self.assertEqual(
            node.to_html(),
            '<a href="https://www.google.com">Click Me!</a>'
        )
        
    
    def test_parent_child(self):
        node = ParentNode(
            "p",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "Italic text"),
                LeafNode(None, "Normal text"),
            ]
        )
        self.assertEqual(
            "<p><b>Bold text</b>Normal text<i>Italic text</i>Normal text</p>",
            node.to_html()
        )
        
        
    def test_parent_of_parent_nodes(self):
        node = ParentNode(
            "p",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                ParentNode(
                    "p",
                    [
                        LeafNode("b", "Bold text", {"href": "google.com"}),
                        LeafNode(None, "Normal text")
                    ]
                ),
                LeafNode("i", "Italic text")
            ]
        )
        self.assertEqual(
            '<p><b>Bold text</b>Normal text<p><b href="google.com">Bold text</b>Normal text</p><i>Italic text</i></p>',
            node.to_html()
        )
        
        
    def test_multiple_parents(self):
        node = ParentNode(
            "a",
            [
                ParentNode(
                    "b",
                    [
                        LeafNode("b1", "This is b1", {"btarget": "targetB"}),
                        LeafNode("b2", "This is b2")
                    ],
                    {
                        "href": "google.com"
                    }
                ),
                ParentNode(
                    "c",
                    [
                        LeafNode("c1", "This is c1"),
                        LeafNode("c2", "This is c2")
                    ]
                )
            ]
        )
        self.assertEqual(
            '<a><b href="google.com"><b1 btarget="targetB">This is b1</b1><b2>This is b2</b2></b><c><c1>This is c1</c1><c2>This is c2</c2></c></a>',
            node.to_html()
        )
        
        
        
if __name__ == "__main__":
    unittest.main()