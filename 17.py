'''17. Знайти суму елементів масиву дійсних чисел, що мають непарні номери.
Розмірність масиву - 20. Заповнення масиву здійснити випадковими числами від 100
до 200.'''

import numpy as np
import random
a=np.array([random.randint(100,200) for i in range(20)])
b=[]
print(a)
for g in range(20):
    if g%2!=0:
     b.append(a[g])
c=np.array(b)
print(f'Елементи на непарних номерах: {c}')
print(f'Сума: {c.sum()}')