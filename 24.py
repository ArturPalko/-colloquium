'''24. Знайти суму елементів масиву цілих чисел, які діляться на 5 і на 8
одночасно. Розмірність масиву - 30. Заповнення масиву здійснити випадковими
числами від 500 до 1000.'''
import numpy as np
import random
a=np.array([random.randint(500,1000) for i in range(30)])
b=[]
k=0
print(a)
for g in a:
    if g%5==0 and g%8==0 :
     b.append(g)
     k+=1
if k==0:
      print('Елементів кратних 3-ьом і 9-ьом не виявлено')
      exit(0)
c=np.array(b)
print(f'Елементи кратні 5-и і 8-ми:{c}')
print(f'Сума:{c.sum()}')