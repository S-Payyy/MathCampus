# code create 23:25 25 Sept 2022 
# created by xcl404
# codename 'Matematika Diskrit'
import os
from Materi import menu as m

codename = 'Discrete Mathematics'
version = 1.0
desc = 'Matematika diskrit atau diskret adalah cabang matematika yang membahas segala sesuatu yang bersifat diskrit. Diskrit disini artinya tidak saling berhubungan (lawan dari kontinu). Objek yang dibahas dalam Matematika Diskrit - seperti bilangan bulat, graf, atau kalimat logika - tidak berubah secara kontinu, tetapi memiliki nilai yang tertentu dan terpisah. Beberapa hal yang dibahas dalam matematika ini adalah teori himpunan, teori kombinatorial, teori bilangan, permutasi, fungsi, rekursif, teori graf, dan lain-lain. Matematika diskrit merupakan mata kuliah utama dan dasar untuk bidang ilmu komputer atau informatika.'

os.system('color b')
print(codename)
print(f'version = {version}\n')
print(f'Description :\n{desc}\n')
print(120*"=")

m.menu()
