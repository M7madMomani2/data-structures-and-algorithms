from data_structures.tree.tree import *
import pytest

# Can successfully instantiate an empty tree
def test_empty_tree():
    new_tree = BinarySearchTree()
    assert new_tree.root == None

# Can successfully instantiate a tree with a single root node
def test_single_root_node(fixed_tree):
    fixed_tree.add(9)
    assert fixed_tree.root.value == 9

# Can successfully add a left child and right child to a single root node
def test_left_right_node(fixed_tree):
    fixed_tree.add(9)
    fixed_tree.add(5)
    fixed_tree.add(10)
    assert fixed_tree.root.left.value == 5
    assert fixed_tree.root.right.value == 10

# Can successfully show data in pre order
def test_preOrder(fixed_tree_with_elements):
    assert fixed_tree_with_elements.pre_order() == [7, 5, 1, 9, 8, 11]

# Can successfully show data in in_order
def test_inOrder(fixed_tree_with_elements):
    assert fixed_tree_with_elements.in_order() == [1, 5, 7, 8, 9, 11]

# Can successfully show data in post_order
def test_postOrder(fixed_tree_with_elements):
    assert fixed_tree_with_elements.post_order() == [1, 5, 8, 11, 9, 7]

# Can successfully return max of tree
def test_max(fixed_tree_with_elements):
    assert fixed_tree_with_elements.find_maximum_value(fixed_tree_with_elements) == 11

@pytest.fixture
def fixed_tree():
    tree=BinarySearchTree()
    return tree

@pytest.fixture
def fixed_tree_with_elements():
    tree=BinarySearchTree()
    tree.add(7)
    tree.add(9)
    tree.add(5)
    tree.add(11)
    tree.add(8)
    tree.add(1)
    return tree
