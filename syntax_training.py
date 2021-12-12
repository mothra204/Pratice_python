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

# mylsit = [x for x in range(1,10) if x%2==0]
# print(mylsit)

# list1 = [1.4 , 6.4 , 8.6 , 5.9]
# list2  = [((8/2)*temp +10) for temp in list1]


# print(list2)

mylist = [x*y for x in [1,6,7] for y in [1,10,100]]

# for x in [1,3,6]:
#     for y in [1,10,100]:
#         mylist.append(x*y)
print(mylist)