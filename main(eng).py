from Crypto.PublicKey import RSA
from Crypto.Random import get_random_bytes
from Crypto.Cipher import AES, PKCS1_OAEP
import os
import os.path
import time
import random

#asci cats arts
cat1 = "     /\_____/\ \n    /  o   o  \ \n   ( ==  |  == )\n    )         (\n   (           )\n  ( (  )   (  ) )\n (__(__)___(__)__)"
cat2 = "  /\_/\  (\n ( ^.^ ) _)\n   \|/  (\n ( | | )\n(__d b__)"
cat3 = "|\__/,|\n|o o  |\n_______"
cat3_1 = "|\__/,|\n|  o o|\n_______"
cat4 = "                     /^--^\     /^--^\      /^--^\ \n                     \____/     \____/     _\____/ \n                    /      \   /      \   /      \ \n                   |        | |        | |        | \n                    \__  __/   \__  __/   \__  __/ \n|^|^|^|^|^|^|^|^|^|^|^|^\ \^|^|^|^/ /^|^|^|^|^\ \^|^|^|^|^|^|^|^|^|^|^|^|\n| | | | | | | | | | | | |\ \| | |/ /| | | | | | \ \ | | | | | | | | | | |\n########################/ /######\ \###########/ /#######################\n| | | | | | | | | | | | |\/ | | | |\/ | | | | | \/| | | | | | | | | | | |\n|_|_|_|_|_|_|_|_|_|_|_|_|_|_|_|_|_|_|_|_|_|_|_|_|_|_|_|_|_|_|_|_|_|_|_|_|"
cat5 = "(^ ' - ' ^)/"
cat6 = "(.) ' - '(.)'"

#str to generate passwords
symbols = 'A B C D E F G H I J K L M N O P Q R S T U V W X Y Z a b c d e f g h i j k l m n o p q r s t u v w x y z 1 2 3 4 5 6 7 8 9 0 ! @ # $ % ^ & * ( ) _ - + = ! " № ; % : ? * { } [ ] /  < > ~'
passsssssssssssword = []

