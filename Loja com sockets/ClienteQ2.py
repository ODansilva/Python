from socket import*
import struct
import Pacote

S_cliente = socket(AF_INET, SOCK_STREAM)
S_cliente.connect(('127.0.0.3', 8084))

qprodutos = int(input('Digite a Quantidade de produtos a serem cadastrados: '))

QP = qprodutos
ID = 1
RID = struct.pack(Pacote.P_REQUEST, ID,QP)
S_cliente.sendall(RID)

for i in range(qprodutos):
    produto = str(input('Digite o nome {} produto:'.format(i+1)))
    prel1 = float(input('Digite o Preço na Primeira Loja R$: '))
    prel2 = float(input('Digite o Preço na Segunda Loja: R$'))
    dados = struct.pack(Pacote.P_PRO,produto.encode(Pacote.ENCODING),prel1,prel2)
    S_cliente.sendall(dados)

    Resposta = S_cliente.recv(struct.calcsize(Pacote.P_RESPOSTA))
    elementos = struct.unpack(Pacote.P_RESPOSTA, Resposta)

    print(elementos[0].decode(Pacote.ENCODING))
S_cliente.close()
