from socket import *
import time
import os

serverName = '192.168.100.92'
serverPort = 6000

clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName, serverPort))

titulo = clientSocket.recv(1024)
os.system('cls')
print(f'\n{titulo.decode()}\n')

user_name = str(input('\nDigite o seu nome: '))
clientSocket.send(user_name.encode())
os.system('cls')

questao1 = clientSocket.recv(1024)
print('\nQuestão 1)\n')
print(questao1.decode())
resposta1 = str(input('\nResposta: '))
os.system('cls')
clientSocket.send(resposta1.encode())
resultado1 = clientSocket.recv(1024)
print(f'\n{resultado1.decode()}')
time.sleep(4)
os.system('cls')

questao2 = clientSocket.recv(1024)
print('\nQuestão 2)\n')
print(questao2.decode())
resposta2 = str(input('\nResposta: '))
os.system('cls')
clientSocket.send(resposta2.encode())
resultado2 = clientSocket.recv(1024)
print(f'\n{resultado2.decode()}')
time.sleep(4)
os.system('cls')

questao3 = clientSocket.recv(1024)
print('\nQuestão 3)\n')
print(questao3.decode())
resposta3 = str(input('\nResposta: '))
os.system('cls')
clientSocket.send(resposta3.encode())
resultado3 = clientSocket.recv(1024)
print(f'\n{resultado3.decode()}')
time.sleep(4)
os.system('cls')

questao4 = clientSocket.recv(1024)
print('\nQuestão 4)\n')
print(questao4.decode())
resposta4 = str(input('\nResposta: '))
os.system('cls')
clientSocket.send(resposta4.encode())
resultado4 = clientSocket.recv(1024)
print(f'\n{resultado4.decode()}')
time.sleep(4)
os.system('cls')

questao5 = clientSocket.recv(1024)
print('\nQuestão 5)\n')
print(questao5.decode())
resposta5 = str(input('\nResposta: '))
os.system('cls')
clientSocket.send(resposta5.encode())
resultado5 = clientSocket.recv(1024)
print(f'\n{resultado5.decode()}')
time.sleep(4)
os.system('cls')

questao6 = clientSocket.recv(1024)
print('\nQuestão 6)\n')
print(questao6.decode())
resposta6 = str(input('\nResposta: '))
os.system('cls')
clientSocket.send(resposta6.encode())
resultado6 = clientSocket.recv(1024)
print(f'\n{resultado6.decode()}')
time.sleep(4)
os.system('cls')

questao7 = clientSocket.recv(1024)
print('\nQuestão 7)\n')
print(questao7.decode())
resposta7 = str(input('\nResposta: '))
os.system('cls')
clientSocket.send(resposta7.encode())
resultado7 = clientSocket.recv(1024)
print(f'\n{resultado7.decode()}')
time.sleep(4)
os.system('cls')

questao8 = clientSocket.recv(1024)
print('\nQuestão 8)\n')
print(questao8.decode())
resposta8 = str(input('\nResposta: '))
os.system('cls')
clientSocket.send(resposta8.encode())
resultado8 = clientSocket.recv(1024)
print(f'\n{resultado8.decode()}')
time.sleep(4)
os.system('cls')

questao9 = clientSocket.recv(1024)
print('\nQuestão 9)\n')
print(questao9.decode())
resposta9 = str(input('\nResposta: '))
os.system('cls')
clientSocket.send(resposta9.encode())
resultado9 = clientSocket.recv(1024)
print(f'\n{resultado9.decode()}')
time.sleep(4)
os.system('cls')

questao10 = clientSocket.recv(1024)
print('\nQuestão 10)\n')
print(questao10.decode())
resposta10 = str(input('\nResposta: '))
os.system('cls')
clientSocket.send(resposta10.encode())
resultado10 = clientSocket.recv(1024)
print(f'\n{resultado10.decode()}')
time.sleep(4)
os.system('cls')

resultado = clientSocket.recv(1024)
print(f'\n{resultado.decode()}\n')
time.sleep(8)
clientSocket.close()