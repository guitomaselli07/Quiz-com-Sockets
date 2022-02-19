from socket import *
import threading
import time
import os

serverHOST = '192.168.100.92'
serverPort = 6000

q1 = "Qual desses objetos não pode ser reciclado? \n\n A) Folha de Caderno \n B) Esponja de Cozinha \n C) Garrafa de Refrigerante"

q2 = 'Qual desses materiais demora mais tempo para se decompor? \n\n A) Papel \n B) Metal \n C) Vidro'

q3 = 'Qual é o país que mais recicla no mundo?\n\n A) Brasil \n B) Itália\n C) Canadá'

q4 = 'Qual é a porcentagem de lixo reciclado no Brasil? \n\n A) 3% \n B) 10% \n C) 25%'

q5 = 'Qual material o Brasil mais recicla?\n\n A) Borracha\n B) Alumínio\n C) Papel'

q6 = 'Qual é a capital brasileira que mais recicla?\n\n A) Florianópolis\n B) Manaus\n C) São Paulo'

q7 = 'O que cesto de lixo com a cor roxa significa?\n\n A) Lixo Hospitalar\n B) Lixo Orgânico\n C) Lixo Radioativo'

q8 = 'Quantas vezes uma latinha de refrigerante pode ser reciclada?\n\n A) Infinitas Vezes\n B) 10 vezes\n C) Uma vez'

q9 = 'Qual é o dia internacional da reciclagem?\n\n A) 20 de abril\n B) 17 de maio\n C) 7 de junho'

q10 = 'Em que ano foi criado a símbulo mundial da reciclagem?\n\n A) 2004\n B) 2000\n C) 1970'

serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind((serverHOST, serverPort))
serverSocket.listen()

def conexao():

	while True:
		os.system('cls')
		print('\nO servidor está esperando por conexões...')
		connectionSocket, addr = serverSocket.accept()
		os.system('cls')
		print(f'\nConexão aceita para {addr}.')
		connectionSocket.send('Bem Vindo ao Quiz'.encode())
		user_name = connectionSocket.recv(1024)
		os.system('cls')
		print(f'\n{user_name.decode()} entrou no jogo.')
		jogo(connectionSocket, user_name)

def jogo(connectionSocket, user_name):

	count = 0

	connectionSocket.send(q1.encode())
	resposta = connectionSocket.recv(1024)
	if(resposta.decode() == 'b' or resposta.decode() == 'B'):
		count = count + 1
		connectionSocket.send("Parabéns, você acertou essa questão!".encode())
	else:
		connectionSocket.send("Você errou essa questão. A alternativa certa era: B) Esponja de Cozinha.".encode())

	connectionSocket.send(q2.encode())
	resposta = connectionSocket.recv(1024)
	if(resposta.decode() == 'c' or resposta.decode() == 'C'):
		count = count + 1
		connectionSocket.send("Parabéns, você acertou essa questão!".encode())
	else:
		connectionSocket.send("Você errou essa questão. A alternativa certa era: C) Vidro.".encode())
	
	connectionSocket.send(q3.encode())
	resposta = connectionSocket.recv(1024)
	if(resposta.decode() == 'a' or resposta.decode() == 'A'):
		count = count + 1
		connectionSocket.send("Parabéns, você acertou essa questão!".encode())
	else:
		connectionSocket.send("Você errou essa questão. A alternativa certa era: A) Brasil.".encode())
	
	connectionSocket.send(q4.encode())
	resposta = connectionSocket.recv(1024)
	if(resposta.decode() == 'a' or resposta.decode() == 'A'):
		count = count + 1
		connectionSocket.send("Parabéns, você acertou essa questão!".encode())
	else:
		connectionSocket.send("Você errou essa questão. A alternativa certa era: A) 3%.".encode())

	connectionSocket.send(q5.encode())
	resposta = connectionSocket.recv(1024)
	if(resposta.decode() == 'b' or resposta.decode() == 'B'):
		count = count + 1
		connectionSocket.send("Parabéns, você acertou essa questão!".encode())
	else:
		connectionSocket.send("Você errou essa questão. A alternativa certa era: B) Alumínio.".encode())
	
	connectionSocket.send(q6.encode())
	resposta = connectionSocket.recv(1024)
	if(resposta.decode() == 'a' or resposta.decode() == 'A'):
		count = count + 1
		connectionSocket.send("Parabéns, você acertou essa questão!".encode())
	else:
		connectionSocket.send("Você errou essa questão. A alternativa certa era: A) Florianópolis.".encode())

	connectionSocket.send(q7.encode())
	resposta = connectionSocket.recv(1024)
	if(resposta.decode() == 'c' or resposta.decode() == 'C'):
		count = count + 1
		connectionSocket.send("Parabéns, você acertou essa questão!".encode())
	else:
		connectionSocket.send("Você errou essa questão. A alternativa certa era: C) Lixo Radioativo.".encode())
	
	connectionSocket.send(q8.encode())
	resposta = connectionSocket.recv(1024)
	if(resposta.decode() == 'a' or resposta.decode() == 'A'):
		count = count + 1
		connectionSocket.send("Parabéns, você acertou essa questão!".encode())
	else:
		connectionSocket.send("Você errou essa questão. A alternativa certa era: A) Infinitas Vezes.".encode())

	connectionSocket.send(q9.encode())
	resposta = connectionSocket.recv(1024)
	if(resposta.decode() == 'b' or resposta.decode() == 'B'):
		count = count + 1
		connectionSocket.send("Parabéns, você acertou essa questão!".encode())
	else:
		connectionSocket.send("Você errou essa questão. A alternativa certa era: B) 17 de maio.".encode())

	connectionSocket.send(q10.encode())
	resposta = connectionSocket.recv(1024)
	if(resposta.decode() == 'c' or resposta.decode() == 'C'):
		count = count + 1
		connectionSocket.send("Parabéns, você acertou essa questão!".encode())
	else:
		connectionSocket.send("Você errou essa questão. A alternativa certa era: C) 1970.".encode())

	os.system('cls')
	print(f'\n{user_name.decode()} terminou e saiu do jogo.')

	if(count >= 7):
		connectionSocket.send(f'Fim do Jodo.\n\nMuito bem {user_name.decode()}, você acertou {str(count)} questões!'.encode())
	if(count < 7):
		connectionSocket.send(f'Fim do Jogo.\n\nQue pena {user_name.decode()}, você acertou apenas {str(count)} questões, mais sorte na próxima!'.encode())

	time.sleep(6)

if __name__ == '__main__':
	user_thread = threading.Thread(target=conexao,args=())
	user_thread.start()
	conexao()