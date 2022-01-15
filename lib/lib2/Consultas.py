from requests import get
import os
import sys
import time

def menu():
	print("""
Opcoes

	  \033[34mDEVTOOLS\033[m
	    by \033[33m@SAS\033[m
	    
          \033[44mVersao: 1.0\033[m
          
  Opcoes:
	
  \033[36m[\033[m1\033[36m]\033[m consultasv3
  \033[36m[\033[m2\033[36m]\033[m geoip

  \033[36m[\033[m90\033[36m]\033[m \033[31m???\033[m
  \033[36m[\033[m91\033[36m]\033[m \033[31mVoltar\033[m
  \033[36m[\033[m92\033[36m]\033[m \033[31mSair\033[m
""")

clear = lambda: os.system('clear')

menu()

kk = int(input('\033[34m===>\033[m '))

if kk == (1):
	clear()
	exec(get('https://raw.githubusercontent.com/T3rMuX0/consulta-v3/master/consultav3.py').text)
    
if kk == (2):
	clear()
	exec(get('https://raw.githubusercontent.com/bydeathlxncer/IPplugg/main/IPplugg.py').text)

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

