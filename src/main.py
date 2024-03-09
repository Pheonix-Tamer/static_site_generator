from textnode import TextNode
from htmlnode import ParentNode, LeafNode

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

output = node.to_html()
print(output)
