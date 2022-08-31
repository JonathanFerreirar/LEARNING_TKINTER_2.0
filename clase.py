import pandas





def adicionar_cliente (x):
    import pandas
    
    with open("Lista_clientes_IR.csv") as file:       
    
        arquivo = pandas.read_csv(file)

        lista_iR = pandas.DataFrame(data=arquivo) #Transformando em dataframe para alterar com facilidade.
        
        lista_iR = lista_iR.drop(columns='Unnamed: 0') # Dropando a coluna
        
        tamanho = len(lista_iR) # Lendo o tamanho do arquivo
                        
        lista_iR.loc[tamanho] = (x)
                
        lista_iR.to_csv('Lista_clientes_IR.csv')
    
    
 
    
    
def deletar (x):
    import pandas         
        
    desfazer = pandas.read_csv('Lista_clientes_IR.csv')

    desfazer = desfazer.drop(columns='Unnamed: 0')
    desfazendo = (x)

    for index, row in desfazer.iterrows():
        for Palavra in row:
                
            if desfazendo in str(Palavra):                                        
            
                desfazer_do_index = (index)           
                
                desfazendo_da_linha = desfazer.drop(index=(desfazer_do_index))

                Resetando = desfazendo_da_linha.reset_index(drop=True)

                Resetando.to_csv('Lista_clientes_IR.csv')
  


def ver_dados ():
    
    dados = []
    with open("Lista_clientes_IR.csv") as file:
        ler_csv = pandas.read_csv(file)
        ler_csv = ler_csv.drop(columns='Unnamed: 0')
        for linha in ler_csv.itertuples():
            n = [(linha.NOME), (linha.CPF),(linha.SENHA),(linha.TELEFONE),(linha.PAGO)]
            dados.append(n)
    
        return dados  
    
    
    
def editar (x,y):
    import pandas
        
    lista_iR = pandas.read_csv('Lista_clientes_IR.csv')

    lista_iR = pandas.DataFrame(data=lista_iR)

    lista_iR = lista_iR.drop(columns='Unnamed: 0')

    lista_iR = lista_iR.replace([x], y)      
    
    lista_iR.to_csv('Lista_clientes_IR.csv')
    
    
        

    
 
        
        
        
