'''
    @Author: Rehan
    @Date: 2022-06-01 01:58:30
    @Last Modified by: Rehan
    @Last Modified time: 2022-06-01 01:58:30
    @Title : This program takes a command-line argument and prints a table of the powers of 2 
    '''

from sys import argv
power=1
if 0<=int(argv[1])<31:
    print("The table for power of 2:")
    while power<int(argv[1]):
        print(2**power)
        power=power+1
else:
    print("Please Enter a proper command line input")