'''
To Avoid Crashing Our Program we have Excpetion Handling
We Handle Excepting using "try" & "except" block
For Example
'''
a = [2,3,5]
try:
    print(a[4]) #Here The Index is out of range
except Exception as exp: #Displaying InBUilt Exception Message
    print(exp)
# ------------ 2nd Example --------------------------
try:
    b = "python"
    b[0] = 'k'
except Exception as exp:
    print(exp)
# Else Will only be executed if try block is successful
else:
    b.replace("p", "k")
finally: 
    print(a)
