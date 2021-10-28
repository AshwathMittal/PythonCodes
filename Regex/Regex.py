import re
# s = "this is a is string string string 28  80290 203 02-04 abc@mail.com abc@mail.com abc@mail.com abc@mail.com"
#
# a = re.search('\w+@\w+.\w+', s)
# print(a.group())
#
#
#
# # /w => used to read a single character
# # .w
# # \d =>First Numbers (\d+)
# # {int} => Length
#
# b = re.findall('\w+@\w+.\w+', s,flags=re.I)
# print(b)
#
# c = re.sub('\d+','' ,  s)
# print(c)
# '\s+' Multiple Spaces


with open('roll.txt', "r") as f:
    a = f.readlines()

    d = []
    for i in a:
        c = re.search('\d+', i)
        if len(c.group()) == 4:
            d.append(c.group())
    print(d)
