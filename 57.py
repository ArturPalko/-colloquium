'''57. Відомість на зарплату представлена як дві таблиці. Одна містить
прізвища працівників цеху, а друга - їх зарплату за поточний місяць. Знайдіть прізвище
працівника, зарплата якого найменш відхиляється від середньої зарплати всіх
працівників за поточний місяць. Знайдіть прізвища двох працівників з найбільшою
заробітною платою. Видаліть з відомості на зарплату відомості про працівника,
зарплата якого мінімальна.'''

import numpy as np
n=('Іван Максим Володимир Ігор Олександр Петро Патрік Григорій Дмитро Ілля'.split()*10)
p=[100,200,300,400,500,600,700,800,900,1000]
a=np.array(list(zip(n,p)))
#створюємо копії уже прінтованих значень(n,p), щоб редагувати і вивести новий масив
n_new=n.copy()
p_new=p.copy()
print(a)


w=sorted(p)
mean=np.array(p).mean()
print(f'Середня зарплата за поточний місяць:{mean}')
w=sorted(p)#сортуємо у порядку зростання зарплати працівників
z=[]#список значень (середня зарплата (мінус) зарплата кожного працівника)
for element in w:
    difference=mean-element
    z.append(difference)
#додаєио значень різниці у список (z)
#якщо елемент (z) від'ємний множимо його на (-1) - для подальшої оцінки наближень з обох сторін
for i in range(len(z)):
    if z[i]<0:
        z[i]*=(-1)
#якщо однакових наближень декілька, то включаємо і їх(наступні елементи у списку z)
if z.index(min(z))!=len(z) and min(z)==z[z.index(min(z))+1] :
        mini=z.index(min(z))+1
#виводимо масив (а) по отриманим індексам
print(f'Найменьше відхилення від середньої зарплати:{a[z.index(min(z))]}{a[mini]}')
print('2 працівники що мають найвищу зарплату:')
k=0
while k<2:
#Виводимо (а) по індексу максимального значення зарплати двічі
    t=p.index(max(p))
    print(f'{a[t]}')
    del p[t]
    k+=1
print('Видалено працівника з найменшою зп:')

del p_new[p_new.index(min(p_new))]
del n_new[p_new.index(min(p_new))]
print()
a_new=np.array(list(zip(n_new,p_new)))
print(a_new)
    

    
    
    
    
    



