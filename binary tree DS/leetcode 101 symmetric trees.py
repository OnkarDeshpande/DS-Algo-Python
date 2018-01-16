
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """

        #### recursive
        def checknode(root1, root2):

            # if both the nodes are none
            if not root1 and not root2:
                return True
            # if either of them is none
            elif not root1 or not root2:
                return False
            # checks if the value at this node is same, and the succeeding tree too
            else:
                return (
                root1.val == root2.val and checknode(root1.right, root2.left) and checknode(root1.left, root2.right))

        # we take them to two diff trees and compare
        return checknode(root, root)

# ####iterative
#         if not root:
#             return True

#     #this is a tuple in a list, everytime this tupe is checked for equivalence
#         stack_lst = [(root.left,root.right)]

#     #this will continue until there is a value in the list
#         while stack_lst:
#             #the tuple elements are assigned to two different var, each is the left and right node
#             l, r = stack_lst.pop()

#             #this condition takes care when both are none
#             if not l and not r:
#                 continue
#             #if either of them is none
#             if not l or not r:
#                 return False
#             #if both of them are not equal
#             if l.val != r.val:
#                 return False
#             #basically, if it comes here, the tree is symmetric and the following two pairs need to be checked
#             # leftnode**---node1---rightnode||  leftnode||---node2--rightnode**
#             # check the legends on nodes, same legends needs to be checked for equivalence

#             stack_lst.append((l.left,r.right))
#             stack_lst.append((l.right,r.left))

#         return True
