import os
from time import sleep

from numpy import choose
from Materi import Algoritma as a

def refresh():
    menu()

def menu():
    ## Menu Table
    menu = ['Algoritma','Fungsi','Himpunan', 'Induksi Matematika', 'Logika','Matrix','Relasi']
    n = 0
    os.system('cls')
    print(120*'=')
    for name in menu :
        n += 1
        print(f'{n}. {name}')

    in_menu = input(f'Pilih Materi 1-{len(menu)} = ')
    choose = int(in_menu)

    if choose == 1:
        os.system('cls')
        a.start()
    elif choose == 2:
        os.system('cls')
    elif choose == 3:
        os.system('cls')
    elif choose == 4:
        os.system('cls')
    elif choose == 5:
        os.system('cls')
    elif choose == 6:
        os.system('cls')
    elif choose == 7:
        os.system('cls')
    else:
        print('Pilihan tidak ada dalam materi ^_^')
        for i in range(1,4):
            print(i)
            sleep(1)
        refresh()        
        


