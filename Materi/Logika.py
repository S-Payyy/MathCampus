from time import sleep

def refresh():
    import os
    os.system('cls')
    logic_menu()

def proposisi():
    p = input('Masukkan Kata Pertama : ')
    q = input('Masukkan Kata Kedua : ')

    Nots = ' Tidak benar '
    And = p + ' dan ' + q
    Or = p + ' atau ' + q
    Not_p = Nots + p
    Not_q = Nots + q
    q_or_not_p = q + ' atau ' + Nots + p 
    p_or_not_q = p + ' atau ' + Nots + q 
    not_p_and_not_q = Nots + p + ' dan ' + Nots + q
    not_q_and_not_p = Nots + q + ' dan ' + Nots + p
    not_p_or_not_q = Nots + p + ' atau ' + Nots + q
    not_q_or_not_p = Nots + q + ' atau ' + Nots + p

    print(f'\np ^ q = {And}\np v q = {Or}\n~p = {Not_p}\n~q = {Not_q}\nq v ~p = {q_or_not_p}\np v ~q = {p_or_not_q}\n~p ^ ~q = {not_p_and_not_q}\n~q ^ ~p = {not_q_and_not_p}\n~p v ~q = {not_p_or_not_q}\n~q v ~p = {not_q_or_not_p}\n')

def ands():
    def AND (a, b):
        if a == 1 and b == 1:
            return 1
        else:
            return 0
    from rich.table import Table
    from rich.console import Console
    c = Console()
    tabel = Table(title='And Gate')
    tabel.add_column('a')
    tabel.add_column('b')
    tabel.add_column('a ^ b')
    data_p = input('Masukkan nilai a secara berurutan > ')
    p = [int(x) for x in data_p]
    data_q = input('Masukkan nilai b secara berurutan > ')
    q = [int(x) for x in data_q]
    for (i,j) in zip(p,q):
        tabel.add_row(str(i),str(j),str(AND(i,j)))
    
    c.print(tabel)
    
def ors():
    def OR (a,b):
        if a == 1 or b == 1:
            return 1
        else:
            return 0

    from rich.table import Table
    from rich.console import Console
    c = Console()
    tabel = Table(title='And Gate')
    tabel.add_column('a')
    tabel.add_column('b')
    tabel.add_column('a v b')
    data_p = input('Masukkan nilai a secara berurutan > ')
    p = [int(x) for x in data_p]
    data_q = input('Masukkan nilai b secara berurutan > ')
    q = [int(x) for x in data_q]
    for (i,j) in zip(p,q):
        tabel.add_row(str(i),str(j),str(OR(i,j)))
    
    c.print(tabel)

def xors():
    def XOR (a,b):
        if a != b:
            return 1
        else:
            return 0

    from rich.table import Table
    from rich.console import Console
    c = Console()
    tabel = Table(title='And Gate')
    tabel.add_column('a')
    tabel.add_column('b')
    tabel.add_column('a ⊕  b')
    data_p = input('Masukkan nilai a secara berurutan > ')
    p = [int(x) for x in data_p]
    data_q = input('Masukkan nilai b secara berurutan > ')
    q = [int(x) for x in data_q]
    for (i,j) in zip(p,q):
        tabel.add_row(str(i),str(j),str(XOR(i,j)))
    
    c.print(tabel)

def implikasi():
    from rich.table import Table
    from rich.console import Console
    table = Table(title='Implikasi Table', style='cyan')
    table.add_column('p')
    table.add_column('q')
    table.add_column('p -> q')
    if p == 'TRUE' and q == 'TRUE':
        table.add_row('T','T','T')
    elif p == 'TRUE' and q == 'FALSE':
        table.add_row('T','F','F')
    elif p == 'FALSE' and q == 'TRUE':
        table.add_row('F','T','T')
    elif p == 'FALSE' and q == 'FALSE':
        table.add_row('F','F','T')
    else:
        table.add_row('n/a','n/a','n/a')
    console = Console()
    console.print(table)  

def konvers():
    from rich.table import Table
    from rich.console import Console
    table = Table(title='Konvers Table', style='cyan')
    table.add_column('p')
    table.add_column('q')
    table.add_column('q -> p')
    if p == 'TRUE' and q == 'TRUE':
        table.add_row('T','T','T')
    elif p == 'TRUE' and q == 'FALSE':
        table.add_row('T','F','T')
    elif p == 'FALSE' and q == 'TRUE':
        table.add_row('F','T','F')
    elif p == 'FALSE' and q == 'FALSE':
        table.add_row('F','F','T')
    else:
        table.add_row('n/a','n/a','n/a')
    console = Console()
    console.print(table)  

