# class Node:
#     def __init__(self, value):
#         self.value = value
#         self.right = None
#         self.left = None
#         self.next = None
# class Queue:
#     def __init__(self):
#         self.front = None
#         self.rear = None

#     def enqueue(self,value):
#         node = Node(value)

#         if self.isEmpty():
#             self.front = node
#             self.rear = node

#         else:
#             self.rear.next = node
#             self.rear = node

#     def dequeue(self):
#         try:
#             if self.isEmpty():
#                 raise Exception('Empty Queue')
#             else:
#                 temp = self.front
#                 self.front = self.front.next
#                 return temp.value
#         except:
#             return 'Empty Queue'

#     def peek(self):
#         try:
#             if self.isEmpty():
#                 raise Exception('Empty Queue')
#             else:
#                 return self.front.value
#         except:
#             return 'Empty Queue'

#     def isEmpty(self):
#         if self.front:
#             return False
#         else :
#             return True


#     def to_string(self):
#         current = self.front
#         current_string = f" { {current.value} }"

#         while current.next:
#             current = current.next
#             current_string += f" -> { {current.value} }"

#         return f"{ current_string } -> NULL"

# class BinaryTree:
#     def __init__(self):
#         self.root = None
#         self.maxVal = 0


#     def pre_order(self):
#         output = []

#         def _walk(node):
#             output.append(node.value)
#             if node.left:
#                 _walk(node.left)
#             if node.right:
#                 _walk(node.right)

#         _walk(self.root)
#         return output


#     def in_order(self):
#         output = []

#         def _walk(node):
#             if node.left:
#                 _walk(node.left)

#             output.append(node.value)

#             if node.right:
#                 _walk(node.right)

#         _walk(self.root)
#         return output


#     def post_order(self):
#         output = []

#         def _walk(node):
#             if node.left:
#                 _walk(node.left)
#             if node.right:
#                 _walk(node.right)

#             output.append(node.value)

#         _walk(self.root)
#         return output

#     def find_maximum_value(self, tree):

#         def _walk(node):
#             if self.maxVal < node.value:
#                 self.maxVal = node.value

#             if node.left:
#                 _walk(node.left)
#             if node.right:
#                 _walk(node.right)

#         _walk(self.root)
#         return self.maxVal

#     def breadth_first(self, tree):
#         temp = []
#         results = []

#         if self.root:
#             temp.append(self.root)

#             while temp:
#                 node = temp.pop()
#                 results.append(node.value)

#                 if node.left:
#                     temp.append(node.left)
#                 if node.right:
#                     temp.append(node.right)
#             return results
#         else:
#             return 'Empty'



# class BinarySearchTree(BinaryTree):
#     def __init__(self):
#         self.root = None
#         self.maxVal = 0



#     def add(self, value):
#         if not self.root:
#             self.root = Node(value)

#         else:
#             def _walk(node):
#                 if value < node.value:
#                     # go left
#                     if not node.left:
#                         node.left = Node(value)
#                         return
#                     else:
#                         _walk(node.left)

#                 else:
#                     # go right
#                     if not node.right:
#                         node.right = Node(value)
#                         return
#                     else:
#                         _walk(node.right)

#             _walk(self.root)


#     def contains(self, value):
#         output = []

#         def _walk(node):
#             output.append(node.value)
#             if node.left:
#                 _walk(node.left)
#             if node.right:
#                 _walk(node.right)

#         _walk(self.root)

#         if value in output:
#             return True
#         else:
#             return False




#     def breadth_first(self):
#         if self.root:
#             output=[]
#             q = Queue()
#             q.enqueue(self.root)

#             while q.front != None:
#                 current = q.front

#                 if current.left:
#                     q.enqueue(current.left)
#                 if current.right:
#                     q.enqueue(current.right)

#                 output.append(current.value)
#                 q.dequeue()

#             return output
#         else:
#             return 'Empty Tree'


#     def find_maximum_value(self, tree):

#         def _walk(node):
#             if self.maxVal < node.value:
#                 self.maxVal = node.value

#             if node.left:
#                 _walk(node.left)
#             if node.right:
#                 _walk(node.right)

#         _walk(self.root)
#         return self.maxVal

#     def sum_odd(self):
#         temp = []
#         sum = 0
#         if self.root:
#             temp.append(self.root)
#             while temp:
#                 node = temp.pop()
#                 if  (node.value%2):
#                     sum+=node.value
#                 if node.left:
#                     temp.append(node.left)
#                 if node.right:
#                     temp.append(node.right)
#             return sum
#         else:
#             return 'Empty'


# def FizzBuzzTree(tree):
#     new_tree = tree
#     if new_tree.root != None:

#         def _walk(node):
#             if node.value%3==0 and node.value%5==0:
#                 node.value = 'FizzBuzz'
#             elif node.value%3==0:
#                 node.value = 'Fizz'
#             elif node.value%5==0:
#                 node.value = 'Buzz'
#             elif node.value%3!=0 and node.value%5!=0:
#                 node.value = str(node.value)


