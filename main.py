import time
import requests
import os
import emoji
import colorama as cor
import re

# reset color auto
cor.init(autoreset=True)

tempo_inicial = time.time()

# limpar terminal
def clear():
  try:
    os.system('cls')
  except:
    os.system('clear')
# main
def main(url,wordlist):
    clear();
    print(f'''
{cor.Fore.BLUE}
{emoji.emojize(':magnifying_glass_tilted_right:').ljust(50,line)}
|{"iniciando".upper().center(50)}|
{emoji.emojize(':magnifying_glass_tilted_right:').rjust(50,line)}
{cor.Fore.RESET} ''')
    cont_global = 0
    cont = 0
    # open wordlist
    lista = open(pasta+"/"+wordlist_arquivos[int(wordlist) -1])

    # read lines of wordlist
    linhas = lista.readlines()
    diretorios = []

    for linha in linhas:
        cont_global+=1
        diretorio_atual = f"{url}/{linha}"
        # request
        rq = requests.get(f"{url}/{linha}")
        # status of request
        if rq.status_code == 200:
            # GOOD
            print(f"{cor.Fore.GREEN}{emoji.emojize(':check_mark:')} - {diretorio_atual}")
            diretorios.append(diretorio_atual);
            cont+=1
        else:
            # BAD
            print(f"{cor.Fore.RED}{emoji.emojize(':cross_mark:')} - {diretorio_atual}")
            cont = cont
    clear()
    # Return
    print(f'''
{cor.Fore.BLUE}
{emoji.emojize(':magnifying_glass_tilted_right:').ljust(50,line)}
|{"Resposta".upper().center(50)}|
{emoji.emojize(':magnifying_glass_tilted_right:').rjust(50,line)}
{cor.Fore.RESET} ''')
    print(f"{cor.Fore.YELLOW}{'Número de diretorios consultados:'.upper()} {cor.Fore.GREEN}{cont_global}")
    print(f"{cor.Fore.YELLOW}{'Número de diretorios encontrados:'.upper()} {cor.Fore.GREEN}{cont}")
    print(f'''{cor.Fore.YELLOW}{'Diretorios encontrados:'.upper()}''')
    for i in diretorios:
        print(f"{cor.Fore.GREEN}{i}")
    print(f'''{cor.Fore.YELLOW}{'Tempo de execução:'.upper()}''')
    print(f"{cor.Fore.GREEN}{str(time.time() - tempo_inicial)} segundos");
    print(f'''\n{cor.Fore.BLUE}{' X-MR '.center(50,'=')}''')


line  = "-";
clear()
host  = str(input(f'''
{cor.Fore.BLUE}
{emoji.emojize(':magnifying_glass_tilted_right:').ljust(50,line)}
|{"Bem vindo ao X-MR".center(50)}|
{emoji.emojize(':magnifying_glass_tilted_right:').rjust(50,line)}
{cor.Fore.YELLOW}
{str("Digite a url nesse modelo 'https://host' ou 'http://host'").upper()}
==>{cor.Fore.RESET}'''));

# host input verification
def Find(string):
    regex = r"(?i)\b((?:https?://|[a-z0-9.\-]+[.][a-z]{2,4}/)(?:[^\s()<>]+|\(([^\s()<>]+|(\([^\s()<>]+\)))*\))+(?:\(([^\s()<>]+|(\([^\s()<>]+\)))*\)|[^\s`!()\[\]{};:'\".,<>?«»“”‘’]))"
    url = re.findall(regex,string)       
    return [x[0] for x in url] 
while Find(host) == []:
    clear()
    host  = str(input(f'''
{cor.Fore.BLUE}
{emoji.emojize(':magnifying_glass_tilted_right:').ljust(50,line)}
|{"Bem vindo ao X-MR".center(50)}|
{emoji.emojize(':magnifying_glass_tilted_right:').rjust(50,line)}
{cor.Fore.RED}
{str("Digite a url nesse modelo 'https://host' ou 'http://host'").upper()}
==>{cor.Fore.RESET}'''));
    
print()

# wordlist input verification
def index_choice(lista,i):
    if(int(i) in lista):
        return True
    else:
        return False

pasta = './wordlist'
wordlist_arquivos = []
index_arquivos = []

for diretorio, subpastas, arquivos in os.walk(pasta):
    wordlist_arquivos = arquivos
    for arquivo in arquivos:
        index_arquivos.append(arquivos.index(arquivo)+1)
        print(f"{arquivos.index(arquivo)+1} - {arquivo}")

wordlist = str(input(f'''
escolha somente o número
{cor.Fore.BLUE}
WORDLIST ==>{cor.Fore.RESET} '''))

while index_choice(index_arquivos,wordlist) != True:
     wordlist = str(input(f'''
escolha somente o número
{cor.Fore.RED}
WORDLIST ==>{cor.Fore.RESET} '''))

main(host,wordlist)