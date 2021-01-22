"""
Tom Ekshtein
CIS 41A Winter 2021
Unit C Take Home Assignment
"""
#Initialization
from math import floor

#First Script - Working with lists
list1=[]
list1.append(1),list1.append(3),list1.append(5)
list2=[1,2,3,4]
list3= list1+list2
print("list3 is:",list1+list2)
print("list3 contains 3:",3 in list3)
count = 0
for i in range(len(list3)):
    if (list3[i]==3):
        count+=1
print("list3 contains",count,"3's")
print("the first index of 3 in list 3 is at position:",list3.index(3))
first3=list3.pop(list3.index(3))
print("first3=",first3)
print("list3 is now:",list3)
list4=sorted(list3)
print("list4 is:",list4)
print("slice of list3 is:",list3[2:5])
print("length of list3 is:",len(list3))
print("max value of list3 is:",max(list3))
list3.sort()
print("Sorted list3 is:",list3)

#Part P
list5=[list1,list2]
print("list5 is:",list5)
list5s=str(list5)
count=0
print("Within list5, there are two lists. List1 and List2.")
for i in range(len(list5[0])):
    if list5[0][i]!=4:
        count+=1
        print("In index[0] (list1) there are no instances of 4.")
        break
    elif list5[0][i]==4:
        print("In index[0] (list1) there are ",count," instances of 4.")
count=0
for i in range(len(list5[1])):
    if list5[1][i]==4:
        count+=1
        print("In index[1] (list2) there is",count, "instance of 4 at position",list5[1].index(4))

print("\n")
#Second Script- Bit Operators
print("Onto the second script")
a=9
b=14
print("Binary of a is:", bin(a))
print("Binary of b is:", bin(b))
def binaryConvert(var):
    mod1=floor(var%2)
    div1=floor(var/2)
    mod2=floor(div1%2)
    div2=floor(div1/2)
    mod3=floor(div2%2)
    div3=floor(div2/2)
    mod4=floor(div3%2)
    total=mod4,mod3,mod2,mod1
    print(var,"converted to binary is:",mod4,mod3,mod2,mod1)
binaryConvert(a)
binaryConvert(b)
placeHolder=1
while placeHolder != 0:  
    binChoice= input("Please select either a (9) or b (14) to convert to binary\n")
    if binChoice== "a" or binChoice== "A":
        binaryConvert(a)
        placeHolder=0
    if binChoice== "b" or binChoice== "B":
        binaryConvert(b)
        placeHolder=0
    else:
        binChoice
        
"""
Execution Results
Script 1:

list3 is: [1, 3, 5, 1, 2, 3, 4]
list3 contains 3: True
list3 contains 2 3's
the first index of 3 in list 3 is at position: 1
first3= 3
list3 is now: [1, 5, 1, 2, 3, 4]
list4 is: [1, 1, 2, 3, 4, 5]
slice of list3 is: [1, 2, 3]
length of list3 is: 6
max value of list3 is: 5
Sorted list3 is: [1, 1, 2, 3, 4, 5]
list5 is: [[1, 3, 5], [1, 2, 3, 4]]
Within list5, there are two lists. List1 and List2.
In index[0] (list1) there are no instances of 4.
In index[1] (list2) there is 1 instance of 4 at position 3



Script 2:

Onto the second script
Binary of a is: 0b1001
Binary of b is: 0b1110
9 converted to binary is: 1 0 0 1
14 converted to binary is: 1 1 1 0
Please select either a (9) or b (14) to convert to binary
A
9 converted to binary is: 1 0 0 1
Onto the second script
Binary of a is: 0b1001
Binary of b is: 0b1110
9 converted to binary is: 1 0 0 1
14 converted to binary is: 1 1 1 0
Please select either a (9) or b (14) to convert to binary
a
9 converted to binary is: 1 0 0 1
Onto the second script
Binary of a is: 0b1001
Binary of b is: 0b1110
9 converted to binary is: 1 0 0 1
14 converted to binary is: 1 1 1 0
Please select either a (9) or b (14) to convert to binary
B
14 converted to binary is: 1 1 1 0
Onto the second script
Binary of a is: 0b1001
Binary of b is: 0b1110
9 converted to binary is: 1 0 0 1
14 converted to binary is: 1 1 1 0
Please select either a (9) or b (14) to convert to binary
b
14 converted to binary is: 1 1 1 0
Onto the second script
Binary of a is: 0b1001
Binary of b is: 0b1110
9 converted to binary is: 1 0 0 1
14 converted to binary is: 1 1 1 0
Please select either a (9) or b (14) to convert to binary
c
Please select either a (9) or b (14) to convert to binary
b
14 converted to binary is: 1 1 1 0
"""
