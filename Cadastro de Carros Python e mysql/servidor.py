import flask
import bd_funcoes


app = flask.Flask("Nuvem de Alunos")


# A URL raiz mostrará algumas instruções de uso
@app.route("/")
def ajuda():
    resposta = {
        "operacao1": "cadastrar aluno -> /adicionar + json",
        "operacao2": "buscar aluno -> /consultar/<int:matricula>"
    }

    return flask.jsonify(resposta)


# Note que neste exemplo, a parâmetro é passado em um JSON
@app.route("/adicionar")
def inserir_carros():

    dados_recebidos = flask.request.get_json()
    print(dados_recebidos)
    resposta = bd_funcoes.inserir_carros(dados_recebidos)

    return flask.jsonify({"sucesso": resposta})


# Note que neste exemplo, a parâmetro é passado na URL
@app.route("/consultar/<int:matricula>")
def buscar_aluno(matricula):
    resposta = bd_funcoes.buscar_por_matricula(matricula)

    return flask.jsonify(resposta)


app.run("0.0.0.0", 8080)
