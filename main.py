# x = 1
# y = 2
#
# i = x >0 and y<2
# print(i)
# # False
#
# i = x >0 or y<2
# print(i)
# True


# a = ["hello", 1, 9, 3.10]
# print(type(a))
#
# # [IndexStrat:IndexStop]
# print(a[:-3:-1])
# a[0] = 10
# print(a)

# print(a[::-1])
# c = a.reverse()
# print(c)
#
# b = a[::-1] == c
# print(b)

# print(a[-1:-4:-1])

# def lol():
#  print("Smh")
# lol()

# a = "Hello World"
# a = a.split(" ")
# print(a)

# b = "Hello World, Welcome to Python"
#
# c = b.split()
# d = []
# for i in c:
#     print(i)
#     d.append(i[-1::-1])
# print(" ".join(d))

# x = "python python is great python"
#
# print(x.count("python"))
#
# z = x.split()
#
# for i in z:
#     print(i, z.count(i))
# from collections import Counter
#
# c = Counter(x)
#
# s = list(c.items())
#
# print(s[-1])


# str = " Hello "
#
# str = str.replace("H", "K")
#
# str = str.strip()
# print(str)

# d = {
#     "name": 'john',
#     "marks": 0
# }
#
# print(d['name'])
# print(d.get("name"))

# ad = {
#     "JOhn": {
#         "marks": {
#             "Maths": 45,
#             "Engilsh": 47,
#             "Science": 49
#         }
#     }
# }

# print(ad["JOhn"]["marks"]["Maths"])


#
# s = 'This is a string'
#
# d = s.split()
# d.reverse()
#
# print(" ".join(d))
#
# print(" ".join(s.split()[::-1]))

# a = {"name": "xyz", "marks": "22"}
#
# for i in a:
#     print(i, ":", a[i])


# print("True" if True else "False")

# Dictionary {Key: Value}

# a = [2,4,54,46,"Hello",53,"World", "!"]

# for j in a:
#     if isinstance(j,int):
#         print(j)
#     else:
#         pass
# print("\n")
# for j in a:
#     if isinstance(j,int):
#         print(j)
#     else:
#         continue

# d = input("Number: ")
# # c = 0
# # for i in d:
# #     i = int(i)
# #     c = c + i
# # print(c)
#
# c = []
#
# for i in d:
#     i = int(i)
#     c.append(i)
# print(sum(c))

# d = [1,4,2,4,1,5,54, 1,4,2,4]
#
# c = 0
# n = 4
# for i in d:
#     if i ==n:
#         print(f"Index of {i}:{c}")
#     c = c +1

# print("%s %d"%("name", 7))





# v = {}
#
# # v["username"] = "100"
# v["username"] = 100
#
# print(v)

# student={"St1":[20,80,90,99],
# "St2":[90,95,50,79],
# "St3":[90,99,90,89],
# "St4":[66,93,98,95]
# }
# sumnum = []
# for i in student.values():
#     a = sum(i)
#     sumnum.append(a)
# print(sumnum)

#
# x = 121
# print(str(x)[::-1] == str(x))
# nums1 = [1, 2, 3, 4]
# nums2 = []
# num_list = nums1 + nums2
# num_list.sort()
# length = len(num_list)
#
# if length % 2 == 1:
#     print("f",  num_list[length // 2])
# else:
#     len2 = length // 2 - 1
#     print(len2)
#     a = num_list[length // 2] +  num_list[len2]
#     print(a/2)

