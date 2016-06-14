#Author: Naina Chaturvedi
#Program : to implement merge sort

class mergeSort:
    #def __init__(self):

    def mergeSortFunc(self,l):

        if len(l)==1:   #Base case if list has only one element
            return 0
        else:
            if len(l)>1:  #If more than one element is present in the list
                #for i in range(len(l)):
             mid=len(l)//2    #Cut the list into two halves
             lefthalf=l[:mid]  #: slicing function (First Half)
             righthalf=l[mid:]  #: slicing function(Second Half)
             print(lefthalf)
             print(righthalf)
             mergeSort.mergeSortFunc(self,lefthalf) # Subsequently left list is halved
             mergeSort.mergeSortFunc(self,righthalf) #Subsequently right list is halved
             #print(mergeSort.mergeSortFunc(self,left))
             #print(mergeSort.mergeSortFunc(self,right))
             i=0
             j=0
             k=0
             newSortedList=[]
             while i<len(lefthalf)and j<len(righthalf):
                if lefthalf[i]<righthalf[j]:
                    l[k]=lefthalf[i]
                    #print(l[k])
                    i=i+1
                elif lefthalf[i]>righthalf[j]:
                     l[k]=righthalf[j]
                     #print[l[k]]
                     j=j+1
                else:
                    if lefthalf[i]==righthalf[j]:
                      l[k]=lefthalf[i]
                      i=i+1
                k=k+1
             while i<len(lefthalf): #Add list left
                 l[k]=lefthalf[i]
                 i=i+1
                 k=k+1
             while j<len(righthalf): #Add list right
                 l[k]=righthalf[j]
                 j=j+1
                 k=k+1
            print(l)
            #p=0
            #s=p+1
            #for i in range(len(l)):
                #if l[p]==l[s]:
                   # temp=l[s]
                   # l[s]=l[s+1]
                #p=p+1
                #s=p+1
            #print(l)




                    #left=[mergeSort.mergeSortFunc(l,start,mid-1)]
                    #mergeSort.mergeProc(left)
                    #right=[mergeSort.mergeSortFunc(l,mid+1,end)]
                    #mergeSort.mergeProc(right)
                    #list2=mergeSort.mergeLists(left)
                    #list3=mergeSort.mergeLists(right)
                    #print(list2+list3)

    #def mergeProc(self,l1):
         #i=0
         #j=i+1
         #for i in range(len(l1)):
            # if l1[i]>l1[j]:
             #    l1[i],l1[j]=l1[j],l1[i]
            # else:
             #    i+=1
             #    j+=1
    #def mergeLists(listlr):
      #  resultList=[]
      #  for i in range(len(listlr)):
       #     resultList.append(listlr[i])
       # return resultList



if __name__=='__main__':
    l=[67,3,2,1,5,6,3,2,5,7,4,2,8]
    mergeSortOb=mergeSort()
    sortStatus=mergeSortOb.mergeSortFunc(l)
    if sortStatus==0:
        print("The list has only one element and its sorted")

    else:
        #for i in range(len(l)):
            print(sortStatus)















