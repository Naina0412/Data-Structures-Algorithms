
#Author : Naina Chaturvedi
#Program : Child,Steps and no of ways to run the stairs

#class stairCase:
#def __init__(self,noOfSteps):
#self.noOfSteps=noOfSteps
def calculateNoOfWays(noOfSteps):

        if noOfSteps < 0:
            return -1
        elif noOfSteps==0:
            return 1
        else:
            #while noOfSteps>=1:
             return (calculateNoOfWays(noOfSteps-1)+ calculateNoOfWays(noOfSteps-2)+ calculateNoOfWays(noOfSteps-3))


if __name__ == '__main__':
  #noOfSteps=stairCase()
  no=10
  for i in range(no):
   noOfStep=calculateNoOfWays(i)
  print(noOfStep)


