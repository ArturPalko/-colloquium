'''37. Розсортуйте заданий лінійний масив по зростанню.'''

import numpy as np
import random

a=np.array([random.randint(1,50) for i in range(10)])
print(a)
print(f'Сортування за зростанням: {sorted(a)}')