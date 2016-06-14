
class stack:
    def __init__(self):
        self.stacky=[]
        #self.top=-1

    def push(self,value):
        print(value)
        return self.stacky.append(value)

    def pop(self):
        data=self.stacky.pop()
        return data


    def isEmpty(self):
        for i in range(len(self.stacky)):
         if self.stacky[i]==[]:
            return True

def revString(mystring):
        staky1=stack()
        for i in mystring:
            #print(i)
            print(staky1.push(i))
            #return data

#s=stack()
mystring1="NainaVinay"
#l=s.isEmpty()
#list1=[]
#print(l)
#for i in mystring1:
   #print(i)
   #print("Push mode",s.push(i))
   #list1.append(chr)
   #print (list1)
revString(mystring1)




#s.push(12)
#s.push(13)
#d1=s.pop()
#print(d1)
#d2=s.pop()
#print(d2)


