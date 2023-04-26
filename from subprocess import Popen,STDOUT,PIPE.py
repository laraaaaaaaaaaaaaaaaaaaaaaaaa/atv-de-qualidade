from subprocess import Popen,STDOUT,PIPE,call
from time import sleep 

print('nome da rede:')
nome = input () 
manipulador = Popen ('netsh wlan connect {}' .format(nome),shell=True,stdout=PIPE,sterr=STDOUT,stdin=PIPE)
sleep(2)
manipulador.stdin.write(b'cabo123\n')
while manipulador.poll() == Nome:
    print(manipulador.stdout.readline().strip ())
if call ('ping -n 1 www.google.com') ==0:
    print('conectado')
else:
    print("tentativa falha")