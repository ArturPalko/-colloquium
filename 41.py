'''41. Змінній t привласнити значення істина, якщо максимальний елемент
одновимірного масиву єдиний і не перевищує наперед заданого числа а.'''

import random
t=False
a=[80,90,99,99]
print(a)
n=int(input('Ваше число='))
b=a.pop(a.index(max(a)))#видаляємо зі списку (а) і присвоюємо це значення змінній (b)
print(b)
if b not in a and b<=n:#перевіряємо умову задачі
    t=True#змінюємо значення (t), якщо умова була виконана
print(t)