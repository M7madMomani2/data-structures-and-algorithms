class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Linkedlist:
    def __init__(self):
        self.head = None

    def insert(self, val):
        node = Node(val)

        if self.head == None:
            self.head = node

        else:
            node.next = self.head
            self.head = node
        return node.value

    def includes(self, value):
        current = self.head
        while current.next:
            if current.value == value:
                return True

            current = current.next
            if current.value == value:
                return True

        return False

    def to_string(self):
        current = self.head
        current_string = f" { {current.value} }"

        while current.next:
            current = current.next
            current_string += f" -> { {current.value} }"

        return f"{ current_string } -> NULL"

if __name__ == "__main__":
    l_list = Linkedlist()
    l_list.insert(2)
    l_list.insert(3)
    l_list.insert(0)
    l_list.insert(1)
    print(l_list.includes(2))
    print(l_list.includes(0))
    print(l_list.to_string())
