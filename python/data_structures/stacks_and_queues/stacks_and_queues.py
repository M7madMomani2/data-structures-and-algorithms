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
        else:
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
        else :
            return True


    def to_string(self):
        current = self.front
        current_string = f" { {current.value} }"

        while current.next:
            current = current.next
            current_string += f" -> { {current.value} }"

        return f"{ current_string } -> NULL"

class PseudoQueue:
  def __init__(self, node = None):
    self.rear = Stack()
    self.front = Stack()

  def enqueue(self, data):
      self.rear.push(data)


  def dequeue(self):
    if self.rear.isEmpty():
        raise Exception('Empty Stack')
    else:
        while not self.rear.isEmpty():
            popped = self.rear.pop()
            self.front.push(popped)
        target = self.front.pop()
        if self.rear.isEmpty():
            while not self.front.isEmpty():
                    self.rear.push(self.front.pop())
        return target




if __name__ == "__main__":
    pseudo = PseudoQueue()
    pseudo.enqueue(1)
    pseudo.enqueue(2)
    pseudo.enqueue(3)
    pseudo.enqueue(4)
    print('peeked: ', pseudo.front.top.value)
    print('value popped: ', pseudo.dequeue())


