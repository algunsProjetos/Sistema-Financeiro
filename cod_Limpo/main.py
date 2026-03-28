import pandas as pd #necessario para manipulação do csv
import os #limpar terminal eventualmente 
os.system("cls") 

#recebe extrato
df_Extrato=pd.read_csv("extrato/extrato.csv", sep=";", skiprows=4,encoding="UTF-8")
print("Extrato deste mes: \n")
print(df_Extrato.to_string(index=False)) #sem indices

#valores foram enviados como str, sendo necessario float para calculos
def tranformar_string_float(coluna):
    df_Extrato[coluna]=df_Extrato[coluna].str.replace('.','').str.replace(',','.').astype(float)


valor_float=tranformar_string_float('Valor') #de string para float
saldo_float=tranformar_string_float('Saldo') #string para float

#com base nesse dicionario nos vamos filtrar cada gasto
categorias = {
    "fixos": [
        "cpfl", "sabesp", "internet", "tim", "aluguel","UNIV"
    ],
    
    "saude": [
        "academia"
    ],
    
    "lazer": [
        "spotify", "steam", "netflix", "jogos"
    ],
    
    "compras": [
        "shpp", "marketplace", "Pagseguro"
    ],
    
    "investimentos": [
        "porquinho", "aplicacao"
    ],
    
    "transferencias": [
        "marcio", "elisabete"
    ],
    "empresa":[
        "mircele", "contador"
    ],
}
"""
inicialemnte seria necessario repetir em cada categoria esse msm codigo 
para tranformar em uma planilha, por isso optei pela função: 
obs: juntar_Fixos="|".join(categorias["fixos"])
gastos_Fixos=df_Extrato[df_Extrato['Descrição'].str.contains(juntar_Fixos, case=False)]
print(gastos_Fixos)
"""

#com base no dicionario nos criamos df de cada categoria
def categorias_para_tabela(filtro):
    juntar_filtro="|".join(categorias[filtro])
    dataframe_gastos=df_Extrato[df_Extrato['Descrição'].str.contains(juntar_filtro, case=False)]
    return dataframe_gastos #apos exe retorne o dataframe 

print("\nSeus gastos fixos: \n")
df_fixos=categorias_para_tabela('fixos')
print(df_fixos)

print("\nSeus gastos em compras online: \n")
df_compras=categorias_para_tabela('compras')
print(df_compras)

print("\n Suas Transferencias: \n")
df_transferencias=categorias_para_tabela('transferencias')
print(df_transferencias)

"""
Começamos o calulo. Meu foco é separar cada tipo de gasto 
calcular sua porcentagem e filtrar entradas e saidas para analise
"""
print("\n-------------------")
print(" Suas Movimentações ")
print("-------------------\n")

#verificar oq foi pago e oq foi recebido
pago = abs(df_Extrato[df_Extrato['Valor'] < 0]['Valor'].sum())
print(f"Total de Pagamentos R${pago:.2f}")
entrada = df_Extrato[df_Extrato['Valor'] > 0]['Valor'].sum()
print(f"\nTotal de Entradas R$ {entrada:.2f}")

movimentacao=df_Extrato['Valor'].sum()
print(f"\nValor final Movimentado R$ {movimentacao:.2f}")

print("\n-------------------")
print("Seus gatos em % ")
print("-------------------")

def porcentagem_gasto(tabela):
    formula_porcentagem=((abs(tabela['Valor'].sum()))/pago)*100
    return formula_porcentagem

porcentagem_gastos_fixos=porcentagem_gasto(df_fixos)
porcentagem_gasto_compras=porcentagem_gasto(df_compras)
porcentagem_gasto_transferencias=porcentagem_gasto(df_transferencias)

print(f"\nGastos fixos representam {porcentagem_gastos_fixos:.2f}%")
print(f"\nGastos em Compras-on representam {porcentagem_gasto_compras:.2f}%")
print(f"\nGastos em Transferencias {porcentagem_gasto_transferencias:.2f}%")
