def main(b):
    c = b.split()
    d = []
    for i in c:
        d.append(i[-1::-1])
    print(" ".join(d))