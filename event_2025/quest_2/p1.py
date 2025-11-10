def multiply(x, y):
    return [x[0] * y[0] - x[1] * y[1], x[0] * y[1] + x[1] * y[0]]


def add(x, y):
    return [x[0] + y[0], x[1] + y[1]]


def divide(x, y):
    return [x[0] // y[0], x[1] // y[1]]


A = list(map(int, open("../../input.txt").read().replace('[', '').replace(']', '').split('A=')[1].split(',')))

R = [0,0]

for i in range(3):
    R = multiply(R, R)

    R = divide(R, [10, 10])

    R = add(R, A)

print(R)