import sqlite3

while True:
    opcao = 1
    if opcao == 1:
        con = sqlite3.connect('dados_ativ02.db')
        k = con.cursor()
        k.execute('select * from aluno;')
        resultado = k.fetchall()
        alunos = len(resultado)
        cmedia = 0
        c_aprovados = 0
        c_reprovados = 0
        c_recuperacao = 0
        for linha in resultado:
            numero = linha[0]
            nome = linha[1]
            curso = linha[2]
            nota1 = linha[3]
            nota2 = linha[4]
            nota3 = linha[5]
            nota4 = linha[6]
            situacao = linha[7]
            media = (nota1+nota2+nota3+nota4)/4
            cmedia += media

            if situacao == 'Aprovado':
                c_aprovados += 1
            elif situacao == 'Reprovado':
                c_reprovados += 1
            elif situacao == 'Recuperação':
                c_recuperacao += 1

            print('Aluno {} : {}'.format(numero, nome))
            print('Curso: {}'.format(curso))
            print('Notas: {} {} {} {}'.format(nota1, nota2, nota3, nota4))
            print('Situação: {} com média {:.2f}\n'.format(situacao, media))

        gmedia = cmedia / alunos
        print('Número total de alunos: {}'.format(alunos))
        print('Número de alunos aprovados: {}'.format(c_aprovados))
        print('Número de alunos em recuperação: {}'.format(c_recuperacao))
        print('Número de alunos reprovados: {}'.format(c_reprovados))
        print('Média geral da turma: {:.4f}\n'.format(gmedia))
        opcao = int(input('1 - Para Lista os aluno novamente \n0 - Para encerrar o programa\n...'))
        if opcao == 0:
            print('Fechando o programa...')
            break
con.close()
