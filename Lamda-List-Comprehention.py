list_1 = [1,7,3,25,6,4,2]

# y = lambda a,b:a*b  #Type <class 'function'>

# v = y(5)

# print(v)
#
# max = lambda x,y:x if x>y else y
#
# print(max(22,223))
#
# x = list(map(lambda x:x**3, list_1))
#
# print(x)
#
# # Another Way
#
# def cube(x):
#     return x**3
# print(list(map(cube, list_1)))
#
#
# r = [i**2 for i in list_1 if i**2%3==0]
# print(r)
#

d = 'UpperCaseWordddD'

r = [i for i in d if i.isupper()]

print(r)

res = [' Even ' if i %2==0 else ' False ' for i in list_1 ]
print(res)



