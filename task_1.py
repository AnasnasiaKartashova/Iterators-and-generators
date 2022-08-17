'''
Функция реализует генератор геометрической прогрессии и значение stop (до какого числа генерировать)
'''
a
def generator(value, denominator,stop):
    value = int(value)
    denominator = int(denominator)
    n = 2
    while value < stop:
        value = value * (denominator ** (n-1))
        yield value
        n + 1


for x in generator(1,2,100):
    print('Значение поменялось на: ', x)



