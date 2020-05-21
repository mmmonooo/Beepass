import os
import time

try:
    a = open('path.txt', 'r')
    w = a.read()
    a.close()
except:
    exit(0)

os.system('cls')
input('\nPlease, plug in your memory stick('+ w +')\nAfter that, press enter.')
print('Private key deleting...')
try:
    os.remove(w + 'private.pem')
    print('Private key deleted!')
except:
    print('Error, private key is not deleted!')
print('Open key deleting...')
try:
    os.remove('open.pem')
    print('Open key deleted!')
except:
    print('Error, open key is not deleted!')
print('Database deleting...')
try:
    os.remove('password.txt.bin')
    print('Database deleted!')
except:
    print('Error, database is not deleted!')
print('Junk deleting...')
try:
    os.remove('path.txt')
    print('Junk deleted!')
except:
    print('Error, junk is not deleted!')
print('----------------------------------------------------')
print('Done!')
time.sleep(4)
exit(0)
