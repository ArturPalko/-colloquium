'''42. Підрахувати кількість елементів одновимірного масиву, для яких
виконується нерівність i*i<ai<i!'''

#створюємо функцію факторіалу
def fac(n):
    factorial=1
    for i in range(2,n+1):
        factorial*=i
    return factorial

import random
x=[]
a=[random.randint(1,100) for i in range(20)]
print(a)
k=0#лічильник елементів що задовільняють настуну умову
for i in range(len(a)):
    if i**2<a[i]<fac(i):
        x.append(a[i])
        k+=1

print(f'Числа що задовільняють умову:',x)
print(f'Кількість: {k}')