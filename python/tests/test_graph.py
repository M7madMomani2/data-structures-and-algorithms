import pytest
from data_structures.graph.graph import *

def test_add_node():
    expected = 'a'
    graph = Graph()
    actual = graph.add_node('a').value
    assert actual == expected

def test_add_edge_exists():
    graph = Graph()
    node_a = graph.add_node('a')
    node_b = graph.add_node('b')
    graph.add_edge(node_a,node_b)
    expected = ['b',0]
    edge = graph.adjacency_list[node_a][0]
    actual = [edge.vertex.value,edge.weight]
    assert actual == expected

def test_add_edge_does_not_exists():
    with pytest.raises(KeyError):
        graph = Graph()
        node_a = graph.add_node('a')
        node_b = Vertex('b')
        graph.add_edge(node_a,node_b)

def test_get_nodes(graph):
    expected = ['a', 'b', 'c', 'd', 'e', 'f']
    nodes = graph.get_nodes()
    actual = []
    for node in nodes:
        actual.append(node.value)
    assert actual == expected

def test_get_neighbors(graph):
    expected = ['c', ['a', 0], ['b', 0], ['e', 0]]
    nodes = graph.get_nodes()
    for node in nodes:
        if node.value == 'c':
            node_c = node
    neighbors = graph.get_neighbors(node_c)
    actual = [node_c.value]
    for edge in neighbors:
        actual += [[edge.vertex.value,edge.weight]]
    assert actual == expected

def test_get_size(graph):
    expected = 6
    actual = graph.size()
    assert actual == expected

def test_empty_graph():
    graph = Graph()
    actual = graph.get_nodes()
    assert not actual
def test_business_trip():
    graph = Graph()
    node1 = graph.add_node('1')
    node2 = graph.add_node('2')
    node6 = graph.add_node('3')
    node3 = graph.add_node('4')
    node4 = graph.add_node('5')
    node5 = graph.add_node('6')
    graph.add_edge(node1,node6)
    graph.add_edge(node1,node3)
    graph.add_edge(node2,node6)
    graph.add_edge(node2,node5)
    graph.add_edge(node6,node4)
    graph.add_edge(node3 ,node4)
    graph.add_edge(node4,node5)
    actual= (businessTrip(graph,[node1,node6 ]))
    assert  actual=="True, 0"

@pytest.fixture
def graph_test():
    test1 = Graph()
    test1.add_node('a')
    test1.add_node('b')
    test1.add_node('c')
    test1.add_node('d')
    test1.add_node('x')
    test1.add_edge('a','b',4)
    test1.add_edge('a','d',9)
    test1.add_edge('a','c',3)
    test1.add_edge('b','a',4)
    test1.add_edge('c','a',3)
    test1.add_edge('c','d',6)
    test1.add_edge('d','a',9)
    test1.add_edge('d','b',5)
    test1.add_edge('d','c',6)

    return test1
@pytest.fixture
def graph():
    graph = Graph()
    node_a = graph.add_node('a')
    node_b = graph.add_node('b')
    node_c = graph.add_node('c')
    node_d = graph.add_node('d')
    node_e = graph.add_node('e')
    node_f = graph.add_node('f')
    graph.add_edge(node_a,node_c)
    graph.add_edge(node_a,node_d)
    graph.add_edge(node_b,node_c)
    graph.add_edge(node_b,node_f)
    graph.add_edge(node_c,node_e)
    graph.add_edge(node_d ,node_e)
    graph.add_edge(node_e,node_f)
    return graph

@pytest.fixture
def graph_weight():
    graph = Graph()
    node_a = graph.add_node('a')
    node_b = graph.add_node('b')
    node_c = graph.add_node('c')
    node_d = graph.add_node('d')
    node_e = graph.add_node('e')
    node_f = graph.add_node('f')
    graph.add_edge(node_a,node_c,1)
    graph.add_edge(node_a,node_d,3)
    graph.add_edge(node_b,node_c,5)
    graph.add_edge(node_b,node_f,7)
    graph.add_edge(node_c,node_e,9)
    graph.add_edge(node_d ,node_e,8)
    graph.add_edge(node_e,node_f,4)
    return
