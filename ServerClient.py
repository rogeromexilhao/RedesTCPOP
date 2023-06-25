import socket
import customtkinter as ctk
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

def executa():
    try:
    #choice = input("Host = (1) ou Client = (2)")
        #if choice == '1':
        server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server.bind(('192.168.15.32', 5000))
        server.listen()
            
        client, doclient = server.accept()
        ctk.CTkLabel(app,text='Esperando Conexões 1').pack()
        ctk.CTkLabel(app,text=f"O cliente = {doclient} se conectou").pack()
    except:
        ctk.CTkLabel(app,text='Esperando Conexões 2').pack()
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client.connect(('192.168.15.32', 5000))

    def sending_mensages(c):
        while True:
                message = input("")
                c.send(message.encode())
                print("You: " + message)

    def receiving_mensages(c):
        while True:
                print("Partner: " + c.recv(1024).decode())
                

    threading.Thread(target=sending_mensages, args=(client,)).start()
    threading.Thread(target=receiving_mensages, args=(client,)).start()


def start_server():
    executa()
    app.mainloop()

thread = threading.Thread(target=start_server)
thread.daemon = True
thread.start()

app.mainloop()