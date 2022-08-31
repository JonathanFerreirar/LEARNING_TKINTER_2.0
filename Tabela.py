import tkinter as tk
from tkinter import NSEW, ttk
from tkinter.tix import Tree
from clase import adicionar_cliente, ver_dados, deletar, editar
from tkinter import messagebox
import csv

tela  = tk.Tk()
tela.title("Lista_clientes_IR")   #Titulo da tela
tela.geometry("700x600") #Declarando o tamanho da tela.
tela.resizable(width=False, height=False)  #Usado para bloquear o alterações no tamanho da janela.

azul = ('#0f0f1c')
branco = ('#06063d')

frame_de_cima = tk.Frame(tela,bg=azul,width=700,height=50)  #_Crio uma parte de cima dar cor selecionada um frame
frame_de_cima.grid(column=0, row=0)  #Indica onde devo o frame na minha janela.

#titulo da janela 
titulo = tk.Label(tela,width=30, text="LISTA_CLIENTES_IR",background=azul, foreground="white", font=('Calibri',15, "bold"))  #Crio meu titulo na janela
titulo.grid(column=0, row=0) 

#Frame de divisão entre os 2 primeiros frames
frame_da_divisao = tk.Frame(tela,bg="white",width=700,height=3)  #_Crio uma parte do meio dar cor selecionada um frame
frame_da_divisao.grid(column=0, row=1, padx=0, pady=0, sticky=NSEW)

#Frame do meio 
frame_do_meio = tk.Frame(tela,bg=branco,width=700,height=260)  #_Crio uma parte do meio dar cor selecionada um frame
frame_do_meio.grid(column=0, row=2, padx=0, pady=0, sticky=NSEW)  #Indica onde devo o frame na minha janela.

frame_da_tela = tk.Frame(tela,bg="grey",width=700,height=290)  #_Crio uma parte do meio dar cor selecionada um frame
frame_da_tela.grid(column=0, row=3, padx=0, pady=15, sticky=NSEW )  #Indica onde devo o frame na minha janela.

global grafico 

def visao():
    global grafico
    
    
    
    
    lista_iR = ver_dados()
    
    grafico = ttk.Treeview(frame_da_tela,columns=('nome', 'cpf', "senha", "telefone", "pago"), show="headings")
    
    #vertical scrollbar
    vsb = ttk.Scrollbar(
        frame_da_tela, orient="vertical", command=grafico.yview)
    
    vsb.grid(column=1, row=3, sticky='ns')
    
    
    #Hoeizontal scrollbar
    hsb = ttk.Scrollbar(
        frame_da_tela, orient="horizontal", command=grafico.xview)
    
    hsb.grid(column=0, row=4, sticky='ew')

    grafico.configure(yscrollcommand=vsb.set, xscrollcommand=hsb.set)
    
   
    #grafico.pack()
    #vsb.pack(side=RIGHT, fill="y")
    #hsb.pack()

    grafico.column('nome', minwidth=0, width=240)
    grafico.column('cpf', minwidth=0, width=130)
    grafico.column('senha', minwidth=0, width=120)
    grafico.column('telefone', minwidth=0, width=130)
    grafico.column('pago', minwidth=0, width=62)

    grafico.heading('nome', text='NOME')
    grafico.heading('cpf', text='CPF')
    grafico.heading('senha', text='SENHA')
    grafico.heading('telefone', text='FONE')
    grafico.heading('pago', text='PAGO')

    #grafico.grid(column=0, row=5)  ou abaixo

    for row in lista_iR:  
        grafico.insert("", "end", values=row)

    grafico.grid(column=0, row=3)
    #messagebox.showinfo("Atualizado com sucesso!")
visao()


#letra do nome
nome_letra = tk.Label(frame_do_meio, width=10, text="NOME: ",bg=branco ,fg="white", font=("", 10,"bold" ))
nome_letra.place(x=19, y=19)

#Area do nome
nome = tk.Entry(frame_do_meio, width=50,justify="left")
nome.place(x=90, y=20)


#letra do cpf
cpf_letra = tk.Label(frame_do_meio, width=10, text="CPF: ", bg=branco, fg="white", font=("", 10,"bold" ))
cpf_letra.place(x=15, y=70)

#area do cpf
cpf = tk.Entry(frame_do_meio, width=45,justify="left")
cpf.place(x=90,y=70)

#Letra do telefone
telefone_letra = tk.Label(frame_do_meio, width=10, text="FONE: ", bg=branco, fg="white", font=("", 10, "bold"))
telefone_letra.place(x=15, y=120)



#Area do telefone
telefone = tk.Entry(frame_do_meio, width=40,justify="left")
telefone.place(x=90,y=120)


#Letra da senha
senha_letra = tk.Label(frame_do_meio, width=10, text="SENHA: ", bg= branco, fg="white", font=("", 10, "bold"))
senha_letra.place(x=15, y=170)

#Area da senha
senha = tk.Entry(frame_do_meio,justify="left", width=35)
senha.place(x=90,y=170)


