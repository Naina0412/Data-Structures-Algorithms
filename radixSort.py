#Author : Naina Chaturvedi
#Program : To implement radix sort

class radixSort:
    def radixSortFunc(self,l):
        if len(l)==1:
         return 0
        else:
            Radix=10
            a=0
            maxLength=False
            tmp,placement=-1,1
            while not maxLength:
                maxLength=True
                bucket=[list() for _ in range(Radix)]
                print(bucket)
                for i in l:
                  #tmp=i/placement
                  ins=tmp%Radix
                  ins//=placement
                  bucket[ins].append(i)
                #Radix*=10
                #placement*=10
                if maxLength and tmp>0:
                   maxLength=False
                for b in range( Radix ):
                   buck = bucket[b]
                for i in buck:
                    l[a] = i
                    a += 1
                placement *= Radix
        return l

if __name__=='__main__':
    l=[67,1,10,34,2,83,4,5,19,2,23,12,78,6,0]
    radixSortOb=radixSort()
    sortStatus=radixSortOb.radixSortFunc(l)
    if sortStatus==0:
        print ("The list contains only one element and is sorted")
    else:
        print("Sorted List:",sortStatus)
