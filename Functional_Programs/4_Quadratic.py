'''
    @Author: Rehan
    @Date: 2022-05-31 08:58:30
    @Last Modified by: Rehan
    @Last Modified time: 2022-05-31 18:00:30
    @Title : Program to find the roots of the equation a*x*x + b*x + c
    '''

from math import sqrt

print("Enter the value for a:")
a=int(input())
print("Enter the value for b:")
b=int(input())
print("Enter the value for c:")
c=int(input())
delta=(b*b)-(4*a*c)
x1=(-b+sqrt(delta))/(2*a)
x2=(-b-sqrt(delta))/(2*a)
print("The two roots are",x1,"and",x2)