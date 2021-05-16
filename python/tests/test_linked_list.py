from Data_Structures.linked_list.linked_list import *
from Data_Structures.linked_list import *
import pytest
def test_instance():
    linked_list_ob = Linkedlist()
    assert isinstance(linked_list_ob, Linkedlist)



def test_insert(linked_list_ob):
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



def test_includes(linked_list_ob):

    assert linked_list_ob.includes(0)
    assert linked_list_ob.includes(1)
    assert not linked_list_ob.includes(4)



def test_to_string(linked_list_ob):

    actual = linked_list_ob.to_string()
    expected = f' { {0} } -> { {3} } -> { {2} } -> { {1} } -> NULL'
    assert actual == expected

def test_append(linked_list_ob):
    linked_list_ob.append(111)
    assert linked_list_ob.to_string() == f' { {0} } -> { {3} } -> { {2} } -> { {1} } -> { {111} } -> NULL'

def test_insert_before(linked_list_ob):
    linked_list_ob.insertBefore(2,222)
    assert linked_list_ob.to_string() == f' { {0} } -> { {3} } -> { {222} } -> { {2} } -> { {1} } -> NULL'

def test_insert_after(linked_list_ob):
    linked_list_ob.insertAfter(3,333)
    assert linked_list_ob.to_string() == f' { {0} } -> { {3} } -> { {333} } -> { {2} } -> { {1} } -> NULL'


@pytest.fixture
def linked_list_ob():
    linked_list_o=Linkedlist()
    linked_list_o.insert(1)
    linked_list_o.insert(2)
    linked_list_o.insert(3)
    linked_list_o.insert(0)
    return linked_list_o

