'''
    @Author: Rehan
    @Date: 2022-06-01 01:58:30
    @Last Modified by: Rehan
    @Last Modified time: 2022-06-01 01:58:30
    @Title : Computes the prime factorization of a number using brute force 
    '''

def primeFactors(n):
	"""
	Description:Its a recursive function which uses itself to count of Heads 
    Parameter:It uses the user enter integer
    Return:Return Head Count
	"""
	c = 2
	while(n > 1):
		if(n % c == 0):
			print(c, end=" ")
			n=n/c
		else:
			c=c+1

print("Enter a number of which prime factors are to be found:")
n = int(input())
primeFactors(n)
