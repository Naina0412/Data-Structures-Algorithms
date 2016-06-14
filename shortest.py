import heapq
import copy

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
        print "double-circle:", v, "predecessor:", pred
        for neigh in G[v].keys():
            heapq.heappush( knownCosts, (costV + G[v][neigh], neigh, v) )


    return knownPaths

G = { 'A': {'B': 5, 'E': 20},
      'B': {'A': 5, 'C': 10, 'E': 6},
      'C': {'B': 10,'E': 2, 'D': 1},
      'D': {'C': 1, 'E': 15},
      'E': {'A': 20, 'B': 5, 'C': 2, 'D': 15}
}

choice=raw_input('Do you want to calculate shortest path:(Enter yes to calculate or no to exit)')
while choice=='y':
    Sr = raw_input('Enter the source node --> ')
    Dt = raw_input('Enter the destination node --> ')
    print getShortestPaths(G,Sr)[Dt]
#else:
     #break

    #ch=raw_input('Do you want to continue?(Enter 1 for Yes or 0 for No ):')
    #if ch==1:

    #else :
    #break


#print "The shortest distance between B to D is :"
#print getShortestPaths(G, 'B')['D']
#print "The shortest distance between C to D is :"
#print getShortestPaths(G, 'C')['D']
#print "The shortest distance between E to D is :"
#print getShortestPaths(G, 'E')['D']


