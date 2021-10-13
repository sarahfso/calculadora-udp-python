from socket import *
serverName = 'localhost'
serverPort = 12000
clientSocket = socket(AF_INET, SOCK_DGRAM)

print('Calculadora remota')
numero1 = input ('Primeiro numero: ')
numero2 = input ('Segundo numero: ')
operador = input ('Operador: (+ / * -) ')

clientSocket.sendto(numero1.encode(),(serverName,serverPort))
clientSocket.sendto(numero2.encode(),(serverName,serverPort))
clientSocket.sendto(operador.encode(),(serverName,serverPort))

resposta,serverAddress = clientSocket.recvfrom(2048)
print('Seu resultado: ', resposta.decode())

clientSocket.close()
