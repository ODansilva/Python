
def cadastrata_produto(produto, prel1, prel2):
    arquivo = open('Produtos.txt', 'a', encoding='utf-8')
    arquivo.write('{};{};{}\n'.format(produto, prel1, prel2))
    arquivo.close()

def lista_produto():
    produtos = []
    arquivo = open('Produtos.txt', 'r', encoding='utf-8')
    for linha in arquivo.readlines():
        campos = linha[:-1].split(";")
        print(campos)
        produtos.append(campos)
    return(produtos)