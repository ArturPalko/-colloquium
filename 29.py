'''29. Знайти кількість парних елементів одновимірного масиву до першого
зустрінутого числа рівного наперед заданому числу а.'''
import numpy as np
import random
n=int(input('n='))
b=[]
a=np.array([random.randint(1,10) for i in range(10)])
print(a)
k=0
for g in a:
    if g == n: break
    if g%2==0:
      b.append(g)
      k+=1
if k==0:
    print('Парних елементів не було виявлено')
    exit(0)
c=np.array(b)
print(f'Парні елементи:{c}')
print(f'Кількість:{k}')