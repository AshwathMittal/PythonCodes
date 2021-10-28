# z = [2,6,2,' ',8,]
# for i,v in enumerate(z):
#     print(v, ":",i)
#


def count(let):
    l = 0
    u = 0
    for i in let:
        if i.islower():
            l = l +1

        elif i.isupper():
            u = u +1
    return f"UpperCase Letters: {u}, LowerCase Letters: {l}"
print(count("PyThON"))