def multi_and():
    def AND (a, b):
        if a == 1 and b == 1:
            return 1
        else:
            return 0

    from rich.table import Table
    from rich.console import Console

    c = Console()
    tabel = Table(title='And Gate')
    tabel.add_column('p')
    tabel.add_column('q')
    tabel.add_column('p ^ q')

    data_p = input('Masukkan nilai p secara berurutan > ')
    p = [int(x) for x in data_p]
    data_q = input('Masukkan nilai p secara berurutan > ')
    q = [int(x) for x in data_q]

    for (i,j) in zip(p,q):
        tabel.add_row(str(i),str(j),str(AND(i,j)))
    
    c.print(tabel)
