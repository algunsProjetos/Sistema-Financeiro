import pandas as pd #biblioca para trabalhar com csv
import os 


os.system("cls")
extrato = pd.read_csv("extrato.csv", sep=";", skiprows=4,
                  usecols=["Data Lançamento", "Histórico", "Descrição", "Valor"]) #nome do arquivo, separado por ';' pula ladainha do Inter
print(extrato.to_string(index=False))

"""extrato['Valor'] = extrato['Valor'].str.replace(',','.')
extrato['Valor'] = extrato['Valor'].astype(float)"""


"""
Encontrei essa resp aqui: 
https://cursos.alura.com.br/forum/topico-duvida-como-
converter-coluna-object-exemplo-r-2-500-00-em-ns-
float-em-python-290333
"""

tabela = pd.DataFrame(extrato) #tranformando em tabela


# Removendo o 'R$' e as vírgulas da coluna 'valor' e convertendo para float
tabela['Valor'] = (
    tabela['Valor']
    .str.replace('.', '') #regex=falso: apenas faça oq pedi. Reges tru=-3631.5499999999997 Regex falso=-3631.5499999999997
    .str.replace(',', '.')
    .astype(float)
)

""""
Lembrar de perguntar para o professor sobre regex, 
gpt errado-> regex no pandas atual
"""

total = tabela['Valor'].sum()
print(f"\n Gosto total do mes  R$ {total:.2f}")
#operador ternario
ana_Gasto="\n Saldo negativo :( \n" if total<0 else "\n Saldo Positivo :)"
print(ana_Gasto)



print("\n -- Apenas o Essencial -- \n")
essencial = extrato[extrato["Descrição"].str.contains("TIM|uber|ifood|cpfl|desktop|nu|sagr coracao|Growth", case=False)] #ignorar casos diferentes, considere oq eu escrevi

tabela_Essencial=pd.DataFrame(essencial)

# Removendo o 'R$' e as vírgulas da coluna 'valor' e convertendo para float
tabela_Essencial['Valor'] = (
    tabela_Essencial['Valor']
    .str.replace('.', '') #regex=falso: apenas faça oq pedi. Reges tru=-3631.5499999999997 Regex falso=-3631.5499999999997
    .str.replace(',', '.')
    .astype(float)
)



print(essencial.to_string(index=False)) #ignorar os ponteiros
total_Essencial=tabela_Essencial["Valor"].sum()
print(f"\n Seus Gasto Essenciais R$ {total_Essencial:.2f}\n")

#valor total da fatura - gastos = descubro quanto foi gasto em essenciais:
SubEssencial=(total)-(total_Essencial)
#operador ternario
ana_Gastos_Essenciais="\n Grande parte dos seus gastos são Essenciais :( \n" if total_Essencial>total else "\n Parte dos seus gastos são Essencias, mas voce esta indo bem :)"
print(ana_Gasto)

if total_Essencial>total:
          print(f"\nGastos essenciais R${total_Essencial:.2f}")
          print(f"\nSeus gastos essenciais exedem seu valor mensal de R${total}")
          print(f"\nCerca de {SubEssencial/100:.2f}% são gastos em produtos e serviços essenciais ")




"""tudo q tiver TIM|uber|ifood|cpfl|desktop|nu|sagr coracao 
considere essencial ignorando letras diferentes"""
"""#os.system("cls")
print("\n -- Apenas o Essencial -- \n")
essencial = extrato[extrato["Descrição"].str.contains("TIM|uber|ifood|cpfl|desktop|nu|sagr coracao|Growth", case=False)] 
print(essencial.to_string(index=False)) #nao mestre indice"""



"""luz = extrato[extrato["Descrição"].str.contains("cpfl", case=False)] 
print(luz)"""





"""#informa apenas oq o usuario quer saber
entradaUser=input("Informe a transação que deseja acessar: ")
try:
      print(extrato.loc[entradaUser])
except erro:
      print(f"{entradaUser} não encontrada")"""
"""
extrato.loc[len(extrato)] = ["23/03/2026", "Pix enviado", "cpfl paulista", -50.00, 200.00]
linha teste
"""
"""luz = extrato[extrato['Descrição'].str.contains('cpfl', case=False)]
agua = extrato[extrato['Descrição'].str.contains('sabesp', case=False)]
print(luz,agua)"""""