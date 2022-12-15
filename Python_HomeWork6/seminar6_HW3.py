# Семинар 2 Д/З 2 абдейт с помощью map,lambda
from math import factorial
n = int(input('Введите число: '))
print(list(map(lambda x: ((x == 1) and 1) or x * factorial(x -1),list(range(1,n+1)))))