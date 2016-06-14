
graph={'A':['B','C'],
       'B':['A','D'],
       'C':['A','D','E'],
       'E':['C','D'],
       'F':[],
       'H':[]}

def add_edges(graph):
    edges=[]
    for start in graph:
        for neighbour in graph[start]:
            edges.append((start,neighbour))
    return edges

def isolated_node(graph):
    isolatedNode=[]
    while(graph):
     for start in graph:
        #if(graph[start]== []):
        if not graph[start]:
            isolatedNode+=start
     return isolatedNode

print(add_edges(graph))
print(isolated_node(graph))

class Graph(object):
    def __init__(self,graph_dict={}):
        self._graphDict=graph_dict

    def vertices(self):
        return(list(self._graphDict.keys()))

    def edges(self):
        return self._generateEdges()

    def add_vertex(self,vertex):
        if vertex not in self._graphDict:
            self._graphDict[vertex]=[]

    def add_edge(self,edges):
        edge=set(edges)
        print("Print set of edges",edge)
        (vertex1,vertex2)=tuple(edge)
        print((vertex1,vertex2))
        if vertex1 in self._graphDict:
            self._graphDict[vertex1].append(vertex2)
        else :
            self._graphDict[vertex1]=[vertex2]

    def _generateEdges(self):
      edges=[]
      for vertex in self._graphDict:
          for neighbour in self._graphDict[vertex]:
              if {neighbour, vertex} not in edges:
                    edges.append({vertex, neighbour})
      return edges

    def findpath(self,vertex1,vertex2):
        path=[]
        graph=self._graphDict
        path=path+ [vertex1]
        if vertex1==vertex2:
            return path
        if vertex1 not in graph:
            return None
        for vertex in graph[vertex1]:
            if vertex not in path:
                extended_path=self.findpath(vertex1,vertex2)
                if extended_path:
                    return extended_path
        return None


        if self._generateEdges():
            path+=self._generateEdges()
            return path
        else:
            print("No path")

if __name__ == "__main__":
    graph={'A':['B','C'],
       'B':['A','D'],
       'C':['A','D','E'],
       'E':['C','D'],
       'F':[],
       'H':[]}

graph1=Graph(graph)

print("Vertices of graph:")
print(graph1.vertices())

print("Edges of graph:")
print(graph1.edges())

print("Add vertex:")
graph1.add_vertex("z")

print("Vertices of graph:")
print(graph1.vertices())

print("Add an edge:")
graph1.add_edge({"a","z"})

print("Vertices of graph:")
print(graph1.vertices())

print("Edges of graph:")
print(graph1.edges())

print('Adding an edge {"x","y"} with new vertices:')
graph1.add_edge({"x","y"})
print("Vertices of graph:")
print(graph1.vertices())
print("Edges of graph:")
print(graph1.edges())
print("Find Path")
print(graph1.findpath('A','B'))

