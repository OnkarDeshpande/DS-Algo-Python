
## basic data structure

#the following class initiates a node with value val and creates left child and right child initialized to None
class node:
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None

#constructing a tree

#as simple as it can get if we were to design the following tree:
#           5 --------------------root
#          / \
#         1   2 --------------------Nodes
#        /    /
#       4    6 --------------------Leaves

#defining root
root = node(5)
#further nodes are addressed keeping root in place
root.left = node(1)
root.right = node(2)
root.left.left = node(4)
root.right.left = node(6)

#desired tree is in var root
