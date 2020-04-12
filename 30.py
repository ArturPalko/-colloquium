'''30. Обчислити середнє арифметичне значення тих елементів одновимірного
масиву, які розташовані за першим по порядку мінімальним елементом.'''

import numpy as np
import random
b=[random.randint(1,10) for i in range(10)]
a=np.array(b)
print(a)
print(f'Індекс мінімального елементу:{b.index(a.min())}')
c=np.array(b[b.index(a.min()):])
print(f'Зріз:{c}')
print(f'Середнє значення елементів зрізу:{c.mean()}')