'''''
    @Author: Rehan
    @Date: 2022-05-30 14:58:30
    @Last Modified by: Rehan
    @Last Modified time: 2022-05-30 18:00:30
    @Title : User Input and Replace String Template “Hello <<UserName>>, How are you?”
    '''


string="Hello <<UserName>>, How are you?"
print(string)
print("Please enter your Name:")
name=str(input())
if len(name)>2:
    print(string.replace("<<UserName>>", name))
else:
    print("Invalid Input")
