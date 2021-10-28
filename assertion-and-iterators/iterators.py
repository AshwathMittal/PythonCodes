'''
We Use iterator to access one element at a time
Example:
'''

a = [2,3,4, 5]

b = iter(a) # Use iter to creat an iterable object

print(next(b)) #It will return First[0] Element
print(next(b)) #It will return Second[1] Element
print(next(b)) #It will return THird[2] Element
print(next(b)) #It will return Fourth[3] Element
# print(next(b)) #It will return Error as No elements to iterate

#-----------------------Another Case --------------------
c = [2,5,6,8,9]
for i in c:
    print(i)
print(next(c)) # Will give error again as the iteration has ended
# ------------