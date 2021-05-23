from linked_list  import *



def zipLists(ll1, ll2):
    """
    this function will take tow list and return new one that contain all element from list 1 and list 2
    by order one node from list and one node from list 2
    """
    new_ll=Linkedlist()
    max_len=max(ll1.length,ll2.length)
    ll1_curent=ll1.head
    ll2_curent=ll2.head
    if ll1.length or ll2.length:
        for i in range(max_len):
            if ll1_curent:
                new_ll.append(ll1_curent.value)
                ll1_curent=ll1_curent.next
            if ll2_curent:
                new_ll.append(ll2_curent.value)
                ll2_curent=ll2_curent.next
        print(new_ll.to_string())
        return new_ll
    else:
        return "Sorry invalid input"

l_list = Linkedlist()
l_list.insert(3)
l_list.insert(2)
l_list.insert(1)
l_list.insert(0)
# print(l_list.includes(2))
# print(l_list.includes(0))
# print(l_list.to_string())
# print(l_list.kthFromEnd(0))
# print(l_list.kthFromEnd(5))
# print(l_list.kthFromEnd(3))
# print(l_list.kthFromEnd(4))
# print(l_list.kthFromEnd(10))
l_list2 = Linkedlist()
l_list2.insert(0)
l_list2.insert(1)
l_list2.insert(2)
l_list2.insert(3)
print(l_list.to_string())
print(l_list2.to_string())
zipLists(l_list,l_list2)
