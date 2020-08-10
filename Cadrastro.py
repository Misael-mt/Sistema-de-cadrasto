#-*-coding:utf8;-*-
#qpy:console
from menu.menu import *
import requests
import time
import sqlite3 as sql
import os 
# cores
vm='\033[1;31m'
vd='\033[1;32m'
az='\033[1;36m'
fn='\033[m'


# input
def inpu():
    try:
         
        global cep
        global nome
        global tell    
        nome = str(input(f'{vd}  nome{fn}{az} =+> {fn}'))
        cep = input(f'{vd}  cep {fn}{az}=+> {fn}')
        tell = input(f'{vd}  telefone{fn}{az} =+> {fn}')
    except ValueError:
        print('  [!] valor invalido tente novamente ')

# MENU

time.sleep(1)
os.system('clear')
main()
        
inp = int(input(f'{az}  =+> {fn}'))
    
if inp == 1:
    inpu()
elif inp == 2:
    print('\n')
    exit()
else:
    print('valor invalido ')
             
    
    
if len(cep) == 8:
    
    req = requests.get('https://viacep.com.br/ws/{}/json/'.format(cep))
    
    n1 = req.json()
    val = n1.values()
    resul = 'São Paulo' in val
    if resul == True:
        banco = sql.connect('database')
        curso = banco.cursor()
        try:
            curso.execute("CREATE TABLE cadrasto (NOME text, CEP integer, TELEFONE integer)")
        except:
            curso.execute(f"INSERT INTO cadrasto VALUES ('{nome}',{cep},{tell})")
            banco.commit()
            banco.close()
            time.sleep(1)
            print(' [+] analisando os dados ...')
            time.sleep(1)
            print(' nome ✓')
            time.sleep(1)
            print (' cep ✓')
            time.sleep(1)
            print (' telefone ✓')
            time.sleep(1)
            print (f'{vd} [✓] cadastro realizado {fn}')
            
    elif resul != True:               
         print('  \033[1;31mOps [ ERRO ] o cep informado não \n  pertence a estado de são Paulo  \n  [!] Para poder se cadrasta voce\n  precisa ser de são Paulo \033[m')
       
else:
    print('\033[1;31m [!] formato inválido \n [!] Digite os dados corretamente  !!\033[m')
       
    
