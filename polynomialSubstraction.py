'''Author : Naina Chaturvedi
  Problem Statement : Program to implement subtraction of two polynomials(poly1-poly2)
  File Name : polynomialSubstraction.py
  Inputs for polynomials are to be given by user
'''

#!/usr/bin/env python

__author__='Naina Chaturvedi'

#Class Poly for Polynomial

class Poly:

    #Function to construct polynomial by construction of terms (use of list's list)

    def polyConstruction(self):

          FullTerm,wholePoly=[],[]
          noOfTerms=int(input("Enter no of terms in the polynomial:"))
          for i in range(noOfTerms):
            coeff=int(input("Enter the coefficient:"))
            varible=input("Enter the variable:")
            power=int(input("Enter the power:"))
            if power <0:
             print("Please enter positive power")
            term=[coeff,varible,power]
            wholePoly.insert(i,[str(term[0])+term[1]+str(term[2])])
          print("Polynomial is : ",end="")
          for i in range(noOfTerms):
           print(wholePoly[i],"+",end="")
          print("\n")
          return wholePoly

    '''Function to substract two polynomials poly1- poly2.
    For loop iterates through the max len of wither ploy1 or poly 2 which ever is greater.
    and then subtract it with corresponding/respective terms having same variables and power.
    If poly2 term has negative coefficient then multiply it with -1
   '''
    def subtractPoly(self,poly1,poly2):
        subrList=[]
        subrList1=[]
        second=False
        i=0
        p=0
        #for i in range(len(poly1)):
        #if poly1[0][i][1]== poly2[0][i][1]:
        #print("Hello",poly1[0][0][0],poly2[0][0][0])
        #print("Hello2",poly1[0][0][1],poly2[0][0][1])
        #print("Hello2",poly1[0][0][2],poly2[0][0][2])
        #print("Hello",poly1[1][0][0],poly2[1][0][0])
        #print("Hello2",poly1[1][0][1],poly2[1][0][1])
        #print("Hello2",poly1[1][0][2],poly2[1][0][2])
        #print(poly1[0][0][0])

        for i in range(len(max(poly1,poly2))):
            for j in range(len(max(poly1,poly2))):
              j=1
              k=2
              if poly1[i][0][j]==poly2[i][0][j] and poly1[i][0][k]==poly2[i][0][k]:

                  if (int(poly2[i][0][0]))< 0:
                   t1= (-1*(int(poly2[i][0][0])))
                   subtract = (int(poly1[i][0][0]))- t1
                  else :
                   subtract = (int(poly1[i][0][0]))-(int(poly2[i][0][0]))

                  subResult= [subtract,poly1[i][0][j],poly1[i][0][k]]
                  subrList.insert(i,[str(subResult[0])+subResult[1]+subResult[2]])

              else:

                  if poly1[i][0][j]== poly2[i][0][j] and poly1[i][0][k]> poly2[i][0][k]:
                   subrList1.insert(i,poly1[i])
                   subrList1.append(poly2[i])
                  else :
                      subrList1.insert(i,poly2[i])
                      subrList1.append(poly1[i])
                  second=True

        i=i+1
        return subrList



'''Main Function : Program execution starts here.
   Object for class Poly is created and then polyConstruction function is called where whole polynomial is constructed
   by construction of individual terms (creation of list's list)
'''
if __name__== '__main__':

      polyOb=Poly()
      print("Enter values for first polynomial")
      poly1=polyOb.polyConstruction()
      print("Enter values for second polynomial")
      poly2=polyOb.polyConstruction()
      subtract=polyOb.subtractPoly(poly1,poly2)
      print("The substraction result is :")
      print(subtract)












