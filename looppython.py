

lyst=[5,3,6,1]


#j=i+1


def swap(lyst,i,j):
    temp=lyst[i]
    lyst[i]= lyst[j]
    lyst[j]=temp
    print("A")

def selectionsort(lyst):
 i=0
 j=i+1
 while i<len(lyst)-1:
    minterm=lyst[i]
    print("AB")
    j=j+1
    while j<len(lyst):
        if lyst[j]<lyst[i]:
            minterm=j
        j=j+1
    if minterm != lyst[i]:
      swap(lyst,minterm,i)
    i=i+1
selectionsort(lyst)
print(lyst)





