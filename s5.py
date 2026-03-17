# # def func(value, values):
# #     var=1
# #     values[0]= 44
# # t=3
# # v=[1,2,3]
# # func(t,v)
# # print(t,v[0])

# # fruit_list1=['apple','berry','cherry','papaya']
# # fruit_list2= fruit_list1
# # fruit_list3=fruit_list1[:]
# # fruit_list2[0]='guava'
# # fruit_list3[1]='kiwi'

# # sum=0
# # for ls in(fruit_list1,fruit_list2,fruit_list3):
# #     if ls[0] == 'guava':
# #         sum+=1
# #     if ls[1]=='kiwi':
# #         sum+=20
# # print(sum)

# # list=[5,2,7,2]
# # list.sort()
# # print(list[-2])

# # remove duplicate
# # list=[5,2,7,2]
# # new_list=[]
# # for i in list:
# #     if i not in 


# # myset={1,2,"krish",5.66,"rahul","ramesh","ankit",1}
# # print(myset)

# # # myset.add(60)
# # # print(myset)

# # # myset.discard(3)
# # # print(myset)

# # myset.remove(3)
# # print(myset)

# # myset={10,20,30,40}
# # yourset={"krish","yadav"}
# # newset=myset.union(yourset)
# # print(newset)

# #intersection return common element

# # myset={10,20,30,40}
# # yorset={10,50,60,30}
# # print(myset.intersection(yorset))


# # list=[3,2,3,1,2,4]
# # newlist= set(list)
# # print(newlist)


# #move zeros to the left

# list=[0,1,0,2,3]
# for i in list:
#     if i == 0:
#         list.remove(i)
#         list.append(i)
# print(list)

#find intersection of three arrays:

list1=[1,2,4]
list2=[4,5,6]
list3=[8,9,4]
for i in list1:
    if i in list2 and i in list3:
        print(i)
