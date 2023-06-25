# Simulator_AFD-and-AFN
Simulador de autômatos finitos determinísticos (AFD) e autômatos finitos não determinísticos (AFN).
<p>Manual</p>
<p>Para escrever o arquivo deve-se seguir o seguinte padrão:</p>
<p>O arquivo é um TSV, A primeira linha deve conter o simbolo '&', que indica a coluna de estados, em seguida as próximas colunas serão os simbolos do alfabeto.</p>
<p>As próximas linhas contem as transicões em si</p>
<p>O simbolo '!' antes do estado indica que ele é um estado inicial</p>
<p>O simbolo '*' antes do estado indica que ele é um estado final</p>
<p>Arquivo de Exemplo: data.tsv</p>

# Entrada Manual
## Como fazer a entrada manual

#N0 = AFN({"0","1"},{0,1,2},{(0,"0"):{0},(0,"1"):{0,1},(1,"0"):{2},(1,"1"):{2}},{0},{2})