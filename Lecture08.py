import datetime, sys, os,random
import math as m
# Math => m

# DateTime
def timedate():
    d = datetime.datetime.now()
    date = d.date()
    time = d.time()
    print(date," ",  time," ", d)

# Sys Module
def sysmodule():
    # Argv => Variable
    print(sys.argv[0])





def osmodule():
    list = os.listdir()
    pylist = [i for i in list if i.endswith(".py")]
    txtlist = [i for i in list if i.endswith(".txt")]
    print(f"Python List: {pylist}  Text File List: {txtlist}")

def randomodule():
    # random.random() #Random Float Number
    d = [45, "hu", 2, 3, 4, "3qeds"]
    # random.uniform(range ) =>  random float number between a given range
    a = random.choice(d)

    random.shuffle(d)
    print(d)
#     random.randint(mumstart, numend)  => Random Integer
randomodule()