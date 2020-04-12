'''20. Знайти суму всіх елементів масиву дійсних чисел, більших за задане
число. Розмірність масиву - 20. Заповнення масиву здійснити випадковими числами
від 50 до 100.'''

import numpy as np
import random
n=int(input('n='))
b=[random.randint(50,100) for i in range(20)]
a=np.array(b)
print(a)
c=[]
k=0
for g in b:
    if g>n:
     c.append(g)
    k+=1
if k==0:
    print('Елементів що задовільняють умову не виявлено')
    exit(0)
a_new=np.array(c)
print('Елементи більші за n:',a_new)
print(f'Сума:{a_new.sum()}')