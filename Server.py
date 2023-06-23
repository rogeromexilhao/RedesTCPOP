#!/usr/bin/python3
import socket
import customtkinter as ctk
import time 

app = ctk.CTk()
app.title('Main')
# Endereco IP do Servidor, '' = significa que ouvira em todas as interfaces

largura = 400
altura = 300
app.geometry("%dx%d" % (largura, altura))

app.update_idletasks()
largura_tela = app.winfo_screenwidth()
altura_tela = app.winfo_screenheight()
pos_x = (largura_tela // 2) - (largura // 2)
pos_y = (altura_tela // 2) - (altura // 2)
app.geometry("+%d+%d" % (pos_x, pos_y))

def executa():
    MEU_IP=''
    MINHA_PORTA = 8000  
    # Porta que o Servidor vai ouvir 

    tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # socket.AF_INET = INET (exemplo IPv4)sockets, #socket.SOCK_STREAM=usaremos TCP

    #x = 1
    testa_mensagem = ''
    MEU_SERVIDOR = (MEU_IP, MINHA_PORTA) 
    tcp.bind(MEU_SERVIDOR)
    # faz o bind do ip e a porta para que possa comecar a ouvir

    tcp.listen(1) 
    #comeca a ouvir

    conexao, docliente =tcp.accept()
    print ("o cliente = ", docliente, " se conectou")
    #pega o ip do cliente que conectou
    while 1:
        Mensagem_Recebida = conexao.recv(1024)
        #Mensagem recebida do cliente 
        if testa_mensagem != Mensagem_Recebida:  
    #aqui verifica se exite mensagem nova  
            print ("Recebi = ",Mensagem_Recebida," , Do cliente", docliente)
        conexao.close()


time.sleep(3)
executa()
app.mainloop()

#fim do socket