'''33. Заданий масив А (1:20). Знайти добуток всіх його ненульових елементів.'''

import numpy as np
import random
a=np.array([random.randint(0,3) for i in range(20)])
b=[]
k=0
print(a)
for g in a:
    if g!=0:
     b.append(g)
     k+=1
if k==0:
      print('Всі елементи мають нульове значення')
      exit(0)
c=np.array(b)
print(f'Елементи що задовільняють умову:{c}')
print(f'Добуток:{c.prod()}')