'''21. Знайти добуток всіх елементів масиву дійсних чисел, менших заданого
числа. Розмірність масиву - 10. Заповнення масиву здійснити випадковими числами
від 50 до 100.'''
import numpy as np
import random
n=int(input('n='))
b=[random.randint(50,100) for i in range(10)]
a=np.array(b)
print(a)
c=[]
k=0
for g in b:
    if g<n:
     c.append(g)
     k+=1
if k==0:
    print('Елементів що задовільняють умову не виявлено')
    exit(0)
a_new=np.array(c)
print('Елементи меньші за n:',a_new)
print(f'Добуток:{a_new.prod()}')