'''59. Дан одновимірний масив з 10 цілих чисел. Підрахуйте кількість різних
чисел в ньому.'''

a=[1,3,2,4,5,6,6,7,7,8]
print(a)
#виводимо список що є множиною списку (а), тобто унікальні значення
print('Різні елементи:',sorted(list(set(a))))
k=len(set(a))
#виводимо потужність множини k
print('Кількість:',k)

