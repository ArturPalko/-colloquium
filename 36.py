'''36. Знайти суму додатніх елементів лінійного масиву цілих чисел.
Розмірність масиву - 10. Заповнення масиву здійснити з клавіатури.'''

import numpy as np
x=list()
c=list()
for i in range(1,11):
    a=(int(input(f'Число{i}=')))
    x.append(a)
print(x)
for g in x:
    if g>=0:
      c.append(g)
print('Додатні елементи:',c)
v=np.array(c)
print(f'Сума додатніх елементів:{v.sum()}')