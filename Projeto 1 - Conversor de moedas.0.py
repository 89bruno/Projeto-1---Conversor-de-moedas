# Projeto 1 - Conversor de Reais para Euros, BitCoin e Dolares

import requests
from time import gmtime, strftime

# Passo Inicial - Entrada dos valores
nome = input("Bem-vindo(a), qual seu nome?")
reais = (input(f"""Olá {nome}, digite o valor em Reais (R$) que você deseja converter e precione enter: \n"""))

while True:
    if not reais.isnumeric():
        reais = input(f'{reais} não é um valor válido, entre com um valor numérico inteiro:')
        continue
    else:
        print(f"""Ok, vamos lá! Convertendo R${reais},00 para Dolar, Euro e Bitcoin\n""")
        break

# Obtendo as Cotações:
moeda = requests.get("https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL").json()

dolar = moeda['USDBRL']
cot_dolar = float(dolar["bid"])

euro = Moeda['EURBRL']
cot_euro = float(euro["bid"])

bitcoin = moeda['BTCBRL']
cot_bit = float(bitcoin["bid"])

# Convertendo os valores:
valor = float(reais)
reais_para_dolar = str(round((valor / cot_dolar),2)).replace('.',',')

reais_para_euro = str(round((valor / cot_euro),2)).replace('.',',')

reais_para_bit = (valor / cot_bit)
if reais_para_bit >= 1:
       novo_reais_para_bit = str(round(reais_para_bit, 2)).replace('.', ',')
else:
    novo_reais_para_bit = str(round(reais_para_bit, 3)).replace('.', ',')

# Imprimindo os resultados:
data = strftime("%d-%m-%y às %H:%M:%S", gmtime())
print (f"""Na cotação de hoje*, R${reais},00 equivalem a:
    U$ {reais_para_dolar}
    € {reais_para_euro}
    ₿ {novo_reais_para_bit}
*Cotação obtida em {data}""")


