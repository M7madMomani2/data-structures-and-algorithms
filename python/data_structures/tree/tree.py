class Node:
  def __init__(self, value):
    self.value = value
    self.next = None

class Stack:
  def __init__(self, node=None):
    self.top = node

  def push(self, value):
    if not self.top:
        self.top = Node(value)
    else:
        node = Node(value)
        node.next = self.top
        self.top = node


  def pop(self):
    if not self.is_empty():
      temp_node = self.top
      self.top = self.top.next
      temp_node.next = None
      return temp_node.value
    raise Exception("Cannot pop an empty Stack")

  def is_empty(self):
    return not self.top

class Queue:
  def __init__(self):
    self.front = None
    self.rear = None

class TNode:
  def __init__(self, value=None):
    self.value = value
    self.left = None
    self.right = None

class BinaryTree:
  def __init__(self, root=None):
    self.root = root

  def pre_order(self):
    """ Pre-order traversal of our tree """
    def walk(root):
      print(root.value)

      if root.left:
        walk(root.left)

      if root.right:
        walk(root.right)

    walk(self.root)

  def pre_order_iter(self):
    stack = Stack()
    stack.push(self.root)

    while not stack.is_empty():
      item = stack.pop()
      print(item.value)

      if item.right is not None:
        stack.push(item.right)

      if item.left is not None:
        stack.push(item.left)


class BinarySearchTree(BinaryTree):

    def add(self, data):
        if not self.root:
            self.root = TNode(data)

        else:
            def walk(root):
                if data < root.value:
                    if not root.left:
                        root.left = TNode(data)
                        return
                    else:
                        walk(root.left)
                else:
                    if not root.right:
                        root.right = TNode(data)
                        return
                    else:
                        walk(root.right)
            return walk(self.root)

    def contains(self, data):
        while self.root:
            if self.root.data == data:
                return True
            elif self.root.data > data:
                if self.root.left:
                    self.root = self.root.left
                else:
                    return False
            else:
                if self.root.right:
                    self.root = self.root.right
                else:
                    return False
        return False


if __name__ == "__main__":
  node1 = TNode(1)
  node1.left = TNode(2)
  node1.right = TNode(3)
  node1.right.left = TNode(4)
  node1.right.right = TNode(5)


  binary_tree = BinaryTree(node1)

  binary_tree.pre_order()





