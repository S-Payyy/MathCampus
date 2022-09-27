from time import sleep


def refresh():
    import os
    os.system('cls')
    proposisis()

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

def implikasi():
    from rich.console import Console
    from rich.table import Table

    table = Table(title='Tabel Kebenaran Implikasi')

    table.add_column('p')
    table.add_column('q')
    table.add_column('p -> q')

    table.add_row('True','True','True')
    table.add_row('True','False','False')
    table.add_row('False','True','True')
    table.add_row('False','False','True')

    console = Console()
    console.print(table)

def konvers():
    from rich.console import Console
    from rich.table import Table

    table = Table(title='Tabel Kebenaran Implikasi')

    table.add_column('p')
    table.add_column('q')
    table.add_column('p -> q')

    table.add_row('True','True','True')
    table.add_row('True','False','False')
    table.add_row('False','True','True')
    table.add_row('False','False','True')

    console = Console()
    console.print(table)

def proposisis():
    from rich.console import Console
    from rich.table import Table
    import os

    jenis = ['Implikasi','Konvers','Inverse','Kontraposisi','ALL','kata(proposisi)']
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
    elif j == 1 or j == 2 or j == 3 or j == 4 or j == 5 or j == 6 :
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

    def implikasi():
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

    def ands():
        table = Table(title='"And" Table', style='cyan')
        table.add_column('p')
        table.add_column('q')
        table.add_column('p ^ q')
        if p == 'TRUE' and q == 'TRUE':
            table.add_row('T','T','T')
        elif p == 'TRUE' and q == 'FALSE':
            table.add_row('T','F','F')
        elif p == 'FALSE' and q == 'TRUE':
            table.add_row('F','T','F')
        elif p == 'FALSE' and q == 'FALSE':
            table.add_row('F','F','F')
        else:
            table.add_row('n/a','n/a','n/a')

        console = Console()
        console.print(table)  

    def ors():
        table = Table(title='"Or" Table', style='cyan')
        table.add_column('p')
        table.add_column('q')
        table.add_column('p v q')
        if p == 'TRUE' and q == 'TRUE':
            table.add_row('T','T','T')
        elif p == 'TRUE' and q == 'FALSE':
            table.add_row('T','F','T')
        elif p == 'FALSE' and q == 'TRUE':
            table.add_row('F','T','T')
        elif p == 'FALSE' and q == 'FALSE':
            table.add_row('F','F','F')
        else:
            table.add_row('n/a','n/a','n/a')

        console = Console()
        console.print(table)  

    def xors():
        table = Table(title='"XOR" Table', style='cyan')
        table.add_column('p')
        table.add_column('q')
        table.add_column('p ⊕  q')
        if p == 'TRUE' and q == 'TRUE':
            table.add_row('T','T','F')
        elif p == 'TRUE' and q == 'FALSE':
            table.add_row('T','F','T')
        elif p == 'FALSE' and q == 'TRUE':
            table.add_row('F','T','T')
        elif p == 'FALSE' and q == 'FALSE':
            table.add_row('F','F','F')
        else:
            table.add_row('n/a','n/a','n/a')

        console = Console()
        console.print(table)  

    def alls():
        implikasi()
        konvers()
        inverse()
        kontraposisi()
        ands()
        ors()
        xors()
        implikasi()

    #if p == 'TRUE' or p == 'FALSE':
    if j == 1:
        implikasi()
        input('Lanjutkan?')
        refresh()
    elif j == 2:
        konvers()
        input('Lanjutkan?')
        refresh()
    elif j == 3:
        inverse()
        input('Lanjutkan?')
        refresh()
    elif j == 4:
        kontraposisi()
        input('Lanjutkan?')
        refresh()
    elif j == 5:
        alls()
        input('Lanjutkan?')
        refresh()
    else:
        print('Jenis salah!')
        sleep(3)
        refresh()
    #else:
    #    os.system('color 4')
    #    print('Nilai Salah!')
    #    sleep(3)
    #    refresh()

