'''15. Знайти суму парних елементів масиву цілих чисел. Розмірність масиву -
20. Заповнення масиву здійснити випадковими числами від 100 до 200.'''

import numpy as np
import random
a=np.array([random.randint(100,200) for i in range(20)])
b=[]
k=0#лічильник
print(a)
for i in a:#прохід по елементах масиву
    if i%2==0:
     b.append(i)#додавання елементів, що проходять умову до списку
     k+=1
if k==0:
    print('Парних елементів не було виявлено')
    exit()#завершення виконання програми
c=np.array(b)
print(f'Парні числа:{c}')
print(f'Сума:{c.sum()}')