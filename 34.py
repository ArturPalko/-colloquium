'''34. Дано два лінійних масиву однакової розмірності. Скласти третій масив з
добутку елементів перших двох масивів, що стоять на місцях з однаковим індексом.'''

import numpy as np
import random
c=[]
a=np.array([random.randint(1,10) for i in range (10)])
b=np.array([random.randint(1,10) for i in range(10)])
print(a)
print(b)
c=a*b
print(c)