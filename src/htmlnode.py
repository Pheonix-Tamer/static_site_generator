class HTMLNode:
    def __init__(self, tag:str=None, value:str=None, children:list=None, props:dict=None) -> None:
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props
        
    
    def to_html(self):
        raise NotImplementedError
    
    
    def props_to_html(self) -> str:
        new_string = ""
        for item in self.props:
            new_string = f"{new_string} {item}=\"{self.props[item]}\""
        return new_string
    
    
    def __repr__(self) -> str:
        return f"HTMLNode({self.tag}, {self.value}, children: {self.children}, {self.props})"


class LeafNode(HTMLNode):
    def __init__(self, tag: str = None, value: str = None, props: dict = None) -> None:
        super().__init__(tag, value, props=props)
        
    
    def to_html(self):
        if self.value is None:
            raise ValueError
        if self.tag is None:
            return self.value
        if self.props is not None:
            props_html = self.props_to_html()
        else:
            props_html = ""
        tagged = f"<{self.tag}{props_html}>{self.value}</{self.tag}>"
        return tagged
    
    
    def __repr__(self) -> str:
        return f"HTMLNode({self.tag}, {self.value}, {self.props})"


class ParentNode(HTMLNode):
    def __init__(self, tag: str = None, children: list = None, props: dict = None) -> None:
        super().__init__(tag, children=children, props=props)
        
    
    def to_html(self):
        if self.tag is None:
            raise ValueError("No tag provided")
        if self.children is None:
            raise ValueError("Child nodes are required")
        output = []
        for node in self.children:
            output.append(node.to_html())
        if self.props is None:
            return f"<{self.tag}>" + "".join(output) + f"</{self.tag}>"
        return f"<{self.tag}{self.props_to_html()}>" + "".join(output) + f"</{self.tag}>"
    
    
    def __repr__(self) -> str:
        return f"HTMLNode({self.tag}, children: {self.children}, {self.props})"