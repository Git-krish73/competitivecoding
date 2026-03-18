# i=1
# while i<=6:
#     print(i)
#     i=i+1

# username =" "
# password = " "
# while username != "admin" and password !="hello":
#     username = input("enter username:")
#     password= input("enter password:")
# print("login")

# mycart=[10,20,200,300,800,60,700]
# for i in mycart:
#     if i>400:
#         print("this is my purchased cart item")
#         continue
#     print(i)


# mydict ={
#     101: "krish",
#     102: "yadav",
#     "103": "kr",
#     "104": "yd",
#     101: "as",
#     104: "cd"
# }
# print(mydict)

# a= mydict[102]
# print(a)

# mydict[102]= "peter"
# print(mydict)

# for x in mydict:
#     print(x)
    
# for x in mydict.values():
#     print(x)
    
# for x,y in mydict.item():
#     print(x,y)

# mydict["mobile number"]= "934675"
# print(mydict)

# mydict.pop(101)


#write code to check pallindrom number 

# name=input("enter ")

# if name == name[:: -1]:
#     print("it is palindrome")
# else:
#     print("not plaindrome")

#check anagram

# str1 = "listen"
# str2 = "silent"

# for i in str1:
#     if i in str2:

#nested loop
#pattern
# for i in range(1,4): #outer loop
#     for j in range(1,4): #inner loop
#         print(i,end=" ")
#     print()
    

# n=int(input("enter the no of rows"))
# for i in range(1,n+1):
#     for i in range(1,n+1):
#         print(chr(64+i),end=" ")
#     print()
    
# n=int(input("enter the no of rows"))
# for i in range(1,n+1):
#     for i in range(1,n+1):
#         print(n+1-i,end=" ")
#     print()

# n=int(input("enter the no of rows"))
# for i in range(1,n+1):
#     for i in range(1,1+i):
#         print(i,end=" ")
#     print()



n=int(input("enter the number of students:"))
d={}
for i in range(n):
    name=input("enter student name: ")
    marks=input("enter student marks: ")
    d[name]=marks
while True:
    name=input("enter student name to get makrs: ")
    marks=d.get(name,-1)
    if marks == -1:
        print("student not found: ")
    else:
        print("the marks of",name,"are",marks)
    option=input("do you want to find another student amrks[Yes|NO]")
    if option=="No":
       break
print("thanks for using")



















        



















