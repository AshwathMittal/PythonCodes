import sys


class Login:
    balance = 0
    user_info = {}
    def screen(self):
        print("[1]Create Account")
        print("[2]Login")
        print("[3]Exit")
        ch = int(input("Enter Choice: "))
        return ch


    def login(self):
        u = input("UserName: ")
        p = input("PassWord: ")
        log  = self.user_info
        if u in log:
            if p == log[u]:
                # print("Login Successfull")
                return True
            else:
                print("Password Is Incorrect")
        else:
            print("User Not Fond")

    def create_acc(self):
        u = input("UserName: ")
        p = input("PassWord: ")
        log  = self.user_info
        log[u] = p

    def main_screen(self):
        print('[1]Deposit')
        print('[2]Withdraw')
        print('[3]Check balance')
        print('[4]Exit')
        ch = int(input("Enter Choice: "))
        return ch


    def deposit(self):

        a = int(input("Enter Amount To Deposit: "))
        self.balance = self.balance + a
        return self.balance

    def withdraw(self):

        a = int(input("Enter Amount To Withdraw: "))
        self.balance = self.balance - a
        return self.balance

    def balance_check(self):
        print(f"The Balance Is {self.balance}")

log = Login()

while True:
    k = log.screen()
    if k ==1:
        # print(deposit())
        log.create_acc()
    elif k ==2:
        n = log.login()
        if n == True:
            while True:
                z = log.main_screen()
                if z ==1:
                    # print(deposit())
                    log.deposit()
                elif z ==2:
                    print(log.withdraw())
                elif z ==3:
                    log.balance_check()
                elif z ==4:
                    break
    elif k ==3:
        sys.exit()