from socket import*
import struct
import Pacote

S_cliente = socket(AF_INET, SOCK_STREAM)
S_cliente.connect(('127.0.0.3',8084))

n1 = int(input('Digite o primeiro números real'))
n2 = int(input('Digite o segundo números real'))
print('Digite o Tipo de Operação\n1: Para >> Soma\n2: Para >> Subtração\n3: Para >> Divisão\n4: Para >> Multiplicação')
operacao = int(input('Digite o Tipo de Operação:'))

dados = struct.pack(Pacote.P_CAL, n1, n2,operacao)
S_cliente.sendall(dados)

Resposta = S_cliente.recv(struct.calcsize(Pacote.P_RESULTADO))
elementos = struct.unpack(Pacote.P_RESULTADO, Resposta)

print('O Resultado e {:.2f} '.format(elementos[0]))

S_cliente.close()
