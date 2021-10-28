a = 0
b = 1
sum = 0
count = 1
print("Fibonacci Series: ", end = " ")
while count<int(input("Number: ")):
  print(sum, end = " ")
  count += 1
  a = b
  b = sum
  sum = a + b