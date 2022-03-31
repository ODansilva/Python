from socket import*
import struct
import loja
import Pacote
import threading

S_servidor = socket(AF_INET,SOCK_STREAM)
S_servidor.bind(('0.0.0.0', 8084))
S_servidor.listen(5)

def tratar_cliente(S_con,endereco_con):
    RID = S_con.recv(struct.calcsize(Pacote.P_REQUEST))
    I = struct.unpack(Pacote.P_REQUEST, RID)
    ID = I[0]
    QP = I[1]

    print("{} conectou como o ID{}!".format(endereco_con, ID))
    if ID == 1:
        for i in range(QP):
            dados = S_con.recv(struct.calcsize(Pacote.P_PRO))
            elementos = struct.unpack(Pacote.P_PRO, dados)

            produto = elementos[0].decode(Pacote.ENCODING).split('\x00',1)[0] #remove os \x00 de preenchimento de espaços quando há sobras de caracteres,no tamanho do pacote.
            prel1 = round(elementos[1],2)
            prel2 = round(elementos[2],2)
            print('Executando Processo de Cadastro...')
            loja.cadastrata_produto(produto, prel1, prel2)
            estado = 'Produto Cadastrado'

            Resposta = struct.pack(Pacote.P_RESPOSTA, estado.encode(Pacote.ENCODING))
            S_con.sendall(Resposta)
        S_con.close()
    if ID == 2:
        print('Reunindo Informações da Lista de Produtos...')
        lista = loja.lista_produto() #a loja retorna uma matriz com todos os produtos. 
        tl = len(lista)
        for i in range(tl):
            produto = lista[i][0]
            prel1 = float(lista[i][1])
            prel2 = float(lista[i][2])
            Resposta = struct.pack(Pacote.P_LISTA,produto.encode(Pacote.ENCODING),prel1,prel2)
            print(Resposta)
            S_con.sendall(Resposta)
        S_con.close()

while True:
    print("Esperando conexão...")
    S_conexao, endereco_cliente = S_servidor.accept()
    print("Conexão recebida de", endereco_cliente)
    threading.Thread(target=tratar_cliente, args=(S_conexao, endereco_cliente)).start()
