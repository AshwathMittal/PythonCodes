# f = open("File1.txt", "w")
# f.write("Hello, world!")
# f.write("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")
# d = f.read()
# f.close()
# print(d)

# with open("File1.txt", "r") as f:
#     d = f.read()
#     print(d)


#
# d = f.read()
# d = d.strip('\n').split()
#
# m = a.read()
# m = m.strip('\n').split()
# words = []
# for i in d:
#     words.append(i) #Appending to make a single list
# for i in m:
#     words.append(i)
# print(f"{words}")
#
# unique = words
#
# for i in unique:
#     if i in d:
#         unique.remove(i)
# print(unique)



# for i in c_1:
#     if i not in words:
#         words.append(i)

# print(words)
# print(c_2)
# for i in c_2:
#     if i not in words:
#         words.append(i)
# words.sort()
# print()
f= open("File1.txt", "r")
a= open("File2.txt", "r")
c_1 = f.read().strip("\n").lower().split()
c_2 = a.read().strip("\n").lower().split()
words = set()
for i in c_2:
    words.add(i)
for i in c_1:
    words.add(i)
print(words)
# print(f.read())


# for i in range(0, 4):
#     u = input('Enter Username: ')
#     p = input('Enter Password: ')
#
#     z = u + "," +  p
#
#     f.write(f'{z}, \n')

# print(f.readlines())


