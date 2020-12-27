# -*- coding: utf-8 -*-
#!/usr/bin/python3
import colorama
from colorama import Fore as F
from colorama import Back as B
import argparse as arg
import os as sistema
import sys
import socket
# colors
BLACK = "\033[1;30m"
RED = "\033[1;31m"
GREEN = "\033[1;32m"
BLUE = "\033[1;94m"
YELLOW = "\033[1;33m"
CIANO = "\033[1;36m"
LIGHT_GREEN = "\033[1;92m"
WHITE = "\033[1;97m"
MAGENTA = "\033[1;35m"
LIGHT_RED = "\033[1;91m"
GREY = "\033[1;37m"
RESET = "\033[0;0m"
# fim

script = sys.argv[0]
sistema.system('cls' if sistema.name == 'nt' else 'reset')


def arruma(url):
    if url[-1] != "/":
        url = url + "/"
    if url[:7] != "http://" and url[:8] != "https://":
        url = "http://" + url
    return url


index = """____________________________________________________________
{}
███            ▄█    █▄       ▄████████         ▄██████▄   ▄██████▄  ████████▄     ▄████████ 
▀█████████▄   ███    ███     ███    ███        ███    ███ ███    ███ ███   ▀███   ███    ███ 
   ▀███▀▀██   ███    ███     ███    █▀         ███    █▀  ███    ███ ███    ███   ███    █▀     
    ███   ▀  ▄███▄▄▄▄███▄▄  ▄███▄▄▄           ▄███        ███    ███ ███    ███   ███        
    ███     ▀▀███▀▀▀▀███▀  ▀▀███▀▀▀          ▀▀███ ████▄  ███    ███ ███    ███ ▀███████████ 
    ███       ███    ███     ███    █▄         ███    ███ ███    ███ ███    ███          ███ 
    ███       ███    ███     ███    ███        ███    ███ ███    ███ ███   ▄███    ▄█    ███ 
   ▄████▀     ███    █▀      ██████████        ████████▀   ▀██████▀  ████████▀   ▄████████▀  
  {}Scythe Port Scanner                 
{}Monge: {}https://github.com/march0s1as
{}Programas: {}https://github.com/Gl4sya
{}Python God: {}https://github.com/Slayyer-dev
____________________________________________________________""".format(F.CYAN, F.RED, F.CYAN, F.WHITE, F.CYAN, F.WHITE, F.CYAN, F.WHITE)
manual = """
{}[INFO] {}Parãmetros:
--ip        IP (--ip www.site.com ou 192.168.0.1).
--scan      Faz scan da porta 0 até a porta 65.536 (--scan).
--portas    Faz um scan nas portas que o usuário escolheu (--portas portas.txt).
--threads   Tempo para cada requisição, também utilizado para burlar firewall (--threads 5).
--verbose   Scanner em tempo real.
{}[INFO] {}Na prática:
Scanner completo de todas as portas:
python3 {} --ip <IP> --scan
Scanner com um número X de portas:
python3 {} --ip <IP> --portas <portas.txt>
Utilizando a opção "threads":
python3 {} --ip <IP> --scan --threads 5
OBS: Pode utilizar está opção com o parãmetro "--portas".
Utilizando a opção "verbose":
python3 {} --ip <IP> --scan --verbose
OBS: Pode utilizar está opção com o parãmetro "--portas".
""".format(F.CYAN, F.WHITE, F.CYAN, F.WHITE, script, script, script, script)

if len(sys.argv) == 1:
    print(index + "\n" + manual)
    exit()

parser = arg.ArgumentParser(description="Scythe Port Scanner by z4gan")
parser.add_argument("--ip", action='store', help=" IP / (--ip 192.168.0.1).")
parser.add_argument("--scan", action='store_true',
                    help="Faz scan da porta 0 até a porta 65.536 (--scan).")
parser.add_argument("--portas", action='store',
                    help="Faz um scan nas portas que o usuário escolheu (--portas portas.txt).")
parser.add_argument("--threads", action='store', type=int, default="1",
                    help="Tempo para cada requisição, também utilizado para burlar firewall (--threads 5).")
parser.add_argument("--verbose", action='store_true',
                    help="Scanner em tempo real.")
param = parser.parse_args()

if not param.ip:
    print(F.RED + "Insira um IP! (--ip IP)")
    exit()
if not param.scan and not param.portas:
    print(F.RED + "Insira o tipo de scan! (--scan ou --portas PORTAS.txt)" + F.WHITE + "")
    exit()

for num in range(0, 11):
    if str(num) in param.ip[0]:
        usar = 0
        break
    elif num == 10:
        print(F.RED + "Insira um endereço de IP válido!" + F.WHITE)
        exit()

if usar == 1:
    host = arruma(param.ip)
else:
    host = param.ip

if param.portas:
    portas = open(param.portas, "r")
    portas = portas.readlines()
    portas = [porta.replace("\n", "") for porta in portas]
    tipo = "Com base nas portas escolhidas pelo usuário... Portas: {}, {}, {} ... {}".format(
        portas[0], portas[1], portas[2], portas[-1])
else:
    portas = []
    faz = [portas.append(porta) for porta in range(0, 65536)]
    tipo = "Todas portas existentes... Portas: {}, {}, {} ... {}".format(
        portas[0], portas[1], portas[2], portas[-1])

print(index)
print("\n" + F.CYAN + "[+]" + F.WHITE + " Endereço IP:", host)
print(F.CYAN + "[+]" + F.WHITE + " Tipo de scan:", tipo)
print("\n" + F.GREEN + "[*]" + F.WHITE +
      " Iniciando scan no host {}".format(host))
print()

abertas = []
for PORTA in portas:
    requisicao = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    requisicao.settimeout(param.threads)
    retorno = requisicao.connect_ex((host, int(PORTA)))
    if param.verbose:
        if retorno == 0:
            print(F.GREEN + "[ABERTA]" + F.WHITE +
                  " Porta encontra-se aberta:", PORTA)
            abertas.append(PORTA)
        else:
            print(F.RED + "[FECHADA]" + F.WHITE +
                  " Porta encontra-se fechada:", PORTA)
    else:
        if retorno == 0:
            print(F.GREEN + "[ABERTA]" + F.WHITE +
                  " Porta encontra-se aberta:", PORTA)
            abertas.append(PORTA)
        else:
            continue

print(F.GREEN + "\n[+]" + F.WHITE +
      " Total de portas testadas: ", str(len(portas)))
print(F.GREEN + "[+]" + F.WHITE +
      " Total de portas abertas: ", str(len(abertas)))
print(F.WHITE + "    São as portas:", abertas)
print(F.GREEN + "\nFinalizado!" + F.WHITE + "")
exit()
