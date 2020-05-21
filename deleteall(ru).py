import os
import time

try:
    a = open('path.txt', 'r')
    w = a.read()
    a.close()
except:
    exit(0)

os.system('cls')
input('\nПодключите вашу флешку('+ w +') к компьютеру\nПосле этого, нажмите Enter.')
print('Удаление приватного ключа...')
try:
    os.remove(w + 'private.pem')
    print('Приватный ключ удален!')
except:
    print('Ошибка! Приватный ключ не удален!')
print('Удаление публичного ключа...')
try:
    os.remove('open.pem')
    print('Публичный ключ удален!')
except:
    print('Ошибка! Публичный ключ не удален!')
print('Удаление базы данных...')
try:
    os.remove('password.txt.bin')
    print('База данных удалена!')
except:
    print('Ошибка! База данных не удалена!')
print('Удаление мусорных файлов...')
try:
    os.remove('path.txt')
    print('Мусорные файлы удалены!')
except:
    print('Ошибка! Мусорные файлы не удалены!')
print('----------------------------------------------------')
print('Успешно!')
time.sleep(4)
exit(0)
