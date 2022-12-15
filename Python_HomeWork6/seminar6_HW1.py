# Семинар 2 Д/З 1 абдейт с помощью map
n = input('Введите вещественное число: ')
sum = sum(map(int, n.replace('.', '')))
print (sum)