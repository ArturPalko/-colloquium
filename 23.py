'''23. Знайти суму всіх елементів масиву цілих чисел, які менше середнього
арифметичного елементів масиву. Розмірність масиву - 20. Заповнення масиву
здійснити випадковими числами від 150 до 300.'''
import numpy as np
import random
c=[]
b=[random.randint(150,300) for i in range(20)]
a=np.array(b)
print(a)
k=0
for i in a:
    if i<a.mean():
        c.append(i)
        k+=1
if k==0:
    print('Елементів що задовільняють умову не знайдено')
d=np.array(c)
print(f'Елементи що задовільняють умову:{d}')
print(f'Сума:{d.sum()} ')