#             if node.left:
#                 _walk(node.left)
#             if node.right:
#                 _walk(node.right)

#         _walk(new_tree.root)
#         return new_tree
#     else:
#         new_tree.root =Node('Tree is Empty')
#         return new_tree



# if __name__ == "__main__":
#     bt = BinaryTree()
#     bst = BinarySearchTree()
#     bt.root = Node(6)
#     bt.root.right = Node(5)
#     bt.root.left = Node(-1)
#     bt.root.right.left = Node(7)
#     bt.root.left.left = Node(10)
#     bt.root.right.right = Node(3)
#     # print(bt.pre_order())
#     # print(bt.in_order())
#     # print(bt.post_order())
#     print('The Maximum Value of BinarTree is:',bt.find_maximum_value(bt))
#     # print('breadth_first for BinaryTree',bt.breadth_first(bt))
#     print('*************** BST ****************')
#     bst.add(4)
#     bst.add(9)
#     bst.add(-1)
#     bst.add(6)
#     bst.add(3)
#     bst.add(8)
#     bst.add(5)

#     # print(bst.sum_odd())
#     print('breadth_first For BinarySearchTree',bst.breadth_first())
#     print(FizzBuzzTree(bt).breadth_first(bt))












class Queue:
    def __init__(self):
        self.front = None
        self.rear = None

    def enqueue(self,value):
        new_node = value

        if self.rear:
            self.rear.next = new_node
            self.rear = new_node

        else:
            self.front = new_node
            self.rear = new_node

    def dequeue(self):
        try:
            if self.front:
                temp = self.front
                self.front = self.front.next
                return temp.value
            else:
                raise Exception('Empty Queue')
        except:
            return 'Empty Queue'

    def peek(self):
        try:
            if self.front:
                return self.front.value
            else:
                raise Exception('Empty Queue')
        except:
            return 'Empty Queue'

    def isEmpty(self):
        if self.front:
            return False
        elif not self.front:
            return True

class Node:
    def __init__(self,value):
        self.value = value
        self.next = None
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None

    def pre_order(self):
        output=[]

        def _walk(node):
            output.append(node.value)
            if node.left:
                _walk(node.left)
            if node.right:
                _walk(node.right)

        _walk(self.root)
        return output

    def in_order(self):
        output=[]

        def _walk(node):
            if node.left:
                _walk(node.left)
            output.append(node.value)
            if node.right:
                _walk(node.right)

        _walk(self.root)
        return output

    def post_order(self):
        output=[]

        def _walk(node):
            if node.left:
                _walk(node.left)
            if node.right:
                _walk(node.right)
            output.append(node.value)

        _walk(self.root)
        return output

    def breadth_first(self):
        if self.root:
            output=[]
            q = Queue()
            q.enqueue(self.root)

            while q.front != None:
                current = q.front

                if current.left:
                    q.enqueue(current.left)
                if current.right:
                    q.enqueue(current.right)

                output.append(current.value)
                q.dequeue()

            return output
        else:
            return 'Empty Tree'

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


class BinarySearchTree(BinaryTree):

    def add(self, value):
        if not self.root:
            self.root = Node(value)
        else:
            def _walk(node):

                if value < node.value:
                    if not node.left:
                        node.left = Node(value)
                        return
                    else:
                        _walk(node.left)
                else:
                    if not node.right:
                        node.right = Node(value)
                        return
                    else:
                        _walk(node.right)

            _walk(self.root)

    def contains(self,value):
        if self.root:
            current = self.root
            def _walk(current):
                if value == current.value:
                    return True
                elif value < current.value:
                    current = current.left
                    if current:
                        return _walk(current)
                elif value > current.value:
                    current = current.right
                    if current:
                        return _walk(current)

            if _walk(current) == True:
                return True
            else:
                return False
        else:
            return False


def FizzBuzzTree(tree):
    new_tree = tree
    if new_tree.root != None:

        def _walk(node):
            if node.value%3==0 and node.value%5==0:
                node.value = 'FizzBuzz'
            elif node.value%3==0:
                node.value = 'Fizz'
            elif node.value%5==0:
                node.value = 'Buzz'
            elif node.value%3!=0 and node.value%5!=0:
                node.value = str(node.value)


            if node.left:
                _walk(node.left)
            if node.right:
                _walk(node.right)

        _walk(new_tree.root)
        return new_tree
    else:
        new_tree.root =Node('Tree is Empty')
        return new_tree

if __name__ == "__main__":
    bt = BinaryTree()
    bt.root = Node(4)
    bt.root.right = Node(9)
    bt.root.left = Node(15)
    bt.root.right.left = Node(6)
    bt.root.left.left = Node(3)
    bt.root.left.right = Node(5)
    print(bt.find_maximum_value())
    print(FizzBuzzTree(bt).breadth_first())
