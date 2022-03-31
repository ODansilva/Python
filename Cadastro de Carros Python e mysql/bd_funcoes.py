import sqlite3

# Nome do arquivo do banco de dados
CARROS = "Carros.db"


def inserir_carros(dic_carro):
    # Conecta no banco informado
    conexao = sqlite3.connect(CARROS)

    # O cursor é usado para enviar SQL que será executado no banco de dados
    c = conexao.cursor()

    try:
        # Comando SQL a ser executado. Retorna o número de linhas inseridas na tabela
        n = c.execute("insert into carros (valor, ano, modelo, marca, combustível, placa, renavam, descrição, "
                      "telefone) values (:valor, :ano, :modelo, :marca, :combustível, :placa, :renavam, :descrição, "
                      ":telefone)", dic_carro)
        print(n)
        # O commit salva os dados efetivamente no banco de dados através da conexão
        conexao.commit()

        # Caso exatamente uma linha tenha sido inserida, retorna True. False caso contrário
        sucesso = n.rowcount == 1
    except sqlite3.Error as erro:
        # Neste caso, ocorreu algum erro
        print(erro)
        sucesso = False

    # Fecha o cursor para liberar recursos alocados
    c.close()

    # Fecha a conexão com o banco de dados
    conexao.close()

    # True caso tenha inserido, False caso contrário
    return sucesso


def buscar_por_matricula(matricula):
    # Conecta no banco informado.
    conexao = sqlite3.connect(BANCO)

    # Pega o cursor
    c = conexao.cursor()

    # Comando SQL que será executado
    c.execute("select * from aluno where matricula = ?", (matricula, ))

    # Pega os resultados em uma lista de tuplas
    resultado = c.fetchone()

    # Fecha o cursor
    c.close()

    # Fecha a conexão com o banco de dados
    conexao.close()

    # Monta um dicionário com o resultado
    if resultado:
        dic_aluno = {
            "id": resultado[0],
            "nome": resultado[1],
            "media": resultado[2],
            "matricula": resultado[3]
        }
    else:
        dic_aluno = {}

    # Retorna o dicionário como resultado
    return dic_aluno
