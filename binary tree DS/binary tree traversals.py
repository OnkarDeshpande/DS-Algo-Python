
##binary tree traversals

##defining nodes in a BT
class node:
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None

#constructing a tree

#           5 --------------------root
#          / \
#         1   2 --------------------Nodes
#        /   / \
#       4   6   7
#                \
#                 10

root = node(5)
root.left = node(1)
root.right = node(2)
root.left.left = node(4)
root.right.left = node(6)
root.right.right = node(7)
root.right.right.right = node(10)


##Level order traversal will go like [5] -- [1,2] -- [4,6,7] -- [10]

#idea is to know the height of the tree, 4 in this case, recurssive approach

def height(node):
    if not node:
        return 0
    else:
        lef_height = height(node.left)
        rgt_height = height(node.right)

        if lef_height > rgt_height:
            return lef_height + 1
        else:
            return rgt_height + 1

print(height(root))


#next, we need to find nodes at a given level
# the nodes are stored in a list for a particular level
def nodeslevel(node,level,lst_val=[]):
    if not node:
        return
    if level == 1:
        lst_val.append(node.val)
    elif level > 1:
        nodeslevel(node.left,level-1,lst_val)
        nodeslevel(node.right,level-1,lst_val)
    return lst_val


print(nodeslevel(root,1,[]))
print(nodeslevel(root,2,[]))
print(nodeslevel(root,3,[]))


#finally we need to do this for all the levels


def ordertraversal(root):
    level_lst = []
    levels_cnt = height(root)
    for i in range(1,levels_cnt+1):
        level_lst.append(nodeslevel(root,i,[]))
    return level_lst

print(ordertraversal(root))


## reverse order would be:

def reversetraversal(root):
    level_lst = []
    levels_cnt = height(root)
    for i in range(levels_cnt,0,-1):
        level_lst.append(nodeslevel(root,i,[]))
    return level_lst

print(reversetraversal(root))


## another simple approch can just be using a stack:
def stack_order(root):
    stack_lst = [(root,0)]
    level_lst = []
    while stack_lst:
        node, level = stack_lst.pop()
        if node:
            if len(level_lst) < level+1:
                level_lst.insert(level,[])
            level_lst[level].append(node.val)
            stack_lst.append((node.right,level+1))
            stack_lst.append((node.left,level+1))
    return level_lst

print(stack_order(root))


def stack_reverse(root):
    stack_lst = [(root,0)]
    level_lst = []
    while stack_lst:
        node, level = stack_lst.pop()
        if node:
            if len(level_lst) < level+1:
                level_lst.insert(0,[])
            level_lst[-(level+1)].append(node.val)
            stack_lst.append((node.right,level+1))
            stack_lst.append((node.left,level+1))
    return level_lst

print(stack_reverse(root))


