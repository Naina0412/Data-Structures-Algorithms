def recursive_dfs(graph, start, path=[]):
  '''recursive depth first search from start'''
  path=path+[start]
  for node in graph[start]:
    if not node in path:
      path=recursive_dfs(graph, node, path)
  return path

def iterative_dfs(graph, start, path=[]):
  '''iterative depth first search from start'''
  q=[start]
  print("I'm in first q",q)
  while q:
    print("I'm in while q",q)
    v=q.pop(0)
    if v not in path:
      path=path+[v]
      print("I.m in path",path)
      q=graph[v]+q
      print("Graph of node",graph[v])
      print("I'm in q",q)
      #print(q)
  return path

def iterative_bfs(graph, start, path=[]):
  '''iterative breadth first search from start'''
  q=[start]
  while q:
    v=q.pop(0)
    if not v in path:
      path=path+[v]
      q=q+graph[v]
      print("I'm in q",q)
  return path

'''
   +---- A
   |   /   \
   |  B--D--C
   |   \ | /
   +---- E
'''
graph = {'A':['B','C'],'B':['D','E'],'C':['D','E'],'D':['E'],'E':['A']}
print ('recursive dfs ', recursive_dfs(graph, 'A'))
print ('iterative dfs ', iterative_dfs(graph, 'A'))
print ('iterative bfs ', iterative_bfs(graph, 'A'))
