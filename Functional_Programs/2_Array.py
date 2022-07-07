'''
    @Author: Rehan
    @Date: 2022-06-03 14:58:30
    @Last Modified by: Rehan
    @Last Modified time: 2022-06-03 14:47:30
    @Title : Program to 2 dimensional array in memory to read in M rows and N cols
    '''

if __name__=='__main__':
    print("Enter number of rows")
    rows=int(input())
    print("Enter the number of columns")
    col=int(input())
    arr=[[0 for x in range(col)] for y in range(rows)]
    b=0
    print("The resulting array is:")
    for z in arr:
        for a in z:
            a=a+b
            print(a,end=' ')
            b=b+1
        print()