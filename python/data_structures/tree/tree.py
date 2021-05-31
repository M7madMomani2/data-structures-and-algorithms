class EmptyTreeException(Exception):
  pass

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

  def bread_first(self):
     # Use queque for FIFO
     pass




class BSTNode(BinaryTree):
    def __init__(self, value= None):
        self.value = value
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self, root=None):
        self.root = root


    def pre_order(self):
        pre_order_list = []
        """ Pre-order traversal of our tree """
        def walk(root):
            if root is  None:
                raise EmptyTreeException("the tree is empty")
                pre_order_list.append(root.value)

            if root.left:
                walk(root.left)

            if root.right:
                walk(root.right)

        walk(self.root)
        return ' '.join(f"{pre_order_list}")




    def add(self ,root, value):
        if root is None:
            return BSTNode(value)
        else:
            if root.value == value:
                return root
            elif root.value < value:
                root.right = self.add(root.right, value)
            else:
                root.left = self.add(root.left, value)
        print (f"{value} has been added successfully")
        return root

    def pre_order(self,root):
        pre_order_list = []

        if root is  None:
            raise EmptyTreeException("the tree is empty")
        new_root = root
        def pre_walk(root):
            if root:
                pre_order_list.append(root.value)
                if root.left:
                     pre_walk(root.left)

                if root.right:
                     pre_walk(root.right)

        pre_walk(new_root)
        return ' '.join(f"{pre_order_list}")


    def contains(self,root,value):
        self.count_n = 0
        self.found = None
        if root is None:
            raise EmptyTreeException("the tree is empty")
        def contains_search(root,value):

                if root is None or root.value == value:
                    self.found = root
                    return root

                if root.value < value:
                    self.count_n +=1
                    return contains_search(root.right,value)
                else:
                     self.count_n +=1
                     return contains_search(root.left,value)
        contains_search(root,value)
        if self.found is None:
            print("not found")
            return False

        print( f"{self.found.value} has been found and the depth of it is {self.count_n}")
        return True

    def find_maximum_value(self):
        self.max=self.root.value

        def _walk(node):
            if node.value > self.max:
                self.max =node.value
            if node.left:
                _walk(node.left)
            if node.right:
                _walk(node.right)

        _walk(self.root)
        return self.max



class Binary_search_tree:
  def __init__(self,value=None):
    self.node = TNode(value)
  def add(self,value):
    if (self.node.value == None):
      self.node.value = value
    else:
      if value == self.node.value:
        return 'no duplicates allowed in binary search self'
      if (value < self.node.value):
        if(self.node.left):
          self.node.left.add(value)
        else:
          self.node.left = Binary_search_tree(value)
      else:
        if(self.node.right):
          self.node.right.add(value)
        else:
          self.node.right = Binary_search_tree(value)

  def in_order(self, lst = []):
    if (self.node.left):
        self.node.left.in_order(lst)
    lst.append(self.node.value)
    if (self.node.right):
        self.node.right.in_order(lst)
    return lst

  def contains(self,value,parent= None):
    if value == self.node.value: return True
    if (value < self.node.value):
      if (self.node.left):
        return self.node.left.contains(value, self.node)
      else:
        return False
    else:
      if (self.node.right):
        return self.node.right.contains(value, self.node)
      else:
        return False




if __name__ == "__main__":

    obj = BinarySearchTree()
    bst_node = BSTNode(50)
    bst_node = obj.add(bst_node, 20)
    bst_node = obj.add(bst_node,600)
    bst_node = obj.add(bst_node,100)
    bst_node = obj.add(bst_node,1)
    bst_node = obj.add(bst_node,1000)
    print(obj.pre_order(bst_node))
    print(obj.contains(bst_node,0))
    print(obj.contains(bst_node,20))
    print(obj.contains(bst_node,1))



    print("-"*50)

    node1 = TNode(1)
    node1.left = TNode(2)
    node1.right = TNode(3)
    node1.right.left = TNode(4)
    node1.right.right = TNode(5)

    binary_tree = BinaryTree(node1)

    print(binary_tree.pre_order())
    print(binary_tree.pre_order())

    # binary_tree.pre_order_iter()
    print("-"*20)
    print(binary_tree.in_order())

    print("-"*20)
    print(binary_tree.post_order())

