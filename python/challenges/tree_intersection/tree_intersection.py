from typing import final
from data_structures.tree.tree import BinaryTree,Node
def tree_intersection(tree1,tree2):
    if (tree1.root and tree2.root):
        tree1_list=tree1.in_order()
        tree2_list=tree2.in_order()
        final_tree=[]
        for i in tree1_list:
            if i in tree2_list:
                final_tree.append(i)
        return final_tree
    else:
        return 'One of trees empty'


















bt = BinaryTree()
bt.root = Node(4)
bt.root.right = Node(9)
bt.root.left = Node(5)
bt.root.right.left = Node(6)
bt.root.left.left = Node(3)
bt.root.left.right = Node(7)

bt2 = BinaryTree()
bt2.root = Node(10)
bt2.root.right = Node(5)
bt2.root.left = Node(4)
bt2.root.right.left = Node(7)
bt2.root.left.left = Node(7)
bt2.root.left.right = Node(1)
print(tree_intersection(bt,bt2))
