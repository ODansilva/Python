from socket import*
import struct
import CalcQ1
import Pacote

S_servidor = socket(AF_INET,SOCK_STREAM)
S_servidor.bind(('0.0.0.0', 8084))
S_servidor.listen(5)

while True:
    print("Esperando conexão...")
    S_conexao , endereco_cliente = S_servidor.accept()
    print("Conexão recebida de", endereco_cliente)

    dados = S_conexao.recv(struct.calcsize(Pacote.P_CAL))
    elementos = struct.unpack(Pacote.P_CAL, dados)

    n1 = elementos[0]
    n2 = elementos[1]
    operacao = elementos[2]
    Resultado = CalcQ1.calc(n1,n2,operacao)
    print(Resultado)

    Resposta = struct.pack(Pacote.P_RESULTADO,Resultado)
    S_conexao.sendall(Resposta)
