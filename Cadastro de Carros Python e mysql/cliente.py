import requests

while True:
    print("---------------------------")
    print("0 - Sair")
    print("1 - Cadastra Carros")
    print("2 - Buscar Carros")
    op = int(input(">> "))

    if op == 0:
        print("Saindo do programa...")
        break
    elif op == 1:
        dados = {
            "valor": input("Digite o valor do veículo: "),
            "ano": input("Digite o ano do veículo: "),
            "modelo": input("Digite o modelo do carro: "),
            "marca": input("Digite a marca do carro: "),
            "combustivel": input("Digite o tipo de combustível utilizado: "),
            "placa": input("Digite a placa do veículo: "),
            "renavam": input("Digite o número do RENAVAM: "),
            "descricao": input("Digite a descrição do veículo: "),
            "telefone": input("Digite o telefone do responsável: ")
        }
        print(dados)

        resposta = requests.get("http://127.0.0.1:8080/adicionar", json=dados).json()

        if resposta["sucesso"]:
            print("Veículo cadastrado com sucesso!")
        else:
            print("Algum erro ocorreu durante o cadastro!")
    elif op == 2:
        matricula, = int(input("Digite a matrícula: "))

        resposta = requests.get("http://127.0.0.1:8080/consultar/{}".format(matricula)).json()

        if resposta:
            print("ID:", resposta["id"])
            print("Nome:", resposta["nome"])
            print("Matrícula:", resposta["matricula"])
            print("Média:", resposta["media"])
        else:
            print("A matrícula não foi encontrada!")
    else:
        print("Opção inválida, tente novamente!")
