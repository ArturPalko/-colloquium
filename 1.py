'''1. Введіть з клавіатури в масив п'ять цілочисельних значень. Виведіть їх в
один рядок через кому. Отримайте для масиву середнє арифметичне.'''''

import numpy as np
x=list()
for i in range(1,6):#Введення 5-ти чисел
    a=(int(input(f'Число{i}=')))
    x.append(a)#Додавання чисел у список
v=np.array(x)#Сторення масиву з отриманого списку
print(v)
print(f'Середнє значення:{v.mean()}')
