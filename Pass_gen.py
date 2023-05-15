import random
import time

# Creating function which will create random passwords and save it in the file


def password(length, qtt, kod):

    small_letters = 'abcdefghijklmnoprstuvwxyz'
    capital_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    digits = '0123456789'
    special_signs = '!@#$%^&*()_-/.,;][}{":?><,}]'

    pula_znakow = ''

    if kod[0] == '1':
        pula_znakow += small_letters
    if kod[1] == '1':
        pula_znakow += capital_letters
    if kod[2] == '1':
        pula_znakow += digits
    if kod[3] == '1':
        pula_znakow += special_signs

    plik = open("haslo","w")

    for i in range(qtt):
        password = "".join(random.sample(pula_znakow, length))
        plik.write(password + '\n')

    plik.close()
    print("\nYour passwords have been secured in file named: 'haslo'. KEEP IT SAFE!")


length = int(input('set the password length  '))
qtt = int(input('set how many passwords has to be generated  '))
print('If u want your passwords contain: ')
time.sleep(3)
small = input('Small letters: YES - 1    NO - 0  ')
time.sleep(1)
capital = input('Capital letters: YES - 1    NO - 0  ')
time.sleep(1)
digits = input('Digits:         YES - 1    NO - 0  ')
time.sleep(1)
special = input('Special Signs:   YES - 1    NO - 0  ')

code = small + capital + digits + special

password(length, qtt, code)








