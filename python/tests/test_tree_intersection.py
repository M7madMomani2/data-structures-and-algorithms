import pytest
from challenges.tree_intersection.tree_intersection import tree_intersection,BinaryTree,Node


def test_tree_intersection(fixed_binary_tree1,fixed_binary_tree2):
    actual_out=tree_intersection(fixed_binary_tree1,fixed_binary_tree2)
    exp_out= [10, 7, 5]
    assert actual_out == exp_out


def test_tree_intersection(fixed_binary_tree3,fixed_binary_tree2):
    actual_out=tree_intersection(fixed_binary_tree3,fixed_binary_tree2)
    exp_out= 'One of trees empty'
    assert actual_out == exp_out


@pytest.fixture
def fixed_binary_tree1():
    binary_tree1=BinaryTree()
    binary_tree1.root = Node(6)
    binary_tree1.root.right = Node(5)
    binary_tree1.root.left = Node(-1)
    binary_tree1.root.right.left = Node(7)
    binary_tree1.root.left.left = Node(10)
    binary_tree1.root.right.right = Node(3)
    return binary_tree1

@pytest.fixture
def fixed_binary_tree2():
    binary_tree2=BinaryTree()
    binary_tree2.root = Node(7)
    binary_tree2.root.right = Node(5)
    binary_tree2.root.left = Node(10)
    binary_tree2.root.right.left = Node(5)
    binary_tree2.root.left.left = Node(10)
    binary_tree2.root.right.right = Node(0)
    return binary_tree2
@pytest.fixture
def fixed_binary_tree3():
    binary_tree3=BinaryTree()
    return binary_tree3
