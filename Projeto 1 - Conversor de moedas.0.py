# Projeto 1 - Conversor de Reais para Euros, BitCoin e Dolares

import requests
from time import gmtime, strftime

# Passo Inicial - Entrada dos valores
Nome = input("Bem-vindo(a), qual seu nome?")
Reais = (input(f"""Olá {Nome}, digite o valor em Reais (R$) que você deseja converter e precione enter: \n"""))

while True:
    if not Reais.isnumeric():
        Reais = input(f'{Reais} não é um valor válido, entre com um valor numérico inteiro:')
        continue
    else:
        print(f"""Ok, vamos lá! Convertendo R${Reais},00 para Dolar, Euro e Bitcoin\n""")
        break

# Obtendo as Cotações:
Moeda = requests.get("https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL").json()

Dolar = Moeda['USDBRL']
CotDolar = float(Dolar["bid"])

Euro = Moeda['EURBRL']
CotEuro = float(Euro["bid"])

Bitcoin = Moeda['BTCBRL']
CotBit = float(Bitcoin["bid"])

# Convertendo os valores:
Valor = float(Reais)
ReaisToDolar = str(round((Valor / CotDolar),2)).replace('.',',')

ReaisToEuro = str(round((Valor / CotEuro),2)).replace('.',',')

ReaisToBit = (Valor / CotBit)
if ReaisToBit >= 1:
       NovoReaisToBit = str(round(ReaisToBit, 2)).replace('.', ',')
else:
    NovoReaisToBit = str(round(ReaisToBit, 3)).replace('.', ',')

# Imprimindo os resultados:
Data = strftime("%d-%m-%y às %H:%M:%S", gmtime())
print (f"""Na cotação de hoje*, R${Reais},00 equivalem a:
    U$ {ReaisToDolar}
    € {ReaisToEuro}
    ₿ {NovoReaisToBit}
*Cotação obtida em {Data}""")


