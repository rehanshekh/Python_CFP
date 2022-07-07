'''
    @Author: Rehan
    @Date: 2022-06-02 08:58:30
    @Last Modified by: Rehan
    @Last Modified time: 2022-06-03 18:00:30
    @Title : Program to find the distance of points from origin
    '''

from math import sqrt
from sys import argv
if __name__=='__main__':
    x1=2
    y1=2
    print("Enter the value for x, should be an integer")
    x=int(input())
    print("Enter the value for y, should be an integer")
    y=int(input())
    if x!=0 and y!=0:
        distance = sqrt(pow(x,x1)+pow(y,y1))
        print("The distance of points from origin is:",distance)
    else:
        print("Enter a valid input")    