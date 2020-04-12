#28. Знайти кількість парних елементів одновимірного масиву.
import numpy as np
import random
b=[]
a=np.array([random.randint(1,10) for i in range(10)])
print(a)
k=0
for g in a:
    if g%2==0:
        b.append(g)
        k+=1
if k==0:
    print('Парних елементів не було виявлено')
    exit(0)
c=np.array(b)
print(f'Парні елементи:{c}')
print(f'Кількість:{k}')