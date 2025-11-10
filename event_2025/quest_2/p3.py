def multiply(x, y):
    return [x[0] * y[0] - x[1] * y[1], x[0] * y[1] + x[1] * y[0]]


def add(x, y):
    return [x[0] + y[0], x[1] + y[1]]


def divide(x, y):
    return [int(x[0] / y[0]), int(x[1] / y[1])]


A = list(map(int, open("../../input.txt").read().replace('[', '').replace(']', '').split('A=')[1].split(',')))

A_end = add(A, [1000, 1000])

grid = []

for col in range(A[0], A_end[0]+1, 1):
    for row in range(A[1], A_end[1]+1, 1):
        grid.append([col, row])

engraved_count = 0

for P in grid:
    R = [0, 0]
    engraved = True
    for i in range(100):

        R = multiply(R, R)

        R = divide(R, [100000,100000])

        R = add(R, P)

        if R[0] < -1000000 or R[0] > 1000000 or R[1] < -1000000 or R[1] > 1000000:
            engraved = False
            break
    if engraved:
        engraved_count += 1


print(engraved_count)