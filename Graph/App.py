# from Vertex import Vertex
# from Edge import Edge
# from Algorithm import Algorithm
# Implmentation Without Graph Object
# A = Vertex("A")
# B = Vertex("B")
# C = Vertex("C")
# D = Vertex("D")
# E = Vertex("E")

# edge1 = Edge(6, A, C)
# edge2 = Edge(1, A, B)
# edge3 = Edge(2, B, C)
# edge4 = Edge(1, C, D)
# edge5 = Edge(1, D, E)
# edge6 = Edge(5, B, E)



# A.adjacenciesList.append(edge1)
# A.adjacenciesList.append(edge2)
# B.adjacenciesList.append(edge3)
# C.adjacenciesList.append(edge4)
# D.adjacenciesList.append(edge5)
# B.adjacenciesList.append(edge6)

# vertexList = [ A, B, C, D, E]
# algorithm = Algorithm()
# algorithm.calculateShortestPath(vertexList, A)
# algorithm.getShortestPathTo(E)

from Graph import Graph

graph = Graph()
VertexNames = ["A","B","C","D","E"]
for vertex in VertexNames:
    graph.addVertex(vertex)
Edges = []
graph.addEdge(6, "A", "C")
graph.addEdge(1, "A", "B")
graph.addEdge(2, "B", "C")
graph.addEdge(1, "C", "D")
graph.addEdge(1, "D", "E")
graph.addEdge(5, "B", "E")
graph.calculateShortestPath(graph.VertexList, graph.getVertex("A"))
graph.getShortestPathTo(graph.getVertex("E"))
