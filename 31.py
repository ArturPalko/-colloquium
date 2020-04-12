'''31. Обчислити середнє арифметичне значення тих елементів одновимірного
масиву, які потрапляють в інтервал від -2 до 10.'''
import numpy as np
import random
c=[]
b=np.array([random.randint(-30,30) for i in range(15)])
print(b)
k=0
for g in b:
    if -2<g<10:
        c.append(g)
        k+=1
if k==0:
    print('Жоден елемент масиву немає значення із вказаного інтервалу')
    exit(0)
a=np.array(c)
print(f'Елементи значення яких належить інтервалу:{a}')
print(f'Середнє арифметичне:{a.mean()}')