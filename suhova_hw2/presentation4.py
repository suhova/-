
# Создайте приложение для перевода из одной системы счисления в другую
def convert(strNumber, to_ss, from_ss=2):
    symbols = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    if isinstance(strNumber, str):
        number = intImpl(strNumber, from_ss)
    else:
        number = strNumber
    if number < to_ss:
        return symbols[number]
    else:
        return symbols[number % to_ss] + convert(number // to_ss, to_ss)

def intImpl(strNumber, from_ss):
    symbols = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    result = 0
    for i in range(len(strNumber)):
        for j in range(from_ss):
            if (strNumber[i] == symbols[j]):
                result = result * from_ss + j
    return result

if __name__ == '__main__':
    print(convert('A', 2, 18))
    print(convert('10', 2, 18))
    print(convert('10', 18, 2))