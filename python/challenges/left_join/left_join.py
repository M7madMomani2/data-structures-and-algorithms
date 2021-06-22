from data_structures.hashtable.hashtable import Hashtable,Node,LinkedList

def left_join(hash1,hash2):

    hash_list = []
    for i in hash1._buckets:
        if i != None:
            current = i.head
            while current:
                hash_list += [[current.data[0], current.data[1]],]
                current = current.next

    for i in hash_list:

        if hash2.contains(i[0]) == True:
            val = hash2.get(i[0])
            i.append(val)
        else:
            i.append(None)

    return hash_list


test = Hashtable(1024)
test.add('fond', '1')
test.add('wrath', '2')
test.add('diligent', '3')
test2 = Hashtable(1024)
test2.add('fond', '3')
test2.add('wrath', '2')
test2.add('diligent', '1')

print(left_join(test,test2))
