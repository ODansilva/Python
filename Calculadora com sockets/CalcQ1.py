def calc(n1,n2,operacao):
    if operacao == 1:
        op = n1 + n2
    if operacao == 2:
        op = n1 - n2
    if operacao == 3:
        op = n1 / n2
    if operacao == 4:
        op = n1 * n2
    return(op)
