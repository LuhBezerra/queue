# Fila de Espera
Utilização de threads e a estrutura de dados deque para simulação de uma fila de espera. 

## Como funciona

1º Dados do cliente 

	Todo cliente informa NOME e IDADE

2º Entrada na fila de espera 

	2.1 Cada novo cliente a ser atendido vai para o final da fila 

	2.2 Se o cliente for VIP(escolha feita de forma randômica), ele vai para o início da fila, não importa quantos clientes já estão lá e se são VIPs ou não

3º Atendimento ao próximo cliente 

	3.1 O próximo cliente a ser chamado é sempre o primeiro da fila
 
	3.2 Atendimento expresso: A cada 10 clientes atendidos, o próximo cliente será sempre o último da fila

4º Gerador de dados aleatórios 

	4.1 O programa gera dados aleatórios de clientes e os insere na fila a cada 1 segundo 
	4.2 O programa simula o atendimento de um novo cliente a cada 2 segundos

5 Exibição de informações 
	
	5.1 A cada alteração na fila o programa mostra o estado da fila, com as seguintes informações: 
	
    	* Cliente no Início da Fila
	* Tamanho da Fila
	* Cliente no Final da Fila

### Execução

```
pithon3 main.py
```

