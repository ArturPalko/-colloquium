'''43. Задано два натуральних числа a і b. Змінній w привласнити значення
істина, якщо в одновимірному цілочисельному масиві є хоча б один елемент, кратний а
і не кратний b.'''

import numpy as np
import random
x=[]
w=False
n=[random.randint(1,100) for i in range(20)]
print(n)
a=int(input('a='))
b=int(input('b='))
k=0
for i in n:
    if i%a==0 and i%b!=0:
        x.append(i)
        k+=1
if k>0:
    w=True
else:
    print(w)
    exit(0)
print(w)
print('Числа що задовільняють умову:',x)
print('Кількість:',k)