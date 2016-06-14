__author__ = 'Naina'



class Queue():
    def __init__(self):
        self.queue=[]

    def enqueue(self,item):
        self.queue.append(item)

    def dequeue(self):
        return self.queue.pop(0)

    def __str__(self):
        return str(self.queue)

    def empty(self):
        return self.queue==[]

def bfs(start,finish,Graph):
    parents={}
    q=Queue()
    q.enqueue(start)
    parents[start.name]=None

    while(not q.empty()):
        node=q.dequeue()
        for neighbour in node.neighbours:
            n=neighbour.name

            if n not in parents:
                parents[n]=node.name
                if n==finish.name:
                    return parents
                q.enqueue(Graph[neighbour.name])

    return parents


def getPath(start,finish,parents):
    finish=finish.name
    path=[finish]
    if finish in parents:
        node=parents[finish]
        while(node!=start.name):
            path.append(node)
            node=parents[node]
    else:
        "No Path "

    path.append(start.name)

    return path[::-1]


