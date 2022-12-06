l = list(map(int, input("Введите числа через пробел:\n").split()))
new_l = [i for i in l if l.count(i) == 1]
print(f"Исходный список: {l} -> Список из неповторяющихся элементов: {new_l}")