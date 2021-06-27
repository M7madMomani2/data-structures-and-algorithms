class Vertex:

    def __init__(self,value):
        self.value = value

    def __str__(self):
        return f"{self.value}"

class Edge:

    def __init__(self,vertex,weight):
        self.vertex = vertex
        self.weight = weight

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
print(graph.size())