while True:
    os.system('cls') #clear screen
    q = os.path.isfile('open.pem') #search public key
    if q == False: #public key is not found
        print('Welcome to Beepass.')
        print(cat2)
        time.sleep(2)
        print('Beepass is a open-source password manager, created by MONO.')
        time.sleep(2)
        a = input("\nLet's generate open and private key.\nEnter the size of keys, for example - 2048: ")
        a = int(a)
        input('\nPlease, plug in your memory stick.\nAfter that, press enter.')
        path = input('Enter the letter of your memory stick(for ex. - E): ')

        r = open('path.txt', 'w') #generate path.txt file to read private key
        r.write(path + ':/')
        r.close()

        for i in range(4): #loading cat
            os.system("cls")
            print(cat3)
            time.sleep(0.5)
            os.system("cls")
            print(cat3_1)
            time.sleep(0.5)

        time.sleep(0.5)
        os.system('cls')
        print('Generating keys...')

        key = RSA.generate(a) #generating keys
        private_key = key.export_key() #generating private key
        file_out = open(path + ':/' + "private.pem", "wb")
        file_out.write(private_key)
        print('Private key is done.')

        public_key = key.publickey().export_key() #generating public key
        file_out = open("open.pem", "wb")
        file_out.write(public_key)
        print('Open key is done.')

        print('\nCreating a password database...')

        g = open('password.txt', 'w') #generating password list
        g.close()

        f = open('password.txt', "rb") #encrypting passwords list
        data = f.read(); f.close()
        file_out = open(str('password.txt')+".bin", "wb")
        recipient_key = RSA.import_key(open("open.pem").read())
        session_key = get_random_bytes(16)
        cipher_rsa = PKCS1_OAEP.new(recipient_key)
        enc_session_key = cipher_rsa.encrypt(session_key)
        cipher_aes = AES.new(session_key, AES.MODE_EAX)
        ciphertext, tag = cipher_aes.encrypt_and_digest(data)
        [ file_out.write(x) for x in (enc_session_key, cipher_aes.nonce, tag, ciphertext) ]
        file_out.close()
        os.remove('password.txt') #deleting not encrypted passwords list
        print('Done!')

        time.sleep(1)
        print('Ok, restart the Beepass.')
        break
    else: #open key is found
        print('Welcome to Beepass.')
        print(cat1)
        time.sleep(2)

        j = open('path.txt', 'r') #reading path.txt file
        w = j.read()
        j.close()

        time.sleep(1)

        lollolololo = os.path.isfile(w + 'private.pem') #reading private key
        if lollolololo == False:
            os.system('cls')

            print('\nError! Private key is not found!\n')
            print(cat4)
            time.sleep(5)
            break #exit

        os.system("cls")
        for i in range(4): #loading cat
            os.system("cls")
            print(cat3)
            time.sleep(0.5)
            os.system("cls")
            print(cat3_1)
            time.sleep(0.5)

        file_in = open('password.txt.bin', "rb") #decrypting passwords list
        file_out = open(str('password.txt.bin'[:-4]), "wb")
        private_key = RSA.import_key(open(w + "private.pem").read())
        enc_session_key, nonce, tag, ciphertext = \
        [ file_in.read(x) for x in (private_key.size_in_bytes(), 16, 16, -1) ]
        cipher_rsa = PKCS1_OAEP.new(private_key)
        session_key = cipher_rsa.decrypt(enc_session_key)
        cipher_aes = AES.new(session_key, AES.MODE_EAX, nonce)
        data = cipher_aes.decrypt_and_verify(ciphertext, tag)
        file_out.write(data)
        file_in.close()
        file_out.close()
        os.remove('password.txt.bin') #deleting encrypted passwords list

        h = open('password.txt', 'r') #reading passwords
        passwords = h.read()
        h.close()

        f = open('password.txt', "rb") #encrypting passwords list
        data = f.read(); f.close()
        file_out = open(str('password.txt')+".bin", "wb")
        recipient_key = RSA.import_key(open("open.pem").read())
        session_key = get_random_bytes(16)
        cipher_rsa = PKCS1_OAEP.new(recipient_key)
        enc_session_key = cipher_rsa.encrypt(session_key)
        cipher_aes = AES.new(session_key, AES.MODE_EAX)
        ciphertext, tag = cipher_aes.encrypt_and_digest(data)
        [ file_out.write(x) for x in (enc_session_key, cipher_aes.nonce, tag, ciphertext) ]
        file_out.close()
        os.remove('password.txt') #deleting not encrypted passwords list

        print('Done!')
        print(cat2)
        time.sleep(2)

        os.system('cls')
        print('Beepass by MONO')
        print('----------------------------------------------------')
        pressf = passwords.split('\n') #creating passwords list
        x = len(pressf)
        for i in range(len(pressf)):
            if pressf[i] == 'with_love,_mono': #creating accounts
                randomcat = random.randint(1, 2)
                if randomcat == 1:
                    print('----------------------------------------------------')
                else:
                    randomcatt = random.randint(1, 4)
                    if randomcatt == 1:
                        print('------------------' + cat5 + '----------------------------------')
                    elif randomcatt == 2:
                        print('-----------------------------------' + cat5 + '-----------------')
                    elif randomcatt == 3:
                        print('------------------' + cat6 + '----------------------------------')
                    elif randomcatt == 4:
                        print('---------------------------' + cat6 + '-------------------------')
            else:
                print(pressf[i]) #print data

        print('Press Enter to add password.')
        input() #wait for Enter
        os.system('cls')
        site = input('Enter site: ')
        login = input('Enter login: ')
        shel4denrazrabotki = input('Would you like to generate password?(y, n): ')
        if shel4denrazrabotki == 'n':
            okdude = False
            passworddd = input('Enter password: ')
        elif shel4denrazrabotki == 'y':
            okdude = True
            passlenght = int(input('Enter the lenght of password: '))
            print('Generating password...')
            for i in range(passlenght): #creating random passwords
                ssymbols = symbols.split(' ') #split the symbols str
                symbol = random.choice(ssymbols) #choice random symbol
                passsssssssssssword.append(symbol) #add it to password
            grechka = ''.join(passsssssssssssword) #creating password str
            print('Password - ' + grechka)
        else:
            exit(0)

        file_in = open('password.txt.bin', "rb") #decrypting passwords list
        file_out = open(str('password.txt.bin'[:-4]), "wb")
        private_key = RSA.import_key(open(w + "private.pem").read())
        enc_session_key, nonce, tag, ciphertext = \
        [ file_in.read(x) for x in (private_key.size_in_bytes(), 16, 16, -1) ]
        cipher_rsa = PKCS1_OAEP.new(private_key)
        session_key = cipher_rsa.decrypt(enc_session_key)
        cipher_aes = AES.new(session_key, AES.MODE_EAX, nonce)
        data = cipher_aes.decrypt_and_verify(ciphertext, tag)
        file_out.write(data)
        file_in.close()
        file_out.close()
        os.remove('password.txt.bin') #deleting encrypted passwords list

        print('Adding data...')
        m = open('password.txt', 'r') #reading passwords list
        passwords = m.read()
        m.close()
        m = open('password.txt', 'w')
        if okdude == False:
            m.write(passwords + '\n' + site + '\n' + login + '\n' + passworddd + '\nwith_love,_mono') #adding regular password
        else:
            m.write(passwords + '\n' + site + '\n' + login + '\n' + grechka + '\nwith_love,_mono') #adding generated password
        m.close()
        print('Encrypting database...')

        f = open('password.txt', "rb") #encrypting passwords list
        data = f.read(); f.close()
        file_out = open(str('password.txt')+".bin", "wb")
        recipient_key = RSA.import_key(open("open.pem").read())
        session_key = get_random_bytes(16)
        cipher_rsa = PKCS1_OAEP.new(recipient_key)
        enc_session_key = cipher_rsa.encrypt(session_key)
        cipher_aes = AES.new(session_key, AES.MODE_EAX)
        ciphertext, tag = cipher_aes.encrypt_and_digest(data)
        [ file_out.write(x) for x in (enc_session_key, cipher_aes.nonce, tag, ciphertext) ]
        file_out.close()
        f.close()
        os.remove('password.txt') #deleting not encrypted passwords list

        print('Done!')

        time.sleep(1)
        print('\nRestarting...')
