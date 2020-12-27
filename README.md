# ScytheScanPort

![](https://image.myanimelist.net/ui/_3fYL8i6Q-n-155t3dn_4hksVs3MIJxHadG7A7FI_oTy9pL-UqrC-cycJtDkuZzC)

--ip        IP (--ip www.site.com ou 192.168.0.1).

--scan      Faz scan da porta 0 até a porta 65.536 (--scan).

--portas    Faz um scan nas portas que o usuário escolheu (--portas portas.txt).

--threads   Tempo para cada requisição, também utilizado para burlar firewall (--threads 5).

--verbose   Scanner em tempo real.

________________________________________________________________________________________________________________________

  Scanner completo de todas as portas                                                      

python3 {} --ip <IP> --scan
  
Scanner com um número X de portas
  
  python3 {} --ip <IP> --portas <portas.txt>

Utilizando a opção "threads"
  
  python3 {} --ip <IP> --scan --threads 5

OBS: Pode utilizar está opção com o parãmetro "--portas".
  

Utilizando a opção "verbose"
  
  python3 {} --ip <IP> --scan --verbose
  
OBS: Pode utilizar está opção com o parãmetro "--portas".


                                                                        ===> Use pip install colorama