def inverse():
    from rich.table import Table
    from rich.console import Console
    table = Table(title='Invers Table', style='cyan')
    table.add_column('p')
    table.add_column('q')
    table.add_column('~p')
    table.add_column('~q')
    table.add_column('~p -> ~q')
    if p == 'TRUE' and q == 'TRUE':
        table.add_row('T','T','F','F','T')
    elif p == 'TRUE' and q == 'FALSE':
        table.add_row('T','F','F','T','T')
    elif p == 'FALSE' and q == 'TRUE':
        table.add_row('F','T','T','F','F')
    elif p == 'FALSE' and q == 'FALSE':
        table.add_row('F','F','T','T','T')
    else:
        table.add_row('n/a','n/a','n/a')
    console = Console()
    console.print(table)  

def kontraposisi():
    from rich.table import Table
    from rich.console import Console
    table = Table(title='Kontraposisi Table', style='cyan')
    table.add_column('p')
    table.add_column('q')
    table.add_column('~q -> ~p')
    if p == 'TRUE' and q == 'TRUE':
        table.add_row('T','T','T')
    elif p == 'TRUE' and q == 'FALSE':
        table.add_row('T','F','F')
    elif p == 'FALSE' and q == 'TRUE':
        table.add_row('F','T','T')
    elif p == 'FALSE' and q == 'FALSE':
        table.add_row('F','F','T')
    else:
        table.add_row('n/a','n/a','n/a')
    console = Console()
    console.print(table)  

def logic_menu():
    from Materi import Logika
    from rich.console import Console
    from rich.table import Table
    import os

    jenis = ['Implikasi','Konvers','Inverse','Kontraposisi','ALL','kata(proposisi)','and ( ^ )','or ( v )','xor ( ⊕  )']
    table_menu = Table()
    table_menu.add_column('Daftar Materi Logika')
    n = 0

    for i in jenis:
        n+=1
        table_menu.add_row(f'{n}. {i}')

    c = Console()
    c.print(table_menu)

    j = int(input('Masukkan Jenis Logika : '))
    if j == 6:
        proposisi()
        input('Lanjutkan?')
        refresh()
    elif j == 7:
        ands()
        input('Lanjutkan?')
        refresh()
    elif j == 8:
        ors()
        input('Lanjutkan?')
        refresh()
    elif j == 9:
        xors()
        input('Lanjutkan?')
        refresh()
    elif j == 1 or j == 2 or j == 3 or j == 4 or j == 5 or j == 6:
        global p
        global q
        p = input('\nMasukkan nilai p : ').upper()
        q = input('Masukkan nilai q : ').upper()
        print('\n')
        if p == 'TRUE':
            if q == 'TRUE':
                pass
            elif q == 'FALSE':
                pass
            else:
                os.system('color 4')
                print('Nilai p atau q tidak valid!')
                sleep(3)
                refresh() 
        elif p == 'FALSE':
            if q == 'TRUE':
                pass
            elif q == 'FALSE':
                pass
            else:
                os.system('color 4')
                print('Nilai p atau q tidak valid!')
                sleep(3)
                refresh() 
        else:
            os.system('color 4')
            print('Nilai p atau q tidak valid!')
            sleep(2)
            refresh() 
    else:
        os.system('color 4')
        print('Jenis Logika tidak ada dalam daftar!')
        sleep(3)
        refresh()

    def alls():
        implikasi()
        konvers()
        inverse()
        kontraposisi()
        implikasi()

    if j == 1:
        implikasi()
        input('Lanjutkan? ')
        refresh()
    elif j == 2:
        konvers()
        input('Lanjutkan? ')
        refresh()
    elif j == 3:
        inverse()
        input('Lanjutkan? ')
        refresh()
    elif j == 4:
        kontraposisi()
        input('Lanjutkan? ')
        refresh()
    elif j == 5:
        alls()
        input('Lanjutkan? ')
        refresh()
    elif j == 7:
        ands()
        input('Lanjutkan? ')
        refresh()
    elif j == 8:
        ors()
        input('Lanjutkan? ')
        refresh()
    elif j == 9:
        xors()
        input('Lanjutkan? ')
        refresh()
    else:
        print('Jenis salah!')
        sleep(3)
        refresh()

