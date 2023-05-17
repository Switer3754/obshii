def get_result():
    number1 = float(input('Введите первое число: '))
    number2 = float(input('Введите второе число: '))
    operation = '+-*/'
    symbol = input('Укажите операцию: ')

    if symbol not in list(operation):
        print('Неверная операция')

    if symbol == '+':
        return number1 + number2
    elif symbol == '*':
        return number1 * number2
    elif symbol == '-':
        return number1 - number2
    elif symbol == '/' and number1 == 0 or number2 == 0:
        return 'Недопустимая операция'
    elif symbol == '/':
        return number1 / number2
    else:
        return 'Неправильно выбрано'

print(get_result())

print(input())







