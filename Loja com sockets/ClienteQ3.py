from socket import*
import struct
import Pacote

S_cliente = socket(AF_INET, SOCK_STREAM)
S_cliente.connect(('127.0.0.3',8084))

ID = 2
QP = 0
RID = struct.pack(Pacote.P_REQUEST,ID,QP)
S_cliente.sendall(RID)
while True: #<< não e necessario
    Resposta = S_cliente.recv(struct.calcsize(Pacote.P_LISTA))
    elementos = struct.unpack(Pacote.P_LISTA, Resposta)

    produto = elementos[0].decode(Pacote.ENCODING).split('\x00',1)[0]
    prel1 = (elementos[1])
    prel2 = (elementos[2])
    pres = [prel1,prel2]
    maior = max(pres)
    menor = min(pres)
    media = (maior + menor)/2

    print('Nome do Produto: {}'.format(produto))
    print('Preços nas Duas Lojas:---< Loja 1 R${} >-----< loja 2 R${} >---'.format(prel1,prel2))
    print('Preço Mais Barato do Produto R$:{}'.format(menor))
    print('Preço Mais Caro do Produto R$:{}'.format(maior))
    print('Preço Médio do Produto: {}'.format(media))


