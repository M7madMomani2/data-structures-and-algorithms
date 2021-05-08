from Data_Structures.linked_list.linked_list import *
from Data_Structures.linked_list import *

def test_instance():
    linked_list_ob = Linkedlist()
    assert isinstance(linked_list_ob, Linkedlist)



def test_insert():
    linked_list_ob=Linkedlist()
    linked_list_ob.insert(1)
    linked_list_ob.insert(2)
    linked_list_ob.insert(3)
    linked_list_ob.insert(0)

    l_list_result1 =linked_list_ob.head.value
    l_list_result2 =linked_list_ob.head.next.value
    l_list_result3 =linked_list_ob.head.next.next.value
    l_list_result4 =linked_list_ob.head.next.next.next.value


    exOutput1 = 0
    exOutput2 = 3
    exOutput3 = 2
    exOutput4 = 1



    assert l_list_result1==exOutput1
    assert l_list_result2==exOutput2
    assert l_list_result3==exOutput3
    assert l_list_result4==exOutput4

def test_includes():
    linked_list_ob=Linkedlist()
    linked_list_ob.insert(1)
    linked_list_ob.insert(2)
    linked_list_ob.insert(3)
    linked_list_ob.insert(0)

    assert linked_list_ob.includes(0)
    assert linked_list_ob.includes(1)
    assert not linked_list_ob.includes(4)

def test_to_string():
    linked_list_ob=Linkedlist()
    linked_list_ob.insert(1)
    linked_list_ob.insert(2)
    linked_list_ob.insert(3)
    linked_list_ob.insert(0)

    actual = linked_list_ob.to_string()
    expected = f' { {0} } -> { {3} } -> { {2} } -> { {1} } -> NULL'
    assert actual == expected
