from math import *
import numpy

def f(x, y):
    return x * x + y * y


def readfile(datax, datay):
    f = open('Lab1.txt', 'r')
    linecount = 0
    for line in f:
        linecount += 1
        line = line.split()
        datax.append(float(line[0]))
        datay.append(float(line[1]))
    return linecount


def table(datax, datay, dataz):
    print('-' * 21)
    print('|    x    |    y    |    z    |')
    print('-' * 21)
    for i in range(nodelen):
        print('|{0:7.3f}  |{1:7.3f}  |{2:7.3f}'.format(datax[i], datay[i], dataz[i]))


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
    print("MENU:\n1. Find z\n2. Enter interval and write f(x, y, z) in def\n3. Exit")

datax = []
datay = []
dataz = []
left = 0
reszy = []
reszx = []
right = 0
while 1:
    menu()
    choice = int(input("Make your choice: "))
    if choice == 1:
        y = float(input('Введите y для нахождения z: '))
        nodenum = int(input("Введите количество узлов n: "))
        sh = int((r - l) / step)
        print (r, l, sh, step)
        for i in range(nodenum + 1):
            ind = findpos(datay[i * sh:i * sh + sh], dataz[i * sh:i * sh + sh], y, nodenum + 1)
            pn = defroot(datay[i * sh:i * sh + sh], dataz[i * sh:i * sh + sh], ind, y)
            print('Pn = {0:.3f}'.format(pn))
            reszy.append(pn)
            reszx.append(datax[i * sh])
        print (reszy)
        print (reszx)
        x = float(input('Введите x для нахождения z: '))
        nodenum = int(input("Введите количество узлов m: "))
        ind = findpos(reszx, reszy, x, nodenum + 1)
        pn = defroot(reszx, reszy, ind, x)
        print('Zn = {0:.3f}'.format(pn))
        left = 0
        reszy = []
        reszx = []
        right = 0

    if choice == 2:
        nodelen = 0
        l = float(input("Enter left end of interval: "))
        r = float(input("Enter right end of interval: "))
        step = float(input("Enter step: "))
        datax = []
        datay = []
        for i in numpy.arange(l, r, step):
            for j in numpy.arange(l, r, step):
                datax.append(i)
                datay.append(j)
                dataz.append(f(datax[nodelen],datay[nodelen]))
                nodelen += 1
        table(datax, datay, dataz)
    if choice == 3:
        break

