
def fun(x):
        l = []
        for i in range(x):
                l.append(lambda x, y=i: y + x)
        return l

l = fun()
for f in l:
        print fun()

if __name__ == '__main__':
    print fun(3)
