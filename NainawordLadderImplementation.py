
__author__='Naina Chaturvedi'
#Program : To build word Ladder for two given words

from bfs2 import Queue,bfs,getPath
import sys

class Node:
    def __init__(self,name):
        self.name=name
        self.neighbours=[]

    __slots__=('name','neighbours')

    def __str__(self):
        result=self.name+':'
        for n in self.neighbours:
            result+=n.name+','
        return result[:-1]

class BuildGraph:
    def buildGraph(self,file1):
        w={}
        f=open(file1)
        words=f.read().split('\n')

        for word in words:
            for i in range(len(word)):
                wrd=word[:i]+'_'+word[i+1:]
                if wrd in w:
                    w[wrd].append(word)
                else :
                    w[wrd]= [word]
        for key in w:
            wordlist=w[key]
            for word1 in wordlist:
                for word2 in wordlist:
                    if word1!=word2:
                     BuildGraph.inputGraph(word1,word2)

    def inputGraph(self,word1,word2):

        if word1 not in Graph:
            node=Node(word1)
            node.neighbours.append(Node(word2))
            Graph[word1]=node
        else:
            neighbours=Graph[word1].neighbours
            if word2 not in [x.name for x in neighbours]:
                neighbours.append(Node(word2))

        if word2 not in Graph:
            node=Node(word2)
            node.neighbours.append(Node(word1))
            Graph[word2]=node
        else:
            neighbours=Graph[word2].neighbours
            if word1 not in [x.name for x in neighbours]:
                neighbours.append(Node(word1))


if __name__=='main':

    Graph={}
    file="words"
    BuildGraphOb=BuildGraph()
    BuildGraphOb.buildGraph(file)

    word1='fool'
    word2='sage'

    if word1 in Graph:
        start=Graph[word1]
        if word2 in Graph:
            finish=Graph[word2]
            predecessors = bfs(start, finish, Graph)
            path = getPath(start, finish, predecessors)
            str = ''

            for p in path:

                str += p + ' -> '

            print (str[:-3])


        else:
             print("Word2 not in Graph")


    else:
        print("Word1 not in Graph")











