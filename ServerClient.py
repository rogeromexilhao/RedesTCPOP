import socket
from tkinter import *
import customtkinter as ctk
import threading

app = ctk.CTk()
app.title('Main')
largura = 600
altura = 600
app.geometry("%dx%d" % (largura, altura))
largura_tela = app.winfo_screenwidth()
altura_tela = app.winfo_screenheight()
pos_x = (largura_tela // 2) - (largura // 2)
pos_y = (altura_tela // 2) - (altura // 2)
app.geometry("+%d+%d" % (pos_x, pos_y))

def executa():
    try:
        server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server.bind(('172.31.14.220', 5000))
        server.listen()
            
        aguardando = ctk.CTkLabel(app,text='Esperando Conexões...')
        aguardando.pack()
        
        client, doclient = server.accept()
        
        aguardando.destroy()
        
        ctk.CTkLabel(app,text=f"O cliente {doclient} se conectou").pack()
        
        chat = ctk.CTkScrollableFrame(app,width=300, height=500)
        chat.pack()
    except:
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client.connect(('172.31.14.220', 5000))
        
        ctk.CTkLabel(app,text="Usuário conectado").pack()
        
        chat = ctk.CTkScrollableFrame(app,width=300, height=500)
        chat.pack()

    def sending(t):        
        messagectk = ctk.CTkEntry(app,placeholder_text='Digite sua mensagem',width=200)
        messagectk.pack()
        
        while True:
            def key_press(event):
                if event.keycode == 13:
                    ctk.CTkLabel(chat,text=f"Você: {messagectk.get()}",fg_color='green',corner_radius=3,padx=(5),pady=(3)).pack()
                    message = messagectk.get()
                    messagectk.delete(0, END)
                    t.send(message.encode())
            app.bind('<Key>',key_press)

    def receiving(t):
        while True:
            ctk.CTkLabel(chat,text=f"USER: {t.recv(1024).decode()}",corner_radius=3,padx=(5),pady=(3)).pack()
                

    threading.Thread(target=sending, args=(client,)).start()
    threading.Thread(target=receiving, args=(client,)).start()


def start_server():
    executa()

thread = threading.Thread(target=start_server)
thread.daemon = True
thread.start()

app.mainloop()