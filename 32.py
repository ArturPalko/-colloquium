'''32. Змінній t привласнити значення істина, якщо в одновимірному масиві є
хоча б одне від’ємне і парне число.'''
import numpy as np
import random
b=np.array([random.randint(-10,10) for i in range(3)])
print(b)
t=False
for i in b:
    if (i < 0) and (i % 2 == 0):
     t=True
     break
print(t)