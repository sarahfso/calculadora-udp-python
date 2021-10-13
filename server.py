from socket import *
serverPort = 12000
serverSocket = socket(AF_INET, SOCK_DGRAM)
serverSocket.bind(('', serverPort))
print('The server is ready to receive')
while 1:
    numero1, clientAddress = serverSocket.recvfrom(2048)
    print('Numero 1 recebido: ', numero1)
    numero2, clientAddress = serverSocket.recvfrom(2048)
    print('Numero 2 recebido: ', numero2)
    operador, clientAddress = serverSocket.recvfrom(2048)
    print('Operador recebido: ', operador)
    print('Calculando...')
	
    if str(operador.decode()) == '+':
        resposta = int(numero1.decode()) + int(numero2.decode())
        serverSocket.sendto(str(resposta).encode(),clientAddress)
    elif str(operador.decode()) == '-':
        resposta = int(numero1.decode()) - int(numero2.decode())
        serverSocket.sendto(str(resposta).encode(),clientAddress)
    elif str(operador.decode()) == '/':
        resposta = int(numero1.decode()) / int(numero2.decode())
        serverSocket.sendto(str(resposta).encode(),clientAddress)
    elif str(operador.decode()) == '*':
        resposta = int(numero1.decode()) * int(numero2.decode())
        serverSocket.sendto(str(resposta).encode(),clientAddress)