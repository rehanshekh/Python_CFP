'''
    @Author: Rehan
    @Date: 2022-06-02 14:58:30
    @Last Modified by: Rehan
    @Last Modified time: 2022-06-02 14:47:30
    @Title : Program to find distinct tripets whose sum is 0
    '''
    

if __name__=='__main__':
    a=print("Enter the single digit integer followed by space N many times:")
    a=str(input())
    list1=[]
    new=''
    sign=''
    for x in a:
        
        if x=="-":
            sign='-'
            continue
        elif x==' ':
            continue
        else:
            if sign=="-":
                x=sign+x
                sign=''
            new=x
            list1.append(new)
    result=False
    count=0
    index=0
    for x in range(len(list1)-2):
            for y in range(x+1,len(list1)-1):
                for z in range(y+1,len(list1)):
                    if (int(list1[x])+int(list1[y])+int(list1[z])==0):
                        result=True
                        count=count+1
                        print("The distant triplets are:")
                        print(list1[x],list1[y],list1[z])
    print("Number of distant triplets found:",count)
    if result==False:
        print("Integers making a sum of zero doesn't exist")

