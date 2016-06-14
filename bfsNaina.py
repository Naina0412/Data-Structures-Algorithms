
class Queue:
    def __init__(self):
        self.queue=[]
    def enqueue(self,item):
        return self.queue.append(item)
    def dequeue (self):
        return self.queue.pop(0)
    def __str__(self):
        return self.queue
    def isempty(self):
        return self.queue==[]
class BFS:
    def calculateBfs(self,start,finish,Graph):
        parents={}
        q=Queue()
        q.enqueue(start)
        parents[start]=None

        while(not q.isempty()):
            p=q.dequeue()
            parents[0]=p
            for neighbour in Graph[p]:
                parents[neighbour]=neighbour
                q.enqueue(parents)
        print(parents)

if __name__=='__main__':
    Graph = {'A':['B','C'],
             'B':['A','D'],
             'C':['A','D'],
             'D':['B','C']
             }
    bfsOb=BFS()
    bfsOb.calculateBfs('A','D',Graph)