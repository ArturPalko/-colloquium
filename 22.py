'''22. Знайти добуток елементів масиву, кратних 3 і 9. Розмірність масиву - 10.
Заповнення масиву здійснити випадковими числами від 5 до 500.'''
import numpy as np
import random
a=np.array([random.randint(5,500) for i in range(10)])
b=[]
k=0
print(a)
for g in a:
    if g%3==0 and g%9==0 :
     b.append(g)
     k+=1
if k==0:
      print('Елементів кратних 3-ьом і 9-ьом не виявлено')
      exit(0)
c=np.array(b)
print(f'Елементи кратні 3-ьом і 9-ьом:{c}')
print(f'Добуток:{c.prod()}')