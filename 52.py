'''52. Знайти найбільший елемент з елементів одновимірного масиву, що мають
парний номер. Визначити, чи є він єдиним.'''

import numpy as np
import random
v=[]
a=[random.randint(1,100) for i in range(10)]
print(a)
for i in range(len(a)):
    if i%2==0:
        v.append(a[i])
print('Елементи що мають парний індекс:',v)
print('Найбільший з них:',max(v))
if len(v)==len(set(v)):#клькість елементів у списку(що включає повторювані,якщо такі є) і множини(тільки унікальні)
    print('Максимальне значення має єдиний елемент')
else:
    print('Максимальне значення мають декілька елементів')
