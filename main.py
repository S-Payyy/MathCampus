# code create 23:25 25 Sept 2022 
# created by xcl404
# codename 'Matematika Diskrit'
from rich.progress import track
from rich.markdown import Markdown
from rich.console import Console
import time
from Materi import menu as m
import os
c = Console()
codename = '# Discrete Mathematics Tools'
version = 1.8
date = '29 Sept 2022'
desc = f'Code Created by Xcl404\nIg : s_payyy01\nLast Update : v{version} ({date})\nDetails :\n- Style Update\n- update on "Logika"\n- New "Kalkulus"'

os.system('cls')
md = Markdown(codename, style='purple')
c.print(md)
print(f'\nversion = {version}')
print(f'{desc}\n')

for i in track(range(3), description='Loading. . .'):
    time.sleep(1)

m.menu()
