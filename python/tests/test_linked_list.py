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


def test_kthFromEnd(linked_list_ob):
    actual_output1 =linked_list_ob.kthFromEnd(3)
    actual_output2=linked_list_ob.kthFromEnd(0)
    actual_output3 =linked_list_ob.kthFromEnd(10)
    expected_output1 = 0
    expected_output2 = 1
    expected_output3 = False
    assert actual_output1 == expected_output1
    assert actual_output2 == expected_output2
    assert actual_output3 == expected_output3


def test_zipLists(linked_list_ob,linked_list_ob2):

    actual_output1 =linked_list_ob.zipLists(linked_list_ob2).to_string()
    expected_output1=" {0} -> {1} -> {3} -> {2} -> {2} -> {3} -> {1} -> {0} -> NULL"
    assert actual_output1== expected_output1
    linked_list_ob2.insert(5)
    actual_output2 =linked_list_ob.zipLists(linked_list_ob2).to_string()
    expected_output2=" {0} -> {5} -> {3} -> {1} -> {2} -> {2} -> {1} -> {3} -> {0} -> NULL"
    assert actual_output2== expected_output2


    print(actual_output1)
    # print()


@pytest.fixture
def linked_list_ob():
    linked_list_o=Linkedlist()
    linked_list_o.insert(1)
    linked_list_o.insert(2)
    linked_list_o.insert(3)
    linked_list_o.insert(0)
    return linked_list_o

@pytest.fixture
def linked_list_ob2():
    linked_list_o2=Linkedlist()
    linked_list_o2.insert(0)
    linked_list_o2.insert(3)
    linked_list_o2.insert(2)
    linked_list_o2.insert(1)
    return linked_list_o2
