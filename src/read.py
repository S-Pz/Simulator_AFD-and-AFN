from afd import AFD
import pandas as pd
from afn import AFN

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

def read_AFN(AFN_file): 

    # Read the TSV file using pandas
    AFN_table = pd.read_csv(AFN_file, delimiter='\t')

    # Pega os estados iniciais
    cont = 0
    Qi1 = 0
    Qi2 = []

    for i in AFN_table['&']:
        if has_char(i, '!'):
            AFN_table.at[cont, '&'] = i[1:]
            if has_char(i, '*'):
                Qi1 = int(i[2:])
                Qi2.append(int(i[2:]))
            else:
                Qi1 = int(i[1:])
                Qi2.append(int(i[1:]))
        cont += 1

    Qi =  set(Qi2) 

    # Pega os estados finais
    cont = 0
    Qf = []
    for i in AFN_table['&']:
        if has_char(i, '*'):
            Qf.append(int(i[1:]))
            AFN_table.at[cont, '&'] = i[1:]
        cont += 1

    Qf = set(Qf)
    # Pega o alfabeto
    sigma = set([column for column in AFN_table.columns if column != '&'])

    # Pega os estados
    Qs = set(AFN_table['&'].unique())

    # Pega as transições
    delta = {}
    for index, row in AFN_table.iterrows():
        state = int(row[0])
        aux = {}
        for column in AFN_table.columns:
            if column != '&':
                values_list = str(row[column]).split(',')
                lista = list(map(int, values_list))
                aux[(state, column)] = set(lista)
        delta.update(aux)

    return AFN(sigma, Qs, delta, Qi, Qf)

# Specify the TSV file path
#AFD_file = 'data.tsv'
#D1 = read_AFD(AFD_file)
#print(D1.sigma)
#print(D1.Q)
#print(D1.delta)
#print(D1.q0)
#print(D1.qf)
#print("___________")
#AFN_file = 'date2.tsv'
#D0 = read_AFN(AFN_file)
#print(D0.sigma)
#print(D0.Q)
#print(D0.delta)
#print(D0.q0)
#print(D0.qf)

#print(D0.run("11"))#true
#print(D0.run("01"))#false
#print(D0.run("10"))#true
#print(D0.run("00"))#false


#print(D0.delta)
#print(D0.run("bb"))
#D1 = AFD({"a","b"},{0,1,2},{(0,"a"):0,(0,"b"):1,(1,"a"):2,(1,"b"):1,(2,"a"):2,(2,"b"):2}, 0, {0,1})
#print(D1.run("ab"))
#print(D0.delta[(0,'a')])
