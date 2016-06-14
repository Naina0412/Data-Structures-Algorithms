

class seqSearch:
    def __init__(self,no):   #The arguments that you want to pass and initialize
       self.element=no
    def funcSeqSearch(self,l): #List exceptionally passed
        i=0
        found=False            #Status
        #print (self.element)
        #print(l)
        for i in range(len(l)):    # To traverse the list
            #print(l[i])
            if l[i]==self.element:
                found=True
                return i
            else:
                i=i+1
        return found #To show the status always use a flag(either true or false)
if __name__=='__main__':
    l=[3,1,5,7,2,10,6,2]
    numberToSearch=input(print("Enter the no"))#Input gets the input in the form of string not number so you have to cast it
    #print(numberToSearch)
    noSeqSearch=seqSearch(int(numberToSearch))
    foundPosition=noSeqSearch.funcSeqSearch(l)
    if foundPosition==False:
        print("Number not present in the list")
    else:
        print("Postion at which no is found is: ",foundPosition+1)


