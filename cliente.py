import socket

# Configurações do servidor
host = '127.0.0.1'  # Endereço IP do servidor
port = 12345       # Porta em que o servidor está escutando

# Cria um objeto socket TCP
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Estabelece a conexão com o servidor
sock.connect((host, port))

# Envia dados para o servidor
mensagem = 'Olá, servidor!'
sock.sendall(mensagem.encode())

# Recebe a resposta do servidor
dados = sock.recv(1024).decode()
print('Resposta do servidor:', dados)

# Fecha a conexão
sock.close()