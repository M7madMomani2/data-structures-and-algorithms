class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def add(self, data):
        node = Node(data)

        if not self.head:
            self.head = node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = node

class Hashtable:
    def __init__(self, size=1024):
        self._buckets = [None]*size
        self.size = size

    def hash(self, key):
        total = 0
        for char in key:
            total += ord(char)
        return total*19 % self.size

    def add(self, key, value):
        Hkey = self.hash(key)

        if self._buckets[Hkey] == None:
            self._buckets[Hkey] = LinkedList()
            self._buckets[Hkey].add([key , value])

        if self.contains(key):
            current = self._buckets[Hkey].head
            while current:
                if current.data[0] == key :
                    current.data[1] = value
                current = current.next

        else:
            self._buckets[Hkey].add([key , value])


    def get(self, key):
        Hkey = self.hash(key)
        if self._buckets[Hkey]:
            current = self._buckets[Hkey].head
            while current:
                if current.data[0] == key :
                    return current.data[1]
                current = current.next
            return 'key not exist'
        else:
            return 'key not exist'

    def contains(self, key):
        Hkey = self.hash(key)
        if self._buckets[Hkey]:
            current = self._buckets[Hkey].head
            while current:
                if current.data[0] == key :
                    return True
                current = current.next
            return False
        else:
            return False

hash_op = Hashtable()
hash_op.add('HI',30)
print(hash_op)
