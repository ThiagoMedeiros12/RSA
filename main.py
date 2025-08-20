import tkinter as tk
from logica import criptografar_descriptografar , decript_msg

def on_click_cript():
    msg = entrada_msg_cript.get()
    list,msg_cript = criptografar_descriptografar(msg)
    return endscreen_call_cript(msg_cript,list)

def on_click_decript():
    msg = entrada_msg_decript.get()
    d = int(keyD.get())
    n = int(keyN.get())
    msgDecripted = decript_msg(d=d,n=n,criptedInput_msg=msg)
    return endscreen_call_decript(msgDecripted)


    

def endscreen_call_decript(msg_decripted):
    endscreen = tk.Toplevel()
    endscreen.title("Descriptografia")
    endscreen_msg = tk.Label(endscreen,text =f"Mensagem Descriptografada:")
    endscreen_msgbox = tk.Text(endscreen,height=2)
    endscreen_msgbox.insert("1.0",msg_decripted)
    endscreen_msgbox.configure(state="disabled")
    endscreen_msg.pack()
    endscreen_msgbox.pack(padx=10,pady=5,fill="both")
    
    
    

def endscreen_call_cript(msg_cript,list):
    endscreen = tk.Toplevel()
    endscreen.title("Criptografia")
    
    
    #[p,q,n,fi_n,e,d] gera valores para encriptar
    endscreen_keys = f"D:{list[5]}\nN:{list[2]}\n"



    endscreen_msg = tk.Label(endscreen,text ="Mensagem Criptografada:")
    endscreen_txt = tk.Label(endscreen,text="Chaves:")
    endscreen_msgbox = tk.Text(endscreen,height=2)
    endscreen_msgbox.insert("1.0",msg_cript)
    endscreen_msgbox.configure(state="disabled")
    endscreen_msg.pack()
    endscreen_msgbox.pack(padx=10,pady=5,fill="both")
    endscreen_keys_box = tk.Text(endscreen,height=2)
    endscreen_keys_box.insert("1.0",endscreen_keys)
    endscreen_keys_box.configure(state="disabled")
    endscreen_txt.pack()
    endscreen_keys_box.pack(padx=10,pady=5,fill="both")


    


app = tk.Tk()

greeting = tk.Label(app,text='Bem vindo ao meu app de criptografia RSA')
ask_msg = tk.Label(app,text='Mensagem:')
entrada_msg_cript = tk.Entry(app)
button_cript = tk.Button(app,text="Criptografar", command=on_click_cript )
ask_cript_key_D = tk.Label(app,text='Chave D:')
keyD = tk.Entry(app)
ask_cript_key_N = tk.Label(app,text='Chave N:')
keyN = tk.Entry(app)
ask_cript_msg = tk.Label(app,text='Mensagem:')
entrada_msg_decript = tk.Entry(app)
button_decript = tk.Button(app,text="Descriptografar", command=on_click_decript)



#mainscreen
greeting.pack(pady=10)
ask_msg.pack()
entrada_msg_cript.pack()

button_cript.pack(pady=10)
ask_cript_msg.pack()
entrada_msg_decript.pack()
ask_cript_key_D.pack()
keyD.pack()
ask_cript_key_N.pack()
keyN.pack()

button_decript.pack(pady=10)


app.title("CriptV0.1")








app.mainloop()