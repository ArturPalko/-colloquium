'''5. Створіть масив А [1..7] за допомогою генератора випадкових чисел і
виведіть його на екран. Збільште всі його елементи в 2 рази.'''

import numpy as np
import random
a=np.array([random.randint(2,5) for i in range(7)])#створення масиву
print(a)
a_new=a.copy()
for g in range(len(a_new)):#прохід по елементах масиву
    a_new[g]*=2#збільшення в 2 рази елементів
print(a_new)