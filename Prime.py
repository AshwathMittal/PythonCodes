c = 0
num = 3
for i in range(1, num+1):
    if num%i == 0:
        c = c +1

print("Prime" if c==2 else "Composite")

f = []
for a in range(5, 200):
     c = 0

     for k in range(1, a+1):
         if a%k ==0:
             c = c+1
     if c ==2:
        f.append(a)
print(f)