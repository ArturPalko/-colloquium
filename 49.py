'''49. Задано дві таблиці. Одна містить найменування послуг, а інша - розцінки
за ці послуги. Видаліть з обох таблиць все, що передує послузі, ціна якої G гривень.'''


import numpy as np
a='Вкладання ламінату на підлогу_Встановленнядатчика руху_Заміна електричної проводки_Зрізання дерева'.split('_')
b=[20,70,250,350]
c='грн'.split()*4
v=np.array(list(zip(a,b,c)))
print(v)
G=int(input('G='))
t=0
for i in b:
    if G==i:
#видалення елементів трьох списку по однаковому проміжку
        t=b.index(i)
        del b[:t]
        del a[:t]
        del c[:t]
c=np.array(list(zip(a,b,c)))
print(c)
