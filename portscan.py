import socket

# Cria um objeto de soquete usando o protocolo IPv4 e o tipo de soquete TCP
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Conecta o cliente ao servidor no endereço "bamcocn.com" na porta 80
client.connect(("bamcocn.com", 80))

# Envia a string "OLa" codificada em bytes para o servidor
client.send(b"OLa")

# Recebe até 1024 bytes de dados do servidor e armazena na variável "resposta"
resposta = client.recv(1024)

# Imprime a resposta recebida do servidor
print(resposta)

