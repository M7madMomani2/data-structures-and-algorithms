class Node:
    def __init__(self, value):
        self.value = value
        self.right = None
        self.left = None

class BinaryTree:
    def __init__(self):
        self.root = None
        self.maxVal = 0


    def pre_order(self):
        output = []

        def _walk(node):
            output.append(node.value)
            if node.left:
                _walk(node.left)
            if node.right:
                _walk(node.right)

        _walk(self.root)
        return output


    def in_order(self):
        output = []

        def _walk(node):
            if node.left:
                _walk(node.left)

            output.append(node.value)

            if node.right:
                _walk(node.right)

        _walk(self.root)
        return output


    def post_order(self):
        output = []

        def _walk(node):
            if node.left:
                _walk(node.left)
            if node.right:
                _walk(node.right)

            output.append(node.value)

        _walk(self.root)
        return output

    def find_maximum_value(self, tree):

        def _walk(node):
            if self.maxVal < node.value:
                self.maxVal = node.value

            if node.left:
                _walk(node.left)
            if node.right:
                _walk(node.right)

        _walk(self.root)
        return self.maxVal

    def breadth_first(self, tree):
        temp = []
        results = []

        if self.root:
            temp.append(self.root)

            while temp:
                node = temp.pop()
                results.append(node.value)

                if node.left:
                    temp.append(node.left)
                if node.right:
                    temp.append(node.right)
            return results
        else:
            return 'Empty'



class BinarySearchTree(BinaryTree):
    def __init__(self):
        self.root = None
        self.maxVal = 0



    def add(self, value):
        if not self.root:
            self.root = Node(value)

        else:
            def _walk(node):
                if value < node.value:
                    # go left
                    if not node.left:
                        node.left = Node(value)
                        return
                    else:
                        _walk(node.left)

                else:
                    # go right
                    if not node.right:
                        node.right = Node(value)
                        return
                    else:
                        _walk(node.right)

            _walk(self.root)


    def contains(self, value):
        output = []

        def _walk(node):
            output.append(node.value)
            if node.left:
                _walk(node.left)
            if node.right:
                _walk(node.right)

        _walk(self.root)

        if value in output:
            return True
        else:
            return False



    def breadth_first(self, tree):
        temp = []
        results = []

        if self.root:
            temp.append(self.root)

            while temp:
                node = temp.pop()
                results.append(node.value)

                if node.left:
                    temp.append(node.left)
                if node.right:
                    temp.append(node.right)
            return results
        else:
            return 'Empty'

    def find_maximum_value(self, tree):

        def _walk(node):
            if self.maxVal < node.value:
                self.maxVal = node.value

            if node.left:
                _walk(node.left)
            if node.right:
                _walk(node.right)

        _walk(self.root)
        return self.maxVal
