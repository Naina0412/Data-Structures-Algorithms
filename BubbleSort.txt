
#Author : Naina Chaturvedi
#Program : To implement bubble sort

class bubbleSort:
    def bubbleSortFunc(self,l):
        i=0
        j=i+1
        for i in range(len(l)):
            for j in range(len(l)):
                if l[i]<l[j]:
                    l[i],l[j]=l[j],l[i]
                j=j+1
            i=i+1
        return l

if __name__=='__main__':
    l=[67,1,10,34,2,83,4,5,19,2,23,12,78,6,0]
    bubbleSortOb=bubbleSort()
    sortStatus=bubbleSortOb.bubbleSortFunc(l)
    if sortStatus==0:
        print("The list has only one item and its sorted")
    else :
        print("Sorted List:",sortStatus)








