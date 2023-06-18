
from afd import AFD
import pandas as pd


def has_char(string, char):
    return char in string

def read_AFD(AFD_file): 

    # Read the TSV file using pandas
    AFD_table = pd.read_csv(AFD_file, delimiter='\t')

    #pega os estados inicial e final
    cont = 0
    Qi = 0
    for i in AFD_table['&']:
        if has_char(i,'!') == True:
            AFD_table.at[cont, '&'] = i[1:]
            if has_char(i,'!') == True:
                Qi = int(i[2:])
                #Qi.append(i[2:])
            else:
                Qi = int(i[1:])
                #Qi.append(i[1:])
        cont +=1
    
    cont = 0
    Qf = []
    for i in AFD_table['&']:
        if has_char(i,'*') == True: # Verificar se algum valor contém o caractere "*"
            Qf.append(int(i[1:]))
            AFD_table.at[cont, '&'] = i[1:]
        cont +=1
    # pega o alfabeto
    sigma = [] 
    for column in AFD_table.columns:
        if column != '&':
            sigma.append(column)
    # pega os estados
    Qs = AFD_table['&'].unique()
    Qs = Qs[1:]
    # pega as transicoes
    delta = {}
    for index, row in AFD_table.iterrows():
        #print(f"Row index: {index}")
        aux = {}
        for column in AFD_table.columns:
            if column != '&':
                aux.update({(int(row[0]),column):row[column]})
            #aux.append(row[column])

        delta.update(aux)
    return AFD(sigma,Qs,delta,Qi,Qf)

def read_AFN(AFD_file): 

    # Read the TSV file using pandas
    AFD_table = pd.read_csv(AFD_file, delimiter='\t')

    #pega os estados iniciais
    cont = 0
    aux = 0
    Qi1 = 0
    Qi2 = []
    for i in AFD_table['&']:
        if has_char(i,'!') == True: # Verificar se algum valor contém o caractere "!"
            AFD_table.at[cont, '&'] = i[1:]
            if has_char(i,'*') == True:
                Qi1 = int(i[2:])
                Qi2.append(i[2:])
                aux += aux
            else:
                Qi1 = int(i[1:])
                Qi2.append(i[1:])
                aux += aux
        cont +=1
    if(aux > 1):
        Qi = Qi2
    else:
        Qi = Qi1

     #pega os estados finais
    cont = 0
    Qf = []
    for i in AFD_table['&']:
        if has_char(i,'*') == True: # Verificar se algum valor contém o caractere "*"
            Qf.append(int(i[1:]))
            AFD_table.at[cont, '&'] = i[1:]
        cont +=1

    # pega o alfabeto
    sigma = [] 
    for column in AFD_table.columns:
        if column != '&':
            sigma.append(column)

    # pega os estados
    Qs = AFD_table['&'].unique()
    Qs = Qs[1:]

    # pega as transicoes
    delta = {}
    for index, row in AFD_table.iterrows():
        #print(f"Row index: {index}")
        aux = {}
        for column in AFD_table.columns:
            if column != '&':
                values_list = [int(value) for value in row[column].split(',')]
                aux.update({(int(row[0]),column):values_list})
            #aux.append(row[column])
        delta.update(aux)

    return AFD(sigma,Qs,delta,Qi,Qf)

# Specify the TSV file path
AFD_file = 'data.tsv'
D0 = read_AFD(AFD_file)
#print(D0.delta)
print(D0.run("bb"))
#D1 = AFD({"a","b"},{0,1,2},{(0,"a"):0,(0,"b"):1,(1,"a"):2,(1,"b"):1,(2,"a"):2,(2,"b"):2}, 0, {0,1})
#print(D1.run("ab"))
#print(D0.delta[(0,'a')])

