'''
    @Author: Rehan
    @Date: 2022-06-01 08:58:30
    @Last Modified by: Rehan
    @Last Modified time: 2022-06-01 18:00:30
    @Title : Program to find a year is leap year or not
    '''


year = int(input('Enter the Year:'))
if 999<year<=9999:
    if(year%4==0 and year%100!=0 or year%400==0):
        print("The year is a leap year!")
    else:
        print("The year isn't a leap year!")
else:
    print("Invalid Input")