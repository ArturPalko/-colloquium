'''12. Дані про температуру повітря за декаду грудня зберігаються в масиві.
Визначити, скільки раз температура була вище середньої за цю декаду.'''

import numpy as np
import random
b=[random.randint(-6,5) for i in range(10)]
a=np.array(b)#створення масиву
print('Температура з 1 по 10 грудня:')
print(a)
k=0#лічильник
for i in a:#прохід по елементах масиву
    if i>a.mean():#перевірка умови
        k+=1
print(f'Темература була вищою за середню: {k} раз')