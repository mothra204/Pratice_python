# #String
# a = "this is  a strings"
# b=len('this is not a string dau dcm m')
# print(a)
# print(b)
# print(a[5:])


# # function
# c = 'Hello World'
# print(c.split())

#.format
# a = 'this {} '.format('is')
# print(a)
# a = 'this {a} {b} {c}'.format(a = 'is' , b ='a', c= 'format')
# print(a)

################ value:width.percisionf
# b = 0.129454645835634
# c =  'number = {:1.3f}'.format(b)
# print(c)

################ f format
# name = 'tien'
# c = f'her name is {name}'
# print(c)

############## list 
# name  = ["nam",7,90]
# name.append('lol')
# a = name.pop(0)
# can't contain string and int  only str or int same type
# b = name.sort()
# print(name)
# print(a)
# print(b)

############### dictionaries
# my_dict = {'key1' : 'value1', 'key2' : 'value2'}
#print(my_dict['key2'])

# d = {'key1 ': 'value1' , 'k1':[1,2,3], 'k2':{'k3': 'bla bla'}}
# print(d['k2']['k3'])

############## I/O file
# from os import write


# f = open('my_file.txt','w')
# f.write('im writing this file \n for the first time')
# f.close

# f = open('my_file.txt','r')
#print(f.readlines())

############## For
# list = [1,2,3,4]
# # for i in list:
# #     print(i)

# for num in list:
#     if num %2 ==0:
#         print(f'good number:{num}')
#     else:
#         print(f'odd number:{num}')

# mylsit = [Myvariable for Myvariable in range(1,10) if Myvariable%2==0]
# print(mylsit)

# list1 = [1.4 , 6.4 , 8.6 , 5.9]
# list2  = [((8/2)*temp +10) for temp in list1]


# print(list2)

# mylist = [Myvariable*y for Myvariable in [1,6,7] for y in [1,10,100]]

# for Myvariable in [1,3,6]:
#     for y in [1,10,100]:
#         mylist.append(Myvariable*y)
# print(mylist)

################## split
# st = 'Print only the words that start with s in this sentence'

# for i in st.split():
#     if i[0] == 's':
#         print(i)

################## range()
# for i in range(0,11):
#     print(i)

#################
# list = [i for i in range(1,51) if i%3 ==0]
# print(list)
#################
# st = 'Print every word in this sentence that has an even number of letters'
# for i in st.split():
#     if i == "even":
#         print('even!')

# for i in range(1,101):
#     if i %3 == 0 and i %5 ==0:
#         print('Fizzbuzz')
#     elif i % 3==0:
#             print('Fizz')
#     elif i %5 ==0:
#             print('buzz')
#     else:
#         print(i)

# st = 'Create a list of the first letters of every word in this string'

# list = [i[0] for i in st.split() ]

# print(list)

# def hi(a):
#     print(f'helli {a}')

# result = hi('hi')
# print(result)

# from random import shuffle
# list = ['6','7','2','9']

# # shuffle(list)
# def check_list(mylist):
#     shuffle(mylist)
#     return mylist

# result = check_list(list)
# print(result)

################# new start

################################################### Variables

# fruits = ["apple", "banana", "cherry"]
# x, y, z = fruits
# print(x)
# print(y)
# print(z)

################################################### Random number

# import random
#
# print(random.randrange(1,200))


################################################### List

# get type of list
# thislist = list(("apple", "banana", "cherry"))
# print(type(thislist))


#access list to get data
# thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
# print(thislist[1:4])

# check existing in list
# thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
# if "melon" in thislist:
#     print("yes")
# else:
#     print("no")

# change item into list
# thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
# thislist[1:3] = ["keyboard", "mouse"]
# print(thislist)

# change item less item into list
# thislist = ["apple", "banana", "cherry"]
# thislist[1:3] = ["chuối"]
# print(thislist)

#insert item into list
# thislist = ["apple", "banana", "cherry"]
# thislist.insert(1,"chuối")
# print(thislist)

#append item into list
# thislist = ["apple", "banana", "cherry"]
# thislist.append("orange")
# print(thislist)

#extend list
# thislist = ["apple", "banana", "cherry"]
# tropical = ["mango", "pineapple", "papaya"]
# thislist.extend(tropical)
# print(thislist)

#extend with another datatype (tuple)
# thislist = ["apple", "banana", "cherry"]
# thistuple = ("kiwi", "orange")
# thislist.extend(thistuple)
# print(thislist)

#remove item from the list
# thislist = ["apple", "banana", "cherry","banana"]
# thislist.remove("banana")
# print(thislist)

#remove item specified index
# thislist = ["apple", "banana", "cherry", "banana"]
# thislist.pop()
# print(thislist)

#remove item specified index with DEL
# thislist = ["apple", "banana", "cherry", "banana"]
# del thislist[2]
# print(thislist)

#remove the list with DEL
# thislist = ["apple", "banana", "cherry", "banana"]
# del thislist
# print(thislist)  #this will cause an error because you have succsesfully deleted "thislist".

# clear item in the list
# thislist = ["apple", "banana", "cherry", "banana"]
# thislist.clear()
# print(thislist)

# loop throught the list
thislist = ["apple", "banana", "cherry", "orange"]
for x in thislist:
    print(x)