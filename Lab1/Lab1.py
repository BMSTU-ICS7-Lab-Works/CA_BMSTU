from math import *
import numpy
'''
cos(pi*2/x) - lab1
x^3 - x^2 - Lab1_2
Lab1 but more nodes - Lab1_3
'''

def f(x):
    return x * x


def readfile(datax, datay):
    f = open('Lab1.txt', 'r')
    linecount = 0
    for line in f:
        linecount += 1
        line = line.split()
        datax.append(float(line[0]))
        datay.append(float(line[1]))
    return linecount


def table(datax, datay):
    print('-' * 21)
    print('|    x    |    y    |')
    print('-' * 21)
    for i in range(nodelen):
        print('|{0:7.3f}  |{1:7.3f}  |'.format(datax[i], datay[i]))


def findpos(datax, datay, x, nodenum):
    global left, right
    left = 0
    right = 0
    for i in range(nodelen - 1):
        if datax[i] <= x <= datax[i + 1] or datax[i] >= x >= datax[i + 1]:
            if i + nodenum / 2 > nodelen - 1:
                right = nodelen - 1 - i
                left = nodenum - right
                return i
            if i - nodenum / 2 < 0:
                left = i + 1
                right = nodenum - left
                return i
            left = nodenum // 2
            right = nodenum - left
            return i
        '''
        
        elif datax[nodelen - 1] < x and datax[0] < x:
            left = nodenum
            return nodelen - 1
        elif datax[nodelen - 1] > x and datax[0] > x:
            right = nodenum
            return 0
            '''
    return -2


def defroot(datax, datay, ind, x):
    nodesx = []
    nodesy = []
    #print(ind, left, right)
    if ind != -1:
        for i in range(ind - left + 1, ind + right + 1, 1):
            nodesx.append(datax[i])
            nodesy.append(datay[i])
    # print(nodesx, nodesy)
    k = 1
    pn = nodesy[0]
    multi = x - nodesx[0]
    while (len(nodesy) > 1):
        for i in range(len(nodesy) - 1):
            nodesy[i] = (nodesy[i] - nodesy[i + 1]) / (nodesx[i] - nodesx[i + k])
        nodesy.pop()
        pn += multi * nodesy[0]
        multi *= (x - nodesx[k])
        k += 1
    return pn

def menu():
    print("MENU:\n1. Task 1\n2. Task 2\n3. Task 3\n4. Enter interval and write f(x) in def\n5. Exit")

datax = []
datay = []
left = 0
right = 0
while 1:
    menu()
    choice = int(input("Make your choice: "))
    if choice == 1:
        x = float(input('Введите x для нахождения y: '))
        nodenum = int(input("Введите количество узлов n: "))
        ind = findpos(datax, datay, x, nodenum + 1)
        if ind != -1:
            pn = defroot(datax, datay, ind, x)
            print('Pn = {0:.3f}'.format(pn))
    if choice == 2:
        eps = 1e-9
        for i in range(nodelen - 1):
            if datay[i] <= 0 <= datay[i + 1] or datay[i] >= 0 >= datay[i + 1]:
                s = datax[i]
                e = datax[i + 1]
                break
        sval = defroot(datax, datay, findpos(datax, datay, s, nodelen), s)
        eval = defroot(datax, datay, findpos(datax, datay, e, nodelen), e)
        if sval * eval < 0:
            while 1:
                mid = (s + e) / 2
                midval = defroot(datax, datay, findpos(datax, datay, mid, nodelen), mid)
                # print(midval)
                if abs(midval) < eps:
                    print("Root was found it is: {0:.3f}".format(mid))
                    break
                elif midval * sval < 0:
                    eval = midval
                    e = mid
                elif midval * eval < 0:
                    sval = midval
                    s = mid
        else:
            print("Введены неверные значения начала и конца")
    if choice == 3:
        print("Reverse interpolation: ")
        ny = int(input("Enter n for y: "))
        print('The answer is: {0:.3f}'.format(defroot(datay, datax, findpos(datay, datax, 0, ny), 0)))
    if choice == 4:
        nodelen = 0
        l = float(input("Enter left end of interval: "))
        r = float(input("Enter right end of interval: "))
        step = float(input("Enter step: "))
        datax = []
        datay = []
        for i in numpy.arange(l, r, step):
            datax.append(i)
            datay.append(f(i))
            nodelen += 1
        table(datax, datay)
    if choice == 5:
        break
#nodelen = readfile(datax, datay)

# print(sval, eval)

