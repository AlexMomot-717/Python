n = int(input('Введите целое число: '))
k = n
max_digit = n % 10
n //= 10
while n > 0:
    digit = n % 10
    if digit > max_digit:
        max_digit = digit
    n //= 10
print('Максимальная цифра в числе', str(k) + ': ', max_digit)
