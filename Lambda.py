m = [2,3,4,5,6,7,8,4,2,1,4,]

y =list(filter(lambda  x:True if x%2==0 else False, m))
print(y)