#!/usr/bin/python3
import socket
import customtkinter as ctk
import time
import threading

app = ctk.CTk()
app.title('Main')
largura = 400
altura = 300
app.geometry("%dx%d" % (largura, altura))
largura_tela = app.winfo_screenwidth()
altura_tela = app.winfo_screenheight()
pos_x = (largura_tela // 2) - (largura // 2)
pos_y = (altura_tela // 2) - (altura // 2)
app.geometry("+%d+%d" % (pos_x, pos_y))

ctk.CTkLabel(app,text='Esperando Conexões').pack()

def executa():
    MEU_IP=''
    MINHA_PORTA = 8000
    tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    MEU_SERVIDOR = (MEU_IP, MINHA_PORTA)
    tcp.bind(MEU_SERVIDOR)
    tcp.listen(1)

    conexao, docliente = tcp.accept()
    print("O cliente =", docliente, "se conectou")
    ctk.CTkLabel(app,text=f"O cliente = {docliente} se conectou").pack()


    while True:
        mensagem_recebida = conexao.recv(1024)
        if not mensagem_recebida:
            break
        print("Recebi =", mensagem_recebida, ", Do cliente", docliente)
        print(mensagem_recebida)
        ctk.CTkLabel(app,text=f"Recebi = {mensagem_recebida.decode()}, Do cliente {docliente}").pack()


    conexao.close()

def start_server():
    time.sleep(3)
    executa()
    app.mainloop()

thread = threading.Thread(target=start_server)
thread.daemon = True
thread.start()

app.mainloop()