# Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
# Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.

def get_div_quotient():
    """"Return a quotient from devision.

    Positional parameters:
    d1 as dividend
    d2 as divisor
    """
    d1 = input('Enter dividend: ')
    d2 = input('Enter divisor: ')
    try:
        d1 = int(d1)
        d2 = int(d2)
        return print(round(d1 / d2, 2))
    except ZeroDivisionError as error:
        print(error)
    except (TypeError, ValueError) as error:
        print(error)


get_div_quotient()
