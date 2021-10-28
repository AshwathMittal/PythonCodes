import sys
import time
start_time = time.time()

class cal():
    def __init__(self):
        self.x = int(input("Enter First number: "))
        self.y = int(input("Enter Second number: "))
    def option(self):
        print('[1]: Addition')
        print('[2]: Subtract')
        print('[3]: Divide')
        print('[4]: Multiply')
        print('[5]: Exit')

        c = int(input("Enter Choice: "))

        if c == 1:
            self.op = "+"
        elif c == 2:
            self.op = "-"
        elif c == 3:
            self.op = "/"
        elif c == 4:
            self.op = "*"
        else:
            sys.exit()
    def display(self):
        exp = str(self.x) + self.op + str(self.y)

        res = eval(exp)

        print(f'{self.x} {self.op} {self.y} = {res}')

while True:
    obj = cal()
    obj.option()
    obj.display()
print("--- %s seconds ---" % (time.time() - start_time))
