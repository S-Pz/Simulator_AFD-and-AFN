from afd import AFD
import pandas as pd

def read_AFD(AFD_file): 

    # Read the TSV file using pandas
    AFD_table = pd.read_csv(AFD_file, delimiter='\t')
    # pega o alfabeto
    sigma = [] 
    for column in AFD_table.columns:
        sigma.append(column)
    sigma = sigma[1:]
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
                aux.update({(row[0],column):row[column]})
            #aux.append(row[column])

        delta.update(aux)
    #pega os estados inicial e final
    Qi = AFD_table.iloc[0,1] 
    Qf = AFD_table[AFD_table['&'].str.contains('\*', regex=False)]

    AFD(sigma,Qs,delta,Qi,Qf)
    return AFD

# Specify the TSV file path
AFD_file = 'data.tsv'
Dfas = read_AFD(AFD_file)
Dfas.run("ab")