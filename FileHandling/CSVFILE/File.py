import csv

d = [["xyz", 12], ["qw", 23], ["Soething", 32]]

f = open("file.csv", "r+")

obj = csv.writer(f)

for i in d:
    obj.writerow(i)


p= list(csv.reader(f))

print(p)

f.close()