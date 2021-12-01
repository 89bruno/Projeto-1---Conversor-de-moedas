# Projeto 1 - Conversor de Reais para Euros, BitCoin e Dolares

import requests
from time import gmtime, strftime

class ConversorDeMoedas:
    def __init__(self):
        self.recebendo_entradas()
        self.validando_entrada()
        self.obtendo_cotacoes()
        self.convertendo()
        self.imprimindo_resultado()

    def recebendo_entradas(self):
        self.reais = input(f'Olá, digite o valor em Reais (R$) que você deseja converter e precione enter: \n')
        return self.reais

    def validando_entrada(self):
        while True:
            try:
                self.reais = str(self.reais).replace(",",".")
                self.reais = float(self.reais)
                print(f"Ok, convertendo R${self.reais}")
                return self.reais
            except:
                self.reais = input("Você não digitou um valor inválido,"
                                   " insira novamente o valor que deseja converter")
                continue

    def obtendo_cotacoes(self):
        moeda = requests.get("https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL").json()

        dolar = moeda['USDBRL']
        self.cot_dolar = float(dolar["bid"])

        euro = moeda['EURBRL']
        self.cot_euro = float(euro["bid"])

        bitcoin = moeda['BTCBRL']
        self.cot_bit = float(bitcoin["bid"])
        return self.cot_dolar, self.cot_euro, self.cot_bit

    def convertendo(self):
        self.reais_para_dolar = round(float(self.reais) / float(self.cot_dolar),2)
        self.reais_para_euro = round(float(self.reais) / float(self.cot_euro),2)
        self.reais_para_bit = float(self.reais) / float(self.cot_bit)
        if self.reais_para_bit > 1:
            self.novo_reais_para_bit = round(self.reais_para_bit, 2)
        else:
            self.novo_reais_para_bit = round(self.reais_para_bit,3)
        return self.novo_reais_para_bit, self.reais_para_dolar, self.reais_para_euro

    def imprimindo_resultado(self):
        data = strftime("%d-%m-%y às %H:%M:%S", gmtime())
        print(f"""Na cotação de hoje*, R${self.reais} equivalem a:
            U$ {self.reais_para_dolar}
            € {self.reais_para_euro}
            ₿ {self.novo_reais_para_bit}
        *Cotação obtida em {data}""")


if (__name__ == "__main__"):
    ConversorDeMoedas()



