"""
Nossa ideia foi elaborar um sistema funional que receba o extrato do usuario (limitado a csv)
mostra no terminal (futuramente em uma interface) 
limpa 
soma valores movimentados 
printa total
separa serviços essenciais, faturas/parcelas, luxos/hobbies (levantamento geral de gastos)
calculos necessarios em porcetagem de cada serviço 
traduz em grafico de pizza

atualizações futuras:
1-usuario podera informar gastos add(como pg em dinheiro) 
e em qual serviço se encontra, alterando o valor dos calculos simultaneamente.
2-intarface que funcione fora do terminal. 
pessoal: separar por pastas, limpar codigo add funções.
"""
import pandas as pd #necessario para manipulação do csv
import os #limpar terminal eventualmente 

os.system("cls") #limpar terminal
df_Extrato=pd.read_csv("extrato/teste_extrato.csv", sep=";", skiprows=4,encoding="UTF-8") #leia o extrato separado por ';' pule as 4 primeiras linhas
"""
Pq usar format ou dayfirst=True? o pandas avisa q a data esta em portugues, mas ele 
interpreta da forma americana. O mais correto é passar o formato(format="%d/%m/%Y") ou 
apenas dizer que o dia vem primeiro pois estamos no brasil
obs: format foi encontrado aqui: https://pandas.pydata.org/docs/reference/api/pandas.
to_datetime.html
"""
#convertendo string de data para datatime
df_Extrato["Data Lançamento"]=pd.to_datetime(df_Extrato["Data Lançamento"],format="%d/%m/%Y")
"""
Como converter valor str do CSV para float?
Resposta encontrada aqui: https://pt.stackoverflow.com/questions/446803/
convers%C3%A3o-de-object-para-float
e aqui:
https://cursos.alura.com.br/forum/topico-duvida-como-
converter-coluna-object-exemplo-r-2-500-00-em-ns-float-em-python-290333
"""
#converter para valor float
df_Extrato['Valor'] = df_Extrato["Valor"].str.replace('.','').str.replace(',','.').astype(float)
df_Extrato['Saldo'] = df_Extrato["Saldo"].str.replace('.','').str.replace(',','.').astype(float)
print(df_Extrato)
#quanto movimentei ao longo do mes (inclui saidas e entradas) 
movimentacao_Valor=df_Extrato["Valor"].sum()
print(f"Valores movimentados: R$ {movimentacao_Valor:.2f}")
#dessas movimentações, quanto foram entradas: #perguntar para o professor
entrada = df_Extrato[df_Extrato['Valor'] > 0]['Valor'].sum()
print(f"Entradas R$ {entrada:.2f}")
#e saidas? #perguntar para o professor
saida = df_Extrato[df_Extrato['Valor'] < 0]['Valor'].sum()
print(f"Saida R$ {saida:.2f}")



#e quanto foi saida

#localiza meu saldo final
saldo_Final_Mes=df_Extrato.loc[0,'Saldo']

"""
https://www.youtube.com/watch?v=rHxy-AxwsTU
SHIFT+\=|
"""

#NEXT: separar essenciais e outros
essenciais=df_Extrato[df_Extrato['Descrição'].str.contains('cpfl|sabesp|coracao|internet|desktop|dae|uber|casolina|mercado|vero|telefonica|energia|agua|esgoto', case=False)]
total_essencial=essenciais['Valor'].sum()
print(essenciais)
print(f"Valores Essenciais movimentados: R$ {total_essencial:.2f}")

#calcular porcentagem do que é essencial.
"""Qual a porcentagem dos meu pagamentos essenciais em relação aos pagamentos da conta? """
porcentagem_Essencial=(total_essencial/saida)*100
print(f"Serviços Essenciais representam cerca de {porcentagem_Essencial:.2f}%")
#Não essencial: 
nao_Essencial=total_essencial-saida
porcentagem_Nao_Essencial=(nao_Essencial/saida)*100
print(f"Total de Serviços não Essencias R$ {nao_Essencial}")
print(f"Serviços Não Essenciais representam cerca de {porcentagem_Nao_Essencial:.2f}%")

#verificar oq gasta mais: essencial vs n essencial