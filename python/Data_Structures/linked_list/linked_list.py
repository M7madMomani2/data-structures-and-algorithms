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

    def append(self,value):
        node = Node(value)
        current = self.head
        while current.next :
            current=current.next
        current.next =node

    def insertAfter(self ,value, newVal) :
        node=Node(newVal)
        if self.head is None:
            self.head = node
        else:
            current = self.head
            while current.next:
                print(current==value)
                if current.value==value:
                    bef_val=current.next
                    current.next =node
                    print(current.next.value)
                    node.next=bef_val
                    return node.value
                current=current.next


    def insertBefore(self,value, newVal):
        new_node = Node(newVal)
        current = self.head
        if current.value == value:
            new_node.next = current
            self.head = new_node
        else:
            while current.next:

                if current.next.value == value:
                    new_node.next = current.next
                    current.next = new_node
                    break
                current = current.next

                if current.next == None:
                    raise Exception("Sorry Couldn't Find The Value")




if __name__ == "__main__":
    l_list = Linkedlist()
    l_list.insert(2)
    l_list.insert(3)
    l_list.insert(0)
    l_list.insert(1)
    l_list.append(15)
    l_list.insertBefore(3, 7)

    print(l_list.includes(2))
    print(l_list.includes(0))
    print(l_list.to_string())


