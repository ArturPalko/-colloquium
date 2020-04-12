'''18. Знайти добуток всіх елементів масиву цілих чисел, менших 0. Розмірність
масиву - 10. Заповнення масиву здійснити за допомогою клавіатури.'''

import numpy as np
import random
b=[]
for i in range(1,11):
    k=int(input(f'Елемент{i}='))
    b.append(k)
a=np.array(b)
k=0
c=[]
for g in a:
    if g<0:
      c.append(g)
      k+=1
if k==0:
    print(f'Елементів що задовільняють умову не виявлено')
    exit(0)
a_new=np.array(c)
print(f'Елементи меньше нуля:{a_new}')
print(f'Добуток:{a_new.prod()}')