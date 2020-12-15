# 1. Каждый день я пробегаю «следующую степень двойки» км.
# Сколько дней пройдет, пока я в сумме пробегу 1000 км? 10000 км?
def task1(s):
    day = 1
    km = 2
    while km < s:
        day += 1
        km += 2 ** day
    return day


# 3. Начав тренировки, спортсмен в первый день пробежал 10 км.
# Для увеличения выносливости ему необходимо повышать норму бега через одну тренировку
# на 15%  от нормы предыдущей тренировки. Спортсмен тренируется каждый день.
# Какой суммарный путь он пробежит за 30 дней.
def task3(firstDayKm, days, prc):
    km = firstDayKm
    day = 1
    res = firstDayKm
    prc = 1 + prc / 100
    while day < days:
        if day % 2 == 0:
            km *= prc
        res += km
        day += 1
    return res


# 4. Начав тренировки, спортсмен в первый день пробежал 10 км.
# Каждый следующий день он увеличивал дневную норму на 10% от нормы предыдущего дня.
# Через сколько дней:
# а) спортсмен будет пробегать в день больше 20 км;
# b) пробежит суммарный путь 100 км.
def task4a(firstDayKm, prc, maxKm):
    km = firstDayKm
    day = 1
    prc = 1 + prc / 100
    while km <= maxKm:
        km *= prc
        day += 1
    return day


def task4b(firstDayKm, prc, sumKm):
    km = firstDayKm
    day = 1
    res = firstDayKm
    prc = 1 + prc / 100
    while res < sumKm:
        km *= prc
        res += km
        day += 1
    return day


if __name__ == '__main__':
    ###
    print("task 1:")
    print(task1(1000))
    print(task1(10000))
    print("task 3:")
    print(task3(10, 30, 15))
    print("task 4a:")
    print(task4a(10, 10, 20))
    print("task 4b:")
    print(task4b(10, 10, 100))
