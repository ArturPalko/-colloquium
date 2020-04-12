'''25. Знайти добуток елементів лінійного масиву цілих чисел, які кратні 5.
Розмірність масиву - 10. Заповнення масиву здійснити випадковими числами від 10 до
100.'''
import numpy as np
import random
a=np.array([random.randint(10,100) for i in range(10)])
b=[]
k=0
print(a)
for g in a:
    if g%5==0:
     b.append(g)
     k+=1
if k==0:
      print('Елементів кратних 5-ти не виявлено')
      exit(0)
c=np.array(b)
print(f'Елементи кратні 5-ти:{c}')
print(f'Добуток:{c.prod()}')