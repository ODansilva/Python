while True:
    S_cliente = socket(AF_INET, SOCK_STREAM)
    S_cliente.connect(('127.0.0.3', 8085))
    S_cliente.close()
