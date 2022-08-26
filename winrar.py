import time     
import sys

money = 25


print("Вы решили купить WinRar")
time.sleep(1)
print("WinRar стоит 200$")
time.sleep(2)
print('Вы хотите купить? Да - Нет')
buy = input('')

if buy == 'Да':
	print("У вас осталось -200$" )

elif buy == 'Нет':
	print('Вы не купили WinRar')
	print('И сэкономили 200$')

else:
	print('Это не ответ') 
