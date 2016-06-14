

import math
l=[-10,-5,2,2,2,3,4,7,9,12,13,14]

def magicIndex(list,start,end):
    if end<start or start<0 or end>=len(list):
        return -1
    else:
        midIndex=(start+end)/2
        print(midIndex)
        midIndex1=int(midIndex)
        print (midIndex1)
        midValue=list[midIndex1]
        if list[midValue]==midIndex1:
            return midIndex1

        leftIndex= min(midIndex1-1,midValue)
        left=magicIndex(list,start,leftIndex)
        if left>=0:
            return left

        rightIndex= max(midIndex1+1,midValue)
        right=magicIndex(list,rightIndex,end)
        return right



if __name__ == '__main__':
    magicIndexno=magicIndex(l,0,len(l)-1)
