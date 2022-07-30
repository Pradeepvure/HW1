Title                   : Calculating Near Misses for Farmet's Theorm
Name of File            :
External files created  :None
External files used     :None
Programer Name          :
Email Address           :
Course & Section Number :
Date                    :
Explanation             :
                        This program takes the value of n & k and finds the pair  of x , y ,z 
                        for which relative error is minimum by following the Farmet's Theorm
Resources               :
                        https://www.programiz.com/python-programming/modules/math
                        https://people.math.harvard.edu/~elkies/ferm.html


This HW1 assignment is about to write a program that an interactive user search 
for "near misses" of the form (x,y,z,n,k) int the formula 
power(x,n) + power(y,n) = power(z,n) where x,y,z,n,k are positive integers
where 2<n<12 ,
10<=x,y<=k

FlowChart :
1) Prompt the user to enter the value of n and k
2) Find near misses of the form --->> power(x,n) + power(y,n) <> power(z,n)
3) print x,y,z,actual miss and relative miss whenever we find a minimum relative miss


Function Used:
1)  Name : powerOf
    INPUT: 
            x -- integer
            n -- integer
    OUTPUT: 
            return the n'th power of x
    Discription :
        This function calculate the nth power of the input varble x 

2)  Name : calculateError
    INPUT: 
        rootOfSum - integer
    OUTPUT: 
            return the actual error
    Discription :
        This function calculate actual error for 
        given nth root of sum of power(n,x) and power(n,y)

3)  Name : main
    INPUT: None
    OUTPUT: None
    Discription :
        This function prompt the user to enter value of n and k 
        and call other functions to calculate relative error
!----------------------

to use this repository use: 
git clone https://github.com/Pradeepvure/HW1.git
