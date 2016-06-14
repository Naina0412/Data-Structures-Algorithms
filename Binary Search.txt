
#Author : Naina Chaturvedi
#Program : To implement binary Search

class binarySearch:
    def __init__(self,no):
        self.element=no

    def findNumber(self,l,start,end): # No of parameters would be one more than what is passed
        found=False
        if start<0 or end>len(l): # Boundry conditions needs to be checked always
            return 0
        else:

            for i in range(len(l)): #See which condition needs again and again computation so put that under for loop
             mid=(start+end)//2     # for mid to not be float but int use //
             if l[mid]==self.element:
                found=True          #To represent status
                return mid
             else:
                if l[mid]>self.element:  #Evaluate the conditions well if greater than or lesser than
                  end=mid-1

                elif l[mid]<self.element:
                  start=mid+1

        return found              # See the position of return(should be with first if)


if __name__=='__main__':
    l=[3,4,5,6,7,8,9,10,12,13,14]
    start=0
    end=len(l)-1
    noToSearch=int(input("Enter the no you want to search")) #Cast the input since it would be string
    binSearchOb=binarySearch(noToSearch)
    foundStatus=binSearchOb.findNumber(l,start,end) #See the number of parameters to be passed
    if foundStatus==False:
        print("No not found")
    else:
        print("No found at position",foundStatus+1)


