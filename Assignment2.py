

import math
import heapq
import copy

D= 50
R=1024

def getShortestPaths(G, S):

    knownVertices = set()       # double-circle nodes
    knownPaths = {S: []}             # blue tuple
    knownCosts = [(0, S, S)]    # branches

    while len(knownCosts) > 0:
      costV, v, pred = heapq.heappop(knownCosts)
      if v not in knownVertices:
        knownVertices.add(v)
        path = copy.deepcopy(knownPaths[pred])
        path.append(v)
        knownPaths[v] = path
        print ("double-circle:", v, "predecessor:", pred)
        for neigh in G[v].keys():
            heapq.heappush( knownCosts, (costV + G[v][neigh], neigh, v) )

G = { 'A': {'B': 5, 'E': 20},
      'B': {'A': 5, 'C': 10, 'E': 6},
      'C': {'B': 10,'E': 2, 'D': 1},
      'D': {'C': 1, 'E': 15},
      'E': {'A': 20, 'B': 5, 'C': 2, 'D': 15}
}
print("Shortest path from A to D is :")
getShortestPaths(G, 'A')['D']
print("Shortest path from B to D is :")
getShortestPaths(G, 'B')['D']
print("Shortest path from C to D is :")
getShortestPaths(G, 'C')['D']
print("Shortest path from E to D is :")
getShortestPaths(G, 'E')['D']
