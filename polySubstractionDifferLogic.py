'''Author : Naina Chaturvedi
  Problem Statement : Program to implement subtraction of two polynomials(poly1-poly4)
  File Name : polySubstractionDifferLogic.py
  Inputs for polynomials are written in main function
  The polynomials P1 and P4 can be equal in length or of any length.In this case P1=25x^9+3x^2 and P4=3x^9+5x^3-13x^1
  x^0 means 1
'''

#!/usr/bin/env python

'''Function to substract two polynomials poly1- poly4.
   Compare the length of two polynomials,if poly1 length is greater than poly2 then insert poly1 in resultPoly first
   and then subtract it with corresponding/respective terms having same variables and power.
   If poly2 term has negative coefficient then call minusCoeff function below and multiply it with -1
   '''
def subtractPoly(poly1,poly2):
    list1=[]
    if len(poly1) > len(poly2):
        resultPoly = [i for i in poly1]
        for i in range(len(poly2)):
         resultPoly[i] -= poly2[i]
    else:
        resultPoly = [i for i in poly2]
        for i in range(len(poly1)):
            if poly1[i]<0:           #If the coefficient of the term is negative , multiply it by -1
                #(-1*(poly1[i]))
                minusCoeff(poly1[i])
                resultPoly[i] -= poly1[i]
            else:
                resultPoly[i] -= poly1[i]
            list1= minusCoeff(resultPoly)
        return  list1
    return resultPoly

def minusCoeff(p):
    return [-1*pi for pi in p]

#Function to add two polynomials poly1+poly2(if user wants to add to two polynomials please uncomment below below add fucntion)
'''
def add(poly1,poly2):

     if len(poly1) > len(poly2):
        resultPoly = [i for i in poly1]
        for i in range(len(poly2)):
         resultPoly[i] += poly2[i]
     else:
        resultPoly = [i for i in poly2]
        for i in range(len(poly1)):
         resultPoly[i] += poly1[i]
     return resultPoly
'''

''' A polynomial is represented as arbitrary no of terms where a term means coefficient,variable and its power (coefficient*variable^power)
    joined by +/- operator i.e 10x^6 + 7x^5 - 3x^4 - 2x^2 + 4x1 + 1x0 is a polynomial
    This function is to form polynomial from all the terms'''

def polyFormation(polFormed,x):
    coeffOpString = []
    for i in range(len(polFormed)-1,0,-1):   #range(start,stop,step) , here I'm starting from last element to first with step -1
        if polFormed[i]:
            if i < len(polFormed)-1:
                if polFormed[i] >= 0:
                 coeffOpString.append('+')
                else:
                 coeffOpString.append('-')
                coeffOpString.append(termFormation(abs(polFormed[i]),i,x))
            else:
                coeffOpString.append(termFormation(polFormed[i],i,x))
    return ' '.join(coeffOpString)           # To join the Coefficient with the operators +/-

''' A polynomial term is represented as coefficient,variable and its power (coefficient*variable^power)
    This function is to form a term of polynomial'''

def termFormation(coeff,h,x):

    if h == 1:                       # h represents no of items in the polynomial list
        if coeff == 1: return 'x^%d'%(x)    # if there is only single term
        elif coeff == -1: return '-x^%d'%(x) # if there is negative coefficient in a single term
        return "%sx^%d" % (coeff,x )       #return coeff and variable x
    elif h>1:
        if coeff == 1: return 'x^%d'%x
        elif coeff == -1: return '-x^%d'%x
        return "%sx^%d" % (coeff,x)   # if there is a coefficient with a power
    return "%s" % coeff

'''Main Function: Program execution starts here.
   The result of the subtraction is stored in string i.e.term1,term2,term3,term4,term5 and then displayed.
   The polynomials P1 and P4 can be equal in length or of any length.In this case P1=25x^9+3x^2 and P4=3x^9+5x^3-13x^1
   string[::] means its string slicing : to show full string / writing only string name will also do rather than slicing
   '''
if __name__ == '__main__':
 term1=(polyFormation(subtractPoly([1,25],[1,3]),9))
 term2=(polyFormation(subtractPoly([1,0],[1,5]),3))
 term3=(polyFormation(subtractPoly([1,3],[1,0]),2))
 term4=(polyFormation(subtractPoly([1,0],[1,-13]),1))
 terms=[term1,term2,term3,term4]
 print ("\n")
 for i in range(len(terms)):
     print("Final Result term %d:"%(i+1),terms[i])
'''
 print ("Final Result term One : " ,term1[::])
 print ("Final Result term Two : " ,term2[::])
 print ("Final Result term Three : " ,term3[::])
 print ("Final Result term Four : : " ,term4[::])
 print ("Final Result term Five : " ,term5[::])
'''
resultSubtraction= "("+term1+")"+"+"+"("+term2+")"+"+"+"("+term3+")"+"+"+"("+term4+")"
print("The subtraction of two polynomials(P1-P4): ",resultSubtraction)
