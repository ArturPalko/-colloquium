'''13. Створіть масив з 15 цілочисельних елементів і визначте серед них
мінімальне значення.'''

import numpy as np
import random
b=[random.randint(-6,5) for i in range(15)]
a=np.array(b)
print(a)
print(f'Мінімальне значення: {a.min()}')