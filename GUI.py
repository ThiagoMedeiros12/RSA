import tkinter as tk
from logica import decript_msg as dm , criptografar_descriptografar as cm



def endscreen_call():
    endscreen = tk.Toplevel()
    endscreen.title("endscreen")
    endscreen_msg = tk.Label(endscreen,text =f"Mensagem:"{msg})
    endscreen_keys = tk.Label(endscreen,text =f"Chave:"{list_keys}")

    endscreen_msg.pack()
    endscreen_keys.pack()

def on_click():
    if button_cript['state'] == 'clicked':
        input_msg = entrada_msg_cript.get()
        list_keys, msg = cm(input=input_msg)
    return endscreen_call()



app = tk.Tk()

greeting = tk.Label(app,text='Bem vindo ao meu app de criptografia RSA')
ask_msg = tk.Label(app,text='Mensagem:')
entrada_msg_cript = tk.Entry(app)
button_cript = tk.Button(app,text="Criptografar",name='Cript', command=on_click)
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