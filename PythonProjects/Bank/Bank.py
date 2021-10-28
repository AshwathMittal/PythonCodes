import sys
import sqlite3
con = sqlite3.connect("Bank_Data.db")

c = con.cursor()

c.execute("CREATE TABLE if not exists record (username text,password text, balance text)")

c.execute("insert into record values ('test','test', 'test')")

con.commit()
con.close()

log={
}
# log_screen()

def log_screen():
    print("[1]Create Account")
    print("[2]Login")
    print("[3]Exit")

    try:
        ch = int(input("Enter Choice: "))
        return ch
    except:
        return 3
def login():
    u = input("UserName: ")
    p = input("PassWord: ")

    if u in log:
        if p == log[u]:
            # print("Login Successfull")
            return True
        else:
            print("Password Is Incorrect")
    else:
        print("User Not Fond")


def create_acc():
    u = input("UserName: ")
    p = input("PassWord: ")
    
    if u in log:
        create_acc()
    else:
        log[u] = p
#
def main_screen():
    print('[1]Deposit')
    print('[2]Withdraw')
    print('[3]Check balance')
    print('[4]Exit')
    
    try:
        ch = int(input("Enter Choice: "))
        return ch
    except:
        return 4
b = 0

def deposit():
    global b
    a = int(input("Enter Amount To Deposit: "))
    b = b + a
    return b


def withdraw():
    global b
    a = int(input("Enter Amount To Withdraw: "))
    b = b - a
    return b

def balance():
    print(f"The Balance Is {b}")

while True:
    k = log_screen()
    if k ==1:
        # print(deposit())
        create_acc()
    elif k ==2:
        n = login()   
        if n == True:
            while True:
                z = main_screen()
                if z ==1:
                    # print(deposit())
                    deposit()
                elif z ==2:
                    print(withdraw())    
                elif z ==3:
                    balance()
                elif z ==4:
                    sys.exit()
    elif k ==3:
        sys.exit()
