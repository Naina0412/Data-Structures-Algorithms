

tree=['a',
      ['b',
      ['d',[],[]],
       ['e',[],[]]],
      ['c',
      ['f',[],[]]]
      ]

#print(tree)
#print(tree[1])
#print(tree[0])
#print(tree[2])
def binaryT(r):
       return [r,[],[]]
def getRoot(root):
        return root[0]
def setRoot(root,newValue):
        root[0]=newValue
def getLeftchild(root):
        return root[1]
def getRightchild(root):
        return root[2]

def insertLeft(root,newBranch):
        t = root.pop(1)
        if len(t)>1:
            root.insert(1,[newBranch,t,[]])
        else:
            root.insert(1,[newBranch,[],[]])
        return root
def insertRight(root,newBranch):
        t = root.pop(2)
        if len(t)>1:
            root.insert(2,[newBranch,[],t])
        else:
            root.insert(2,[newBranch,[],[]])
        return root
r=binaryT(3)
insertLeft(r,4)
insertRight(r,5)
insertLeft(r,6)
insertRight(r,9)
print(r)
l=getLeftchild(r)
print(l)
r=getRightchild(r)
print(r)
setRoot(r,12)



