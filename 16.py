'''16. Знайти добуток елементів масиву цілих чисел, які кратні 7. Розмірність
масиву - 15. Заповнення масиву здійснити випадковими числами від 10 до 50.'''
import numpy as np
import random
a=np.array([random.randint(10,500) for i in range(20)])
b=[]
k=0#лічильник
print(a)
for g in a:#прохід по елементах
    if g%7==0:#перевірка умови
     b.append(g)#додавання до списку
     k+=1
if k==0:
      print('Елементів кратних 7-ми не виявлено')
      exit(0)
c=np.array(b)
print(f'Елементи кратні 7-ми:{c}')
print(f'Добуток:{c.prod()}')