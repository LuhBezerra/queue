import string
import time
import timeit
import collections 
import random
from threading import Thread

fila = collections.deque([]) 
tamanho = len(fila)

def gerarCliente(size=5, chars=string.ascii_uppercase + string.digits):
    nome = ''.join(random.choice(chars) for _ in range(size))
    idade = random.randint(18,60)

    dados = (nome,idade)
    
    return dados

def inserir_na_fila(nome,quantClientes):
    for eh_vip in range(quantClientes):
        eh_vip = random.choice([True, False])

        if eh_vip == True:
            fila.appendleft(gerarCliente())
            #print("Eh vip >>>", fila)

        else:
            fila.append(gerarCliente())
            #print("Nao eh vip >>>",fila)
        
        
        print("Cliente no Inicio da Fila: ", fila[0],"\nTamanho da Fila: ",
                len(fila),"\nCliente no Final da Fila: ", fila[tamanho-1])

        print()
        time.sleep(1)  

def atender_cliente(nome):
    atendeu = 0
    atendimento = 1
    while len(fila) != 0:
        
        if atendeu == 10: # atendimento expresso

            cliente_atendido = fila.pop()
            print("\n>>> Atendimento Expresso(%d) "%atendimento,cliente_atendido)
            atendeu = 0
            atendimento += 1
        else:
            cliente_atendido = fila.popleft()
            print(">>> Atendimento(%d) "%atendimento,cliente_atendido)
            atendeu += 1
            atendimento += 1

        print()
        #print("Fila Atual: ", fila)

        time.sleep(2)

def play(quantidadeClientes):
    insere = Thread(target=inserir_na_fila,args=["Entrando na fila ",quantidadeClientes])
    atende = Thread(target=atender_cliente,args=["Sendo atendido ",])

    insere.start()
    atende.start()

quantidade_clientes = int(input("Informe a quantidade de clientes que deseja atender >>> "))
print()
play(quantidade_clientes)