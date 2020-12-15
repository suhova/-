# 1. Нарисовать рамочку шириной w символов и высотой h символов.
def task1(w, h):
    task3(w, h, "$", 1)


# 2. Пускай символ, которым рисуется рамочка – тоже входной параметр.
def task2(w, h, symbol):
    task3(w, h, symbol, 1)


# 3. Нарисовать рамочку шириной w символов и высотой h символов, и толщиной f символов. (оформить в виде функции)
def task3(w, h, symbol, f):
    for i in range(h):
        if i not in range(f, h - f):
            print(symbol * w)
        else:
            print((symbol * f) + (" " * (w - 2 * f)) + (symbol * f))
    print()


if __name__ == '__main__':
    task3(17, 8, "#", 2)
