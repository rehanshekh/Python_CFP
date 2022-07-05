'''
    @Author: Rehan
    @Date: 2022-06-01 01:58:30
    @Last Modified by: Rehan
    @Last Modified time: 2022-06-01 01:47:30
    @Title : Prints the Nth harmonic number: 1/1 + 1/2 + ... + 1/N
    '''
print("Enter the Nth number:")
n=int(input())
sum=0
if n>0:
    for x in range(n+1):
        if x>0:
            sum=sum+(1/x)
        else:
            continue
    print("The sum of Harmonic Series is:",sum)
else:
    print("Invalid Input")