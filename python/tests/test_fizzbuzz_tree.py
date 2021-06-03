from data_structures.tree.tree import *
import pytest

# Can successfully return breadth first tree
def test_breadth_first(fixed_binary_tree):
    assert fizz_buzz_tree(fixed_binary_tree).breadth_first() == ['4', 'FizzBuzz', 'Fizz', 'Fizz', 'Buzz', 'Fizz']

@pytest.fixture
def fixed_binary_tree():
    bt = BinaryTree()
    bt.root = Node(4)
    bt.root.right = Node(9)
    bt.root.left = Node(15)
    bt.root.right.left = Node(6)
    bt.root.left.left = Node(3)
    bt.root.left.right = Node(5)
    return bt
