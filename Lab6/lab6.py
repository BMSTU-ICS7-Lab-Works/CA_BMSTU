def left_side(Y, step, index):
    if index > 0:
        return (Y[index] - Y[index - 1]) / step
    else:
        '----'

def right_side(Y, step, index):
    if index < len(Y) - 1:
        return (Y[index + 1] - Y[index]) / step
    else:
        '----'

def center_side(Y, step, index):
    if index > 0 and index < len(Y) - 1:
        return (Y[index + 1] - Y[index - 1]) / 2 / step
    else:
        '----'

def sec_diff(Y, step, index):
    if index > 0 and index < len(Y) - 1:
        return (Y[index - 1] - 2 * Y[index] + Y[index + 1]) / step ** 2
    else:
        '----'

def runge_left(Y, step, index):
    if index < 2:
        return '----'
    f1 = left_side(Y, step, index)
    f2 = (Y[index] - Y[index - 2]) / 2 / step
    return f1 + f1 - f2

def align_vars_diff(Y, X, step, index):
    if index > len(Y) - 2:
        return '----'
    ksi_diff = (1 / Y[index + 1] - 1 / Y[index] / (1 / X[index + 1] - 1 / X[index]))
    y = Y[index]
    x = X[index]
    return ksi_diff * y * y / x / x

X = [1, 2, 3, 4, 5, 6]
Y = [0.571, 0.889, 1.091, 1.231, 1.333, 1.412]

table = [[0 for i in range(6)] for j in range(5)]
methods = [left_side, center_side, runge_left, align_vars_diff, sec_diff]

for i in range(len(X)):
    print('|')
    for j in range(len(methods) - 2):
        res = methods[j](Y, X[1] - X[0], i)
        print(f'{0:.3f}'.format(res).center(8) if res != '----' else res.center(8), '|',sep='', end='')
    res = align_vars_diff(Y, X, X[1] - X[0], i)
    print(f'{0:.3f}'.format(res).center(8) if res != '----' else res.center(8), '|', sep='', end='')
    res = sec_diff(Y, X[1] - X[0], i)
    print(f'{0:.3f}'.format(res).center(8) if res != '----' else res.center(8), '|', sep='', end='')
    print('-' * (46))