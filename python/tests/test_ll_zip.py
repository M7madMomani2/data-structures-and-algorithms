import pytest
from Data_Structures.linked_list.ll_zip import *
from Data_Structures.linked_list.linked_list import *

def test_zipLists(linked_list_ob,linked_list_ob2):

    actual_output1 =linked_list_ob.zipLists(linked_list_ob2).to_string()
    expected_output1=" {0} -> {1} -> {3} -> {2} -> {2} -> {3} -> {1} -> {0} -> NULL"
    assert actual_output1== expected_output1
    linked_list_ob2.insert(5)
    actual_output2 =linked_list_ob.zipLists(linked_list_ob2).to_string()
    expected_output2=" {0} -> {5} -> {3} -> {1} -> {2} -> {2} -> {1} -> {3} -> {0} -> NULL"
    assert actual_output2== expected_output2




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
