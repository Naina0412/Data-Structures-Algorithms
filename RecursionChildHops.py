
def Staircase(steps):
    prev=0
    curr=1
    if steps==0:
        return 0
    else :
        for i in range(steps):
            temp=curr
            curr=prev+steps
            prev=temp
            return curr
if __name__ == '__main__':
    no=Staircase(2)
    print(no)



