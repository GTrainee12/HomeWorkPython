n = int(input('Введите число: '))

def get_fibonacci(n):
    f_n = []
    a, b = 1, 1
    for i in range(n-0):  # Номера фибоначи
        f_n.append(a)
        a, b = b, a + b
    a, b = 0, 1
    for i in range (n):    # Добавляем отрицательные номера
        f_n.insert(0, a)
        a, b = b, a - b
    return f_n

f_n = get_fibonacci(n)
print(f"Список негафибоначчи: {get_fibonacci(n)}")
print(f"Индексы после 0: {f_n.index(0)}")