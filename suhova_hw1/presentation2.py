# 1. Найти N-й член последовательности 1, 1, 2, 3, 5, 8, 13...
def task1(n):
    if n < 1:
        return 0
    if n < 3:
        return 1
    x1 = 1
    x2 = 1
    for i in range(2, n):
        tmp = x1
        x1 = x2
        x2 += tmp
    return x2


# 2. Найти N-й член последовательности 1, 1, 1, 3, 5, 9, 17...
def task2(n):
    if n < 1:
        return 0
    if n < 4:
        return 1
    x1 = 1
    x2 = 1
    x3 = 1
    for i in range(3, n):
        tmp1 = x1
        tmp2 = x2
        x1 = x2
        x2 = x3
        x3 += tmp1 + tmp2
    return x3


# 3. Вывести квадраты нечетных чисел до N. (генератором списков)
def task3(n):
    return [i ** 2 for i in range(1, n, 2)]


# 4. Вычислить сумму и произведение всех натуральных чисел от А до В включительно.
def task4(a, b):
    b += 1
    summa = 0
    mul = 1
    for i in range(a, b):
        summa += i
        mul *= i
    return summa, mul


# 5. Даны натуральные числа А и В. Вывести сначала все чётные числа, заключённые
# между ними, потом все нечётные (генератором/ами списков)
def task5(a, b):
    a += 1
    return [i for i in range(a, b) if i % 2 == 0], [i for i in range(a, b) if i % 2 == 1]


# 6. Исходный список содержит положительные и отрицательные числа. Требуется
# положительные поместить в один список, а отрицательные - в другой (генератором/ами списков)

def task6(oldList):
    return [i for i in oldList if i > 0], [i for i in oldList if i < 0]

if __name__ == '__main__':
    ###
    print("task 1:")
    print(task1(7))
    print("task 2:")
    print(task2(7))
    print("task 3:")
    print(task3(10))
    print("task 4:")
    print(task4(2, 5))
    print("task 5:")
    print(task5(3, 15))
    print("task 6:")
    print(task6([2,346,-54776,2.8,443,2,0,15,-4,3]))
