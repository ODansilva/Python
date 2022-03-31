import sqlite3

while True:
    opcao = 1
    if opcao == 0:
        print('fechando o programa...')
        break
    elif opcao == 1:
        con = sqlite3.connect('dados_ativ02.db')
        k = con.cursor()
        k.execute('select curso, situacao, count(nome), avg((nota1+nota2+nota3+nota4)/4) from aluno group by curso;')
        resultado = k.fetchall()
        print(resultado)
        for i in range(len(resultado)):
            for linha in resultado:
                curso = linha[0]
                situacao = linha[1]
                t_alunos = linha[2]
                gmedia = linha[3]

                con2 = sqlite3.connect('dados_ativ02.db')
                k2 = con2.cursor()
                k2.execute('select * from aluno;')
                resultado2 = k2.fetchall()
                c_aprovados = 0
                c_reprovados = 0
                c_recuperacao = 0
                situacao = resultado2[i][7]
                print(resultado2)

                if situacao == 'Aprovado':
                    c_aprovados += 1
                elif situacao == 'Reprovado':
                    c_reprovados += 1
                elif situacao == 'Recuperação':
                    c_recuperacao += 1

                print('{}:'.format(curso.upper()))
                print('Total de alunos: {}'.format(t_alunos))
                print('Número de alunos aprovados: {}'.format(c_aprovados))
                print('Número de alunos recuperação: {}'.format(c_recuperacao))
                print('Número de alunos reprovados: {}'.format(c_reprovados))
                print('Média geral do curso: {:.3f}\n'.format(gmedia))
            opcao = input('1 - Para Atualizar a Lista \n0 - Para encerrar o programa\n...')
con.close()
