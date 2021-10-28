import random
num = []
frequency = {}
for i in range(0,100):
    num.append(random.randint(1, 10))
for i in num:
    frequency[i] = num.count(i)
print(frequency)