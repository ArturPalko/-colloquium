'''54. Введіть масив з 20 елементів і визначте, чи є в ньому елементи з
однаковими значеннями.'''

import numpy as np
a=[]
x=[]
for i in range(1,20):
    n=int(input(f'n{i}='))
    x.append(n)
if x==list(set(x)):#порівнюємо список введених значень, із списком що є множиною із цих значень
    print('Повторюваних елементів немає')
else:
    print('Присутні повторювані елементи')