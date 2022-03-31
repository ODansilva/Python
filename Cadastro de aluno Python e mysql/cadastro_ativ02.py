import sqlite3
def sit(media):
    if media >= 7:
        situacao = 'Aprovado'
    elif media < 3:
        situacao = 'Reprovado'
    else:
        situacao = 'Recuperação'
    return situacao

while True:
    con = sqlite3.connect('dados_ativ02.db')
    k = con.cursor()
    numero = int(input('Digite o numero do aluno: '))
    nome = str(input('Digite o nome do aluno: '))
    curso = str(input('Digite o curso do aluno: '))
    nota1 = float(input('Digite a Primeira nota do aluno: '))
    nota2 = float(input('Digite a Segunda nota do aluno: '))
    nota3 = float(input('Digite a Terceira nota do aluno:'))
    nota4 = float(input('Digite a Quarta nota do aluno: '))
    media = (nota1+nota2+nota3+nota4)/4
    situacao = sit(media)

    k.execute('insert into aluno (numero, nome, curso, nota1, nota2, nota3, nota4, situacao) values (?, ?, ?, ?, ?, ?, ?, ?)', (numero, nome, curso, nota1, nota2, nota3, nota4, situacao))
    if k.rowcount > 0:
        print('Aluno foi cadastrado com sucesso!')
    else:
        print('Falha ao cadastrado o aluno!')
    con.commit()
    opcao = int(input('1 - Para Inserir outro aluno \n0 - Para encerrar o programa\n...'))
    if opcao == 0:
        print('fechando o programa...')
        break
con.close()