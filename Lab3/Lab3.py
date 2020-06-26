from math import *
import numpy

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
    for i in range(len(datax)):
        print('|{0:7.3f}  |{1:7.3f}  |'.format(datax[i], datay[i]))

def spline(datax, datay, x_value):
    n = len(datax)
    i_near = min(range(n), key = lambda i: abs(datax[i] - x_value)) # индекс ближайшего значения

    h = [0 if not i else datax[i] - datax[i - 1] for i in range(n)] # шаг значения
    
    A = [0 if i < 2 else h[i-1] for i in range(n)]
    B = [0 if i < 2 else -2 * (h[i - 1] + h[i]) for i in range(n)]
    D = [0 if i < 2 else h[i] for i in range(n)]
    F = [0 if i < 2 else -3 * ((datay[i] - datay[i - 1]) / h[i] - (datay[i - 1] - datay[i - 2]) / h[i - 1]) for i in range(n)]

    # forward
    ksi = [0 for i in range(n + 1)]
    eta = [0 for i in range(n + 1)]
    for i in range(2, n):
        ksi[i + 1] = D[i] / (B[i] - A[i] * ksi[i])
        eta[i + 1] = (A[i] * eta[i] + F[i]) / (B[i] - A[i] * ksi[i])

    # backward
    c = [0 for i in range(n + 1)]
    for i in range(n - 2, -1, -1):
        c[i] = ksi[i + 1] * c[i + 1] + eta[i + 1]


    a = [0 if i < 1 else datay[i-1] for i in range(n)]
    b = [0 if i < 1 else (datay[i] - datay[i - 1]) / h[i] - h[i] / 3 * (c[i + 1] + 2 * c[i]) for i in range(n)]
    d = [0 if i < 1 else (c[i + 1] - c[i]) / (3 * h[i]) for i in range(n)]

    res = a[i_near] + b[i_near] * (x_value - datax[i_near - 1]) + c[i_near] * ((x_value - datax[i_near - 1]) ** 2) + d[i_near] * ((x_value - datax[i_near - 1]) ** 3)

    return res

    
def menu():
    print("MENU:\n1. Find x\n2. Enter interval and write f(x, y, z) in def\n3. Exit")

datax = []
datay = []
while 1:
    menu()
    choice = int(input("Make your choice: "))
    if choice == 1:
        x = float(input('Введите x для поиска: '))
        res = spline(datax, datay, x)
        print("Найденный x: ", res)
        reszy = []
        reszx = []

    if choice == 2:
        nodelen = 0
        l = float(input("Enter left end of interval: "))
        r = float(input("Enter right end of interval: "))
        step = float(input("Enter step: "))
        datax = []
        datay = []
        for i in numpy.arange(l, r, step):
            datax.append(i)
            datay.append(f(i))
        table(datax, datay)
    if choice == 3:
        break

