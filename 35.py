'''35. Дан лінійний масив цілих чисел. Перевірте, чи є він упорядкованим по
спаданню.'''

a=[3,2,1]
b=sorted(a,reverse=True)#масив що складається з елементів (а), відстортованих за спаданням (reverse=True)
if a==b:
    print('True')
else:
    print('False')