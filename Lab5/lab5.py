#a lot to be done above

N = 0
M = 0

start = 0
end = 3.1415926535 / 2
 
step  = 0.0001

start_poly = -1
end_poly = 1

h_y = 0
EPS = 1e-7


def matrix_max_first(matrix, x_vars, itera):
    mx = itera;
    for i in range(itera, x_vars, 1):
        if matrix[i][itera] > matrix[mx][itera]:
            mx = i
    tmp = matrix[itera]
    matrix[itera] = maxtrix[mx]
    matrix[mx] = tmp

def matrix_normalize_rows(matrix, x_vars, itera):
    for i in range(itera, x_vars, 1):
        normalize = matrix[i][itera]
        if (fabs(normalize) < 1E-06):
            continue
        for j in range(itera, x_vars + 1, 1):
            matrix[i][j] /= normalize;
    for i in range(itera + 1, x_vars, 1):
        if (matrix[i][itera] < 1E-06):
            continue
        for j in range(itera, x_vars + 1, 1):
            matrix[i][j] -= matrix[itera][j];
    

def matrix_get_solutions(matrix, x_vars, x):
    for i in range (x_vars - 1, 0, -1):
        sigma = 0
        for j in range (x_vars - 1, 0, -1):
            sigma += matrix[i][j] * x[j]
        if (abs(matrix[i][i]) <= 1E-06):
            x[i] = 0
            continue
        x[i] = (matrix[i][x_vars] - sigma) / matrix[i][i]


def f(phi, tau, t):
    l_r = (2 * cos(tau)) / (1 - sin(tau) * sin(tau) * cos(phi) * 2)
    return  (1 - exp(-t * l_r)) * cos(tau) * sin(tau)

def F(phi, tau, M, h_y):
    res = 0
    for i in range(0, M / 2, 1):
        res += f(phi, start + 2 * i * h_y, tau) +\
           4 * f(phi, start + (2 * i + 1) * h_y, tau) +\
               f(phi, start + (2 * i + 2) * h_y, tau);

    res *= h_y / 3
    return res

def P_i(x, i):
    if i == 0:
        return 1
    elif i == 1:
        return x
    return 1/i * ((2 * i - 1) * x * P_i(x, i - 1)\
                  - (i - 1) * P_i(x, i - 2))

def half_search(start, end, n):
    half = (end + start) / 2
    while (abs(P_i(half, n) > EPS)):
        if (P_i(half, n) * P_i(end, n) < 0):
            start = half
            half = (end + start) / 2
        else:
            end = half
            half = (end + start) / 2
    return half

def calculate():
    x = []
    y = []
    tau  = 0.05
    while (tau <= 10):
        x.append(tau)
        N = int(input("Введите N"))
        M = int(input("Введите M"))
        h_y = (end - start) / M
        n = N
        P = [(n + 1) * [n + 1]]
        t = []
        x = start_poly
        while x < (end_poly - step):
            if P_i(x, n) * P_i(x + step, n) < 0:
                t.append(half_search(x, x + step, n))
            x += step
        matrix = [(2*n - 1) * [n + 1]]
        for i in range(0, 2 * n - 1, 1):
            for j in range(0, n, 1):
                matrix[i][j] = t[j]**i
            matrix[i][n] = (1 - (-1)**(i + 1)) / (i + 1)

        for itera in range(0, n, 1):
            matrix_max_first(matrix, n, itera)
            matrix_normalize_rows(matrix, n, itera)
        A = [n]
        matrix_get_solutions(matrix, n, A)
        res
        for i in range(0, N, 1):
            res += A[i] * F((end + start) / 2 + (end - start)\
                            / 2 * t[i], tau, M, h_y)
        res *= (end - start) / 2
        res *= 4 / 3,1415926535
        y.append(res)
        tau += 0.05
    plt.plot(x, y, 'kD', color = 'black', label = '$таблица$')
    plt.grid(True)
    plt.axis(-1, 11, 0, 1.5)

    plt.show()
            
calculate()
        
