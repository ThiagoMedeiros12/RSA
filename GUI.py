import tkinter as tk

def on_click():
    return endscreen_call()

def endscreen_call():
    endscreen = tk.Toplevel()
    endscreen.title("endscreen")
    endscreen_msg = tk.Label(endscreen,text ="Mensagem:")
    endscreen_keys = tk.Label(endscreen,text="Chave:")

    endscreen_msg.pack()
    endscreen_keys.pack()


app = tk.Tk()

greeting = tk.Label(app,text='Bem vindo ao meu app de criptografia RSA')
ask_msg = tk.Label(app,text='Mensagem:')
entrada_msg_cript = tk.Entry(app)
button_cript = tk.Button(app,text="Criptografar", command=on_click )
ask_cript_key = tk.Label(app,text='Chave:')
key = tk.Entry(app)
ask_cript_msg = tk.Label(app,text='Mensagem:')
entrada_msg_decript = tk.Entry(app)
button_decript = tk.Button(app,text="Descriptografar", command=on_click)



#mainscreen
greeting.pack(pady=10)
ask_msg.pack()
entrada_msg_cript.pack()
button_cript.pack(pady=10)
ask_cript_key.pack()
key.pack()
ask_cript_msg.pack()
entrada_msg_decript.pack()
button_decript.pack(pady=10)


app.title("CriptV0.1")








app.mainloop()