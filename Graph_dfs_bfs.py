def dfs(graph,start):
    path = []
    stack = [start]
    while stack != []:
        v = stack.pop()
        if v not in path:
            path.append(v)
        for w in reversed(graph[v]):
            if w not in path:
                stack.append(w)
    return path

graph = {1: [2, 3],
         2: [1, 4, 5, 6],
         3: [1, 4],
         4: [2, 3, 5],
         5: [2, 4, 6],
         6: [2, 5]}
print(dfs(graph,1))