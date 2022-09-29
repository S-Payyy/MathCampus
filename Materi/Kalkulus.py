def PersamaanLinear():
    import os
    from rich.table import Table
    from rich.console import Console
    console = Console()

    def Bentuk1():
        tabel_bentuk1 = Table()
        tabel_bentuk1.add_column('Example Code')
        tabel_bentuk1.add_row('ax + b = cx + d')
        tabel_bentuk1.add_row('\n"10x-4 = 5x+7" Menjadi "10 -4 5 7"')
        tabel_bentuk1.add_row('\nCatatan: ')
        tabel_bentuk1.add_row('- Masukkan soal tanpa "x,=,+"')
        tabel_bentuk1.add_row('- Gunakan "-" untuk angka yang bernilai negatif')
        tabel_bentuk1.add_row('- Pisahkan setiap nilai dengan space')
        tabel_bentuk1.add_row('- Masukkan soal tanpa "x,=,+"')

        console.print(tabel_bentuk1)

        m = input('Masukkan soal : ')
        soal = m.split(' ')

        ax = int(soal[0])
        b = int(soal[1])
        cx = int(soal[2])
        d = int(soal[3])

        x1 =  ax+(-cx)
        x2 = d-b
        xx1 = abs(x1)
        xx2 = abs(x2)
        x = str(xx2)+'/'+str(xx1)
        try:
            y = xx2/xx1
        except:
            y = 0
        print(f'{ax}x + ({b}) = {cx}x + ({d})')
        print(f'> hasil adalah {x} atau {y:.2f} atau {int(y)}\n')

    def Bentuk2():
        pass
    def Bentuk3():
        pass
    def Bentuk4():
        pass

    tabel = Table(title='Persamaan Linear')
    tabel.add_column('Bentuk Persamaan Linear')
    bentuk = ['Bentuk 1', 'Bentuk 2', 'Bentuk 3', 'Bentuk 4']
    n = 0
    for nama in bentuk:
        n += 1
        tabel.add_row(f'{n}. {nama}')
    console.print(tabel)

    m = input('Pilih Bentuk Persamaan Linear : ')
    menu = int(m)

    if menu == 1:
        os.system('cls')
        Bentuk1()
    elif menu == 2:
        os.system('cls')
        Bentuk2()
    elif menu == 3:
        os.system('cls')
        Bentuk3()
    elif menu == 4:
        os.system('cls')
        Bentuk4()
    else:
        os.system('cls')
        print('Bentuk Tidak ada dalam Persamaan Linear\n')
