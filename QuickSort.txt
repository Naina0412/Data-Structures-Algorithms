#Author : Naina Chaturvedi
#Program : To implement Quicksort

class quickSort:
   def quickSortFunc(self,l): #Function calls the helper function which calculates splitpoint
       quickSort.quickSortHelper(self,l,0,len(l)-1)
       return l
   def quickSortHelper(self,l,first,last):
       if len(l)==1:          #if the list has only one element
           return 0
       if first<last:         #the first should be lesser than last
          splitPoint=quickSort.partition(self,l,first,last) #Splitpoint is rightmark
          quickSort.quickSortHelper(self,l,first,splitPoint-1) #Recursively calculate to the left sub list
          quickSort.quickSortHelper(self,l,splitPoint+1,last)  #Recursively caluclate to the right sub list
   def partition(self,l,first,last):
           #i=0
           #c=0
           pivot=l[first]          #Pivot is the first element
           leftmark=first+1        #After the first element which is a pivot next is leftmark
           rightmark=last          #Last element i.e. len(l)-1 is the rightmark
           done=False              #Status to indicate if rightmark is less than leftmark
           while not done:         #Loop till done is true
               while l[leftmark]<=pivot and leftmark<=rightmark: # Till the list start elements and further are lesser than pivot and leftmark is less than or equal to rightmark
                   leftmark+=1      #Increment leftmark
               while l[rightmark]>=pivot and rightmark>=leftmark : #Till the list end elements and backwards are greater than pivot and rightmark is greater than or equal to leftmark
                   rightmark-=1     #Decrement rightmark
               #print(leftmark)
               #print(rightmark)
               #print(pivot)
               if rightmark<leftmark:  #When rightmark is less than leftmark set done as true i.e. all the elements are in their proper order and no exchange is required
                   done=True
               else:
                l[leftmark],l[rightmark]=l[rightmark],l[leftmark] #exchange if the element marked by left and right are inproper order
           l[first],l[rightmark]=l[rightmark],l[first] # if done is set true then exchange the first with rightmark which would act as splitpoint
           return rightmark # return right mark which means this would be your splitpoint

           #if rightmark<=leftmark:
              #splitPoint=rightmark-1
              #print("Splitpoint",splitPoint)
              #print("Split point",l[splitPoint])
              #temp= pivot
              #l[splitPoint],temp=temp,l[splitPoint]
              #l[splitPoint]=temp
                #print(l)
                #l[splitPoint]=
                #print("Pivot",pivot)
               #continue
           #print(l)
if __name__=='__main__':
    l=[67,1,10,34,2,83,4,5,19,2,23,12,78,6,0]
    #l1=[78]
    quickSortOb=quickSort()
    sortStatus=quickSortOb.quickSortFunc(l)
    if sortStatus==0:
        print("List has only one element and its already sorted")
    else :
        print(sortStatus)

