""" 
Title                   : Calculating Near Misses for Farmet's Theorm
Name of File            :
External files created  :None
External files used     :None
Programer Name          : Sai Pradeep Vure, Sharath Chandra Dondlapally
Email Address           : SaiPradeepVure@lewisu.edu, SharathChandraDond@lewisu.edu
Course & Section Number : SU22-CPSC-60500-001 & 002
Date                    :
Explanation             :
                        This program takes the value of n & k and finds the pair  of x , y ,z 
                        for which relative error is minimum by following the Farmet's Theorm
Resources               :
                        https://www.programiz.com/python-programming/modules/math
                        https://people.math.harvard.edu/~elkies/ferm.html
"""

""" Math is a standerd module in python.We have to import this 
#module to use mathematical functions like power, floor etc. """
import math

""" Sys is also a module.This module provides access to some 
#variables and functions that interact  with the interpreter. """
import sys


""" function -1
    Name : powerOf
    INPUT: 
            x -- integer
            n -- integer
    OUTPUT: 
            return the n'th power of x
    Discription :
        This function calculate the nth power of the input varble x 
"""  
def powerOf(x,n):
    # calculating and returning the nth power of x
    return math.pow(x,n)


""" function -2
    Name : calculateError
    INPUT: 
        rootOfSum - integer
    OUTPUT: 
            return the actual error
    Discription :
        This function calculate actual error for 
        given nth root of sum of power(n,x) and power(n,y)
"""  
def calculateError(rootOfSum):

    # calculating ceil or upper value or z +1
    z_plus1 = math.ceil(rootOfSum)
    # calculating floor value or z
    z = math.floor(rootOfSum)

    # miss for z
    nearMissZ = rootOfSum - z
    # miss for z+1
    nearMissZ_Plus1 = z_plus1 - rootOfSum

    # if miss of z+1 is grater then miss of z then we will use miss of z   
    if(nearMissZ_Plus1 > nearMissZ):
        return nearMissZ
    else:
        return nearMissZ_Plus1

""" function -3
    Name : main
    INPUT: None
    OUTPUT: None
    Discription :
        This function prompt the user to enter value of n and k 
        and call other functions to calculate relative error
""" 
def main():
    # initializing relError and sum to max value using maxsize 
    relError = sys.maxsize
    sum = sys.maxsize

    # prompting user to enter value of n and k
    n = int(input("Enter the value of n (the power to use in the equation) :"))
    k = int(input("Enter the value of k(k>10) :"))

    # outer loopt interate x from 10 to k
    for x in range(10,k+1):
        #ested loop to iterate y from 10 to k
        for y in range(10,k+1):
            # calculating sum of x power n and y power n
            sum = powerOf(x,n) + powerOf(y,n)

            # calculating nth root of sum by powerOf function
            rootOfSum = powerOf(sum,1/n)

            # calculating actual error by calling calculateError function 
            curentActualMiss = calculateError(rootOfSum)

            # calculating relative error by dividing it to sum
            currentRelMiss = curentActualMiss/sum

            # if relative error is grater then current relative error 
            # i.e. we have found the new minimum relative error so far
            if(relError>currentRelMiss):
                # assigning relative error to current relative error
                relError = currentRelMiss
                # printing x, y,z
                print("x ={}\ny ={}\nz ={}\n".format(x,y,rootOfSum))
                print("Actual Miss ={}\nRelative Miss ={}\n".format(curentActualMiss,currentRelMiss))

# calling main function
main()



