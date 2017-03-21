# coding=utf-8
from graphviz import Digraph
import rbtree

class Graph(object):
    def __init__(self):
        self.dot = Digraph("G", comment="RBTree")
        self.dot_red = Digraph(comment="Red", node_attr={"style": "filled", "color": "red"})
        self.dot_black = Digraph(comment="Black", node_attr={"style": "filled", "color": "black", "fontcolor": "white"})

    def GraphNode(self, node):
        if node.color == rbtree.RED:
            self.dot_red.node(str(node.key), str(node.key))
        else:
            self.dot_black.node(str(node.key), str(node.key))
        if node.left is not None:
            self.GraphNode(node.left)
        if node.right is not None:
            self.GraphNode(node.right)

    def EdgeNode(self, node):
        if node.left is not None:
            self.dot.edge(str(node.key), str(node.left.key))
            self.EdgeNode(node.left)
        if node.right is not None:
            self.dot.edge(str(node.key), str(node.right.key))
            self.EdgeNode(node.right)


    def GraphTree(self, rbtree):
        if rbtree is None:
            return False
        if rbtree.root is None:
            return False
        self.GraphNode(rbtree.root)
        self.dot.subgraph(self.dot_red)
        self.dot.subgraph(self.dot_black)
        self.EdgeNode(rbtree.root)


    def View(self):
        self.dot.view()

    def Render(self):
        self.dot.render('test-output/test.dot', view=False)











# dot_red.node("A", "AAA")
# dot_black.node("B", "BBB")
# dot_black.node("C", "CCC")
#
# dot.subgraph(dot_red)
# dot.subgraph(dot_black)
#
# dot.edge("A", "B")
# dot.edge("A", "C")
#
#
#
# dot.view()

#dot.render('test-output/test.gv', view=True)


