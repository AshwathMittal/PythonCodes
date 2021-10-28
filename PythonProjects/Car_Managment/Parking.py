import sys
import csv
import datetime

def main():
    print("[1]: Add Car Info")
    print("[2]: Display All Cars Info")
    print("[3]: Check Out")
    print("[4] Exit")

    return int(input("Enter Choice: "))



def add_detail():
    no = input("Enter Car Number: ")
    model = input("Enter Car Model: ")
    date = datetime.datetime.now()
    f = open("Car.csv", "a")
    d = [no,model,date]
    obj = csv.writer(f)
    obj.writerow(d)

def display_all():
    f = open("Car.csv", "r")
    obj = csv.reader(f)
    obj = list(obj)
    print("Number\tModel\tDate Added")
    for i in obj:
        if len(i) > 0:
            print(f"{i[0]}\t{i[1]}\t{i[2]}")

def check_out():
    f = open("Car.csv", "r")
    obj = csv.reader(f)
    obj = list(obj)

    search = input('Enter Car No: ')
    for i in obj:
        if search in i:
            print("Number\tModel\tDate Added")
            print(f"{i[0]}\t{i[1]}\t{i[2]}")


while True:
    k = main()

    if k == 1:
        add_detail()
    elif k == 2:
        display_all()
    elif k == 3:
        check_out()
    else:
        sys.exit()