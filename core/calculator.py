#from decorators import cache_decorator

def calculator(a, b, operation):
    # Здесь нужно реализовать функцию,
    # которая реализует основные арифметические операции между числами: +, -, /, *, **.
    # Так же следует сделать проверку, что поступивший оператор корректен (присутствует в этом списке +, -, /, *, **)
    available = ["+", "-", "/", "*", "**"]
    if operation not in available:
        return "Неккоректная операция"
    operations = {
        "+": lambda x, y: x + y,
        "-": lambda x, y: x - y,
        "/": lambda x, y: x / y,
        "*": lambda x, y: x * y,
        "**": lambda x, y: x ** y
    }
    try:
        result = operations[operation](a, b)
    except ZeroDivisionError:
        return "Ошибка! Деление на ноль"
    else:
        return result

if __name__ == '__main__':
    while True:
        try:
            a = int(input('Введите число: '))
            break
        except ValueError:
            print("Ошибка! Для ввода доступны только целые числа")
    while True:
        try:
            b = int(input('Введите число: '))
            break
        except ValueError:
            print("Ошибка! Для ввода доступны только целые числа")
    operation = input('Введите операцию: ')

    print('Результат: ', calculator(a, b, operation))