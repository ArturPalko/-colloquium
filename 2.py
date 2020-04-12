'''2. Введіть з клавіатури п'ять цілочисельних елементів масиву X. Виведіть на
екран значення коріння і квадратів кожного з елементів масиву.'''
import numpy as np
import math
a=list()
for i in range(1,6):#Введення чисел
    x=(int(input(f'Число{i}=')))
    a.append(x)#додавання чисел до списку
b=a[:]
v=np.array(a)#створення масиву зі списку
for element in a:
    print(element**element)
for c in b:
    print(math.sqrt(c))