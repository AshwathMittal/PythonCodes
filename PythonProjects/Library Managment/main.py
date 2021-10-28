import sys
class lib:
    def screen(self):
        print("[1]: Add Book Details")
        print("[2]: Display all Books")
        print("[3]: Search for a book")
        # Delete
        # Update
        print("[4]: Exit")

        return int(input("Enter Choice: "))
    def add(self):
        id = int(input("Enter Book ID: "))
        name = input("Enter Book Name: ")
        pages = int(input("Enter Number Of Pages In The Book: "))

        f = open("Info.txt", "a")
        f.write(f"{str(id)},{name},{str(pages)} \n")

        f.close()

        self.info = {}
        f = open("Info.txt", "r")
        d = f.readlines()
        f.close()


        for i in d:
            i = i.strip("\n").split(',')
            # print(i)
            self.info[i[0]] = i[1:]
        # self.info

    def display(self):
        data = self.info
        print('id\tname\tPages')
        for i in data:
            print(f'{i}\t{data[i][0]}\t{data[i][1]}')


    def search(self):
        data = self.info

        id = input("Book ID: ")
        if id in data:
            print('id\tname\tPages')
            print(f"{id}\t{data[id][0]}\t{data[id][1]}")
        else:
            print("Not Found")

obj = lib()
while True:
    k = obj.screen()
    if k == 1:
        obj.add()
    elif k == 2:
        obj.display()
    elif k == 3:
        obj.search()
    else:
        sys.exit()