#Letra do pago
pago_letra = tk.Label(frame_do_meio, width=10, text="PAGO: ", bg=branco, fg="white", font=("", 10, "bold"))
pago_letra.place(x=15, y=210)

#Area do pago
pago = tk.Entry(frame_do_meio, width=20,justify="left")
pago.place(x=90, y=210)


def editarr ():
    
    #messagebox.showinfo("Jhow Avisa", "Para editar telefone e CPF se atente aos pontos espeços e ifen pois aqui não são automaticos! ")
    
    tela2  = tk.Tk()
    tela2.title("Lista_clientes_IR")   #Titulo da tela
    tela2.geometry("700x200") #Declarando o tamanho da tela.
    tela2.resizable(width=False, height=False) 
    #letra do nome
    Substituir_letra = tk.Label(tela2, width=10, text="Substituir: ", fg="black", font=("", 10,"bold" ))
    Substituir_letra.place(x=22, y=29)

    #Area do nome
    Substituir = tk.Entry(tela2, width=90,justify="left")
    Substituir.place(x=150, y=29)


    #letra do cpf
    Substituir_por_letra = tk.Label(tela2, width=14, text="Subistituir_por: ",  fg="black", font=("", 10,"bold" ))
    Substituir_por_letra.place(x=22, y=90)

    #area do cpf
    Substituir_por = tk.Entry(tela2, width=90,justify="left")
    Substituir_por.place(x=150,y=90)
   
    
   
    def edting ():
        
        sub = Substituir.get()
        sub.upper()
        sub_por =  Substituir_por.get()
        sub_por.upper()
    
        editar(sub, sub_por)
        visao()
        
        messagebox.showinfo("Jhow Avisa", "Dados editados com sucesso!")
        
    
      #butão editar
    edit = tk.Button(tela2,command=edting,width=23,text="Alterar")
    edit.place(x=330, y=140)
    
 
def colocar ():
    
    name = nome.get()
    if len(name) < 1:
        messagebox.showerror("Jhow Avisa!", "Nome não informado!")
    else:
        name = name.upper()
    
        cpf1 = cpf.get()
        senh = senha.get()
        pag = pago.get()
        telefon = telefone.get()  

        if len(cpf1) == 11:    
            cpf1 = cpf1[:3] + '.' + cpf1[3:6] + '.' + cpf1[6:9] + '-' + cpf1[9:]
                     
            with open ("Lista_clientes_IR.csv") as file:
                desfazer = csv.reader(file)
                for linha in desfazer: 
                            
                    if cpf1 in linha:
                        n = "sim"
                    else:
                        n = "no"
            if n == "no":                          
                 
                if len(telefon) < 1:
                    
                    telefon = ("00000000000")
                    telefon = '('+telefon [:2]+') '+telefon[2]+ ' '+telefon[3:] 
                if len(telefon) > 1:
                    telefon = '('+telefon [:2]+') '+telefon[2]+ ' '+telefon[3:] 
                                    
            
                    
                if len(senh) < 1:
                    senh = "-------"
                    
                
                if len(pag) < 1:
                    pag = "nao"
                pag = pag.upper()
                
                dado = [name, cpf1, senh, telefon, pag]
                
                adicionar_cliente(dado)
                messagebox.showinfo("Jhow Avisa!", "Cliente cadastrado com sucesso!")
                
                nome.delete(0, "end")
                cpf.delete(0, "end")
                telefone.delete(0, "end")
                senha.delete(0, "end")
                pago.delete(0, "end")
                
                visao()
            else:
                messagebox.showerror("Jhow Avisa!", "CPF existente")    
                                  
        else:
            messagebox.showerror("Jhow Avisa!", "CPF possui 11 digitos verifique e tente novamente")
        
        
def excluir():
    ver_dados()
    
    
    nome.get()
    senha.get()
    telefone.get()
    pago.get()
     
    cpf1 = cpf.get()
    
    if len(cpf1) == 11:
        cpf1 = cpf1[:3] + '.' + cpf1[3:6] + '.' + cpf1[6:9] + '-' + cpf1[9:] 
        
        deletar(cpf1)   
        
        nome.delete(0, "end")
        cpf.delete(0, "end")
        senha.delete(0, "end")
        telefone.delete(0, "end")
        pago.delete(0, "end")

        messagebox.showinfo("jhow avisa!", "Cliente excluido com sucesso")   
    
    else:
         messagebox.showerror("""jhow avisa!""", """Cliente não encontrado:

Lembre-se, deletamos clientes somente pelo CPF!""")
        
    
    
    
    visao()
    
    
    
#butão adicionar
adicionar = tk.Button(frame_do_meio,command=colocar ,width=23,text="ADICIONAR")
adicionar.place(x=490, y=15)

#butão deletar
deleta = tk.Button(frame_do_meio,command=excluir,width=23,text="DELETAR")
deleta.place(x=490, y=66)

#butão editar
edtar = tk.Button(frame_do_meio,command=editarr,width=23,text="EDITAR")
edtar.place(x=490, y=120)
 
#butão editar
ver = tk.Button(frame_do_meio,command=visao ,width=23,text="VER DADOS")
ver.place(x=490, y=180)

 






tela.mainloop()