import unittest

from textnode import TextNode, text_node_to_html_node


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", "bold")
        node2 = TextNode("This is a text node", "bold")
        self.assertEqual(node, node2)
        
        
    def test_eq_false_text_type(self):
        node = TextNode("This is a text node", "italic")
        node2 = TextNode("This is a text node", "bold")
        self.assertNotEqual(node, node2)
        
    
    def test_eq_false_text(self):
        node = TextNode("This is a text node", "bold")
        node2 = TextNode("This is a text node2", "bold")
        self.assertNotEqual(node, node2)
        
        
    def test_eq_url(self):
        node = TextNode("This is a text node", "bold", "https://google.com")
        node2 = TextNode("This is a text node", "bold", "https://google.com")
        self.assertEqual(node, node2)
        
    
    def test_repr(self):
        node = TextNode("This is a text node", "bold", "https://google.com")
        self.assertEqual(
            "TextNode('This is a text node', bold, 'https://google.com')", repr(node)
        )
        

if __name__ == "__main__":
    unittest.main()
