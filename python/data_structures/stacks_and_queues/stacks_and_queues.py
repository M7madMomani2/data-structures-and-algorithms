class Node:
    def __init__(self,value) :
        self.value=value
        self.next=None

class Stack:
    def __init__(self) :
        self.top=None

    def push(self,value):
        node =Node(value)
        if self.top:
            node.next = self.top
        self.top = node

    def pop(self):
        try:
            if self.isEmpty():
                raise Exception('Empty Stack')
            else:
                temp = self.top
                self.top = self.top.next
                return temp.value
        except:
            return 'Empty Stack'


    def peek(self):
        try:
            if self.isEmpty():
                raise Exception('Empty Stack')
            else:
                return self.top.value
        except:
            return 'Empty Stack'

    def isEmpty(self):
        if self.top:
            return False
        elif not self.top:
            return True



    def to_string(self):
        current = self.top
        current_string = f" { {current.value} }"

        while current.next:
            current = current.next
            current_string += f" -> { {current.value} }"

        return f"{ current_string } -> NULL"


class Queue:
    def __init__(self):
        self.front = None
        self.rear = None

    def enqueue(self,value):
        node = Node(value)

        if self.isEmpty():
            self.front = node
            self.rear = node

        else:
            self.rear.next = node
            self.rear = node

    def dequeue(self):
        try:
            if self.isEmpty():
                raise Exception('Empty Queue')
            else:
                temp = self.front
                self.front = self.front.next
                return temp.value
        except:
            return 'Empty Queue'

    def peek(self):
        try:
            if self.isEmpty():
                raise Exception('Empty Queue')
            else:
                return self.front.value
        except:
            return 'Empty Queue'

    def isEmpty(self):
        if self.front:
            return False
        elif not self.front:
            return True


    def to_string(self):
        current = self.front
        current_string = f" { {current.value} }"

        while current.next:
            current = current.next
            current_string += f" -> { {current.value} }"

        return f"{ current_string } -> NULL"


stack1 = Stack()
stack1.push(2)
stack1.push(1)
stack1.push(0)
stack1.push(4)
stack1.push(6)
stack1.push(8)
print(stack1.to_string())
stack1.pop()
print(stack1.to_string())
print(stack1.peek())



queue1 = Queue()
queue1.enqueue(2)
queue1.enqueue(1)
queue1.enqueue(0)
queue1.enqueue(4)
queue1.enqueue(6)
queue1.enqueue(8)
print(queue1.to_string())
queue1.dequeue()
print(queue1.to_string())
print(queue1.peek())
