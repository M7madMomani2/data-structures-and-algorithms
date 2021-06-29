from collections import deque

class Vertex:

    def __init__(self,value):
        self.value = value

    def __str__(self):
        return f"{self.value}"

class Edge:

    def __init__(self,vertex,weight):
        self.vertex = vertex
        self.weight = weight

class Queue():

    def __init__(self):
        self.dq = deque()

    def enqueue(self, value):
        self.dq.appendleft(value)

    def dequeue(self):
        return self.dq.pop()

    def __len__(self):
        return len(self.dq)

class  Graph:

    def __init__(self):
        self.adjacency_list = {}

    def add_node(self,value):
        node = Vertex(value)
        self.adjacency_list[node] = []
        return node

    def add_edge(self,node1=None,node2=None,weight1=0):
        if node1 not in self.adjacency_list:
            raise KeyError
        elif node2 not in self.adjacency_list:
            raise KeyError
        else:
            edge = Edge(vertex=node2,weight=weight1)
            self.adjacency_list[node1].append(edge)
            edge = Edge(vertex=node1,weight=weight1)
            self.adjacency_list[node2].append(edge)

    def get_nodes(self):
       return self.adjacency_list.keys()

    def get_neighbors(self,node):
        return self.adjacency_list.get(node,[])

    def size(self):
        return len(self.adjacency_list)

    def breadth_first(self,node):
        queue = Queue()
        queue.enqueue(node)
        visited  = set()
        visited.add(node)
        node_list = []
        def inner_func(queue,visited,node_list):
            for index in range(len(queue)):
                node = queue.dequeue()
                node_list.append(node)
                neighbors = self.get_neighbors(node)
                for edge in neighbors:
                    if edge.vertex not in visited:
                        queue.enqueue(edge.vertex)
                        visited.add(edge.vertex)
            if len(queue) > 0:
                inner_func(queue,visited,node_list)
        inner_func(queue,visited,node_list)
        return node_list

    #breadth first search
    def bfs(self, start_node):
        nodes=set([])
        temp = [start_node]
        values = []

        while len(temp) >0:
            front_node = temp.pop(0)
            nodes.add(front_node)

            for i in self.adjacency_list.keys():
                if str(i.value) == str(front_node):
                    values.append(self.adjacency_list[i])
                    break

            if len(values) > 0:
                for n in values[0]:
                    if n[1] not in nodes:
                        temp.append(n[1])
                        nodes.add(n[1])
            else:
                return False
        return nodes

    def depth_first(self):
        nodes = self.get_nodes()
        root = None
        for node in nodes:
            root = node
            break
        result = []
        def inner_func(root,result):
            if root not in result:
                result.append(root)
            neighbors = self.get_neighbors(root)
            for edge in neighbors:
                if edge.vertex not in result:
                    result.append(edge.vertex)
                    inner_func(edge.vertex,result)
        if root:
            inner_func(root,result)
        return result

def businessTrip(graph, cityArray) :
    totalCost = 0
    check = False
    for i in range(len(cityArray)-1):
        neighbors = graph.get_neighbors(cityArray[i])
        for j in range(len(neighbors)-1) :
            if (cityArray[i + 1] == neighbors[j].vertex) :
                totalCost += neighbors[j].weight
                check = True

    if (check == False) :
        totalCost = 0
        check = False
        return f'{check}, {totalCost}'

    return f'{check}, {totalCost}'

graph = Graph()
node1 = graph.add_node('a')
node2 = graph.add_node('b')
node3 = graph.add_node('c')
node4 = graph.add_node('d')
node5 = graph.add_node('e')
node6 = graph.add_node('f')
node7 = graph.add_node('g')
node8 = graph.add_node('h')
graph.add_edge(node1,node2)
graph.add_edge(node1,node4)
graph.add_edge(node2,node3)
graph.add_edge(node2,node4)
graph.add_edge(node3,node7)
graph.add_edge(node4,node5)
graph.add_edge(node4,node8)
graph.add_edge(node4,node6)
graph.add_edge(node8,node6)
for node in graph.depth_first():
    print(node.value)
