# def msg():
#     val1= int(input("enter first number"))
#     val2=int(input("enter second number"))
#     # print(val1+val2)
#     sum= val1+val2
#     mul= val1*val2
#     sub= val1-val2
#     div= val1/val2
#     return sum,mul,sub,div
    
# res=msg() #calling function
# print("result=",res)

# types of agruments 
# positional agrumnent 
# keyword argumment
# default argument 
# variable length argument/ variable number of arguments



#keyword  argument
# def personalinfo(fname,lname):
#     print("first name",fname)
#     print("last name",lname) 
    
# fname="krish"  #this is keyword argument
# lname="yadav"


# personalinfo(fname,lname)

#default argument

# def cityName(city="adrak"):  #this is the default agrument
#     print("city name",city)

# cityName("nagpur")
# cityName("nagpur")
# cityName()

#variable length argument
# def cityName(*city):
#     print("city name",city)
    
# cityName("m","n","p","n")

# def login():
#     username= input("enter username")
#     password= input("enter pass")
#     if username == password:
#         print("login succesfull")
#     else:
#         print("invalid credentials")

# login()

# mylist = [3,4,5,6,7,5,3,7]

# def searchvalue(target):
#     for i in range(len(mylist)):
#         if mylist[i] == target:
#             return i
#     return -1

# target = 10
# res = searchvalue(target)
# if res != -1:
#     print("value found at index", res)
# else:
#     print("not found")


# def sumofall(mylist):
#     sum=0
#     for i in range(len(mylist)):
#         sum = sum+mylist[i]
#     return sum
# mylist = [3,4,5,6,7,5,3,7]
# res = sumofall(mylist)
# print("sum of arrays ",res)
