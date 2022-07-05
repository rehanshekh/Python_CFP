'''
    @Author: Rehan
    @Date: 2022-05-30 14:58:30
    @Last Modified by: Rehan
    @Last Modified time: 2022-05-30 18:00:30
    @Title : Flip Coin and print percentage of Heads and Tails
    '''

import random
def flip_coin(n):
    """
        Description:Its a recursive function which uses itself to count of Heads 
        Parameter:It uses the user enter integer
        Return:Return Head Count
    """
    if n<=0:
        return 0
    else:
        r=random.randint(0,1)    
        if r>=0.5:
            count= 1
        else:
            count= 0
        
        return count+ flip_coin(n-1)

print("Enter how many times to flip the coin")
flips=int(input())
if flips>0:
    heads=(flip_coin(flips))
    tails=flips-heads
    print("Heads=",((heads/flips)*100),"%")
    print("Tails=",((tails/flips)*100),"%")
else:
    print("Invalid Input")
