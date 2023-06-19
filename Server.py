import socket

# Configurações do servidor
host = '127.0.0.1'  # Endereço IP do servidor
port = 12345       # Porta em que o servidor irá escutar

# Cria um objeto socket TCP
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Liga o socket ao endereço IP e porta
sock.bind((host, port))

# Define o limite de conexões pendentes
sock.listen(1)

print('Servidor aguardando conexões...')

# Aguarda a conexão do cliente
cliente_sock, cliente_endereco = sock.accept()
print('Cliente conectado:', cliente_endereco)

# Recebe dados do cliente
dados = cliente_sock.recv(1024).decode()
print('Mensagem recebida:', dados)

# Envia resposta para o cliente
resposta = 'Olá, cliente!'
cliente_sock.sendall(resposta.encode())

# Fecha a conexão com o cliente
cliente_sock.close()

# Fecha o socket do servidor
sock.close()