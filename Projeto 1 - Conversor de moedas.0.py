import requests
from time import gmtime, strftime

class ConversorDeMoedas:
    def __init__(self):
        self.recebendo_entradas()
        self.validando_entrada()
        self.obtendo_cotacoes()
        self.convertendo()
        self.registrando_data()
        self.imprimindo_resultado()

    def recebendo_entradas(self):
        self.reais = input('Olá, digite o valor em Reais (R$) que você deseja converter e precione enter: \n')
        return self.reais

    def validando_entrada(self):
        while True:
            try:
                self.reais = str(self.reais).replace(",",".")
                self.reais = float(self.reais)
                print("Ok, vamos converter R${:.2f} em Euro, Dolar e BitCoin".format(self.reais))
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
        self.cot_btc = float(bitcoin["bid"])
        return self.cot_dolar, self.cot_euro, self.cot_btc

    def convertendo(self):
        self.reais_dolar = round(self.reais / self.cot_dolar,2)
        self.reais_euro  = round(self.reais / self.cot_euro,2)
        self.reais_bitcoin   = self.reais / self.cot_btc
        if self.reais_bitcoin > 1:
            self.reais_btc = round(self.reais_bitcoin,2)
        else:
            self.reais_btc = round(self.reais_bitcoin,3)
        return self.reais_dolar, self.reais_btc, self.reais_euro
    
    def  registrando_data(self):
        self.data = strftime("%d-%m-%y às %H:%M:%S", gmtime())
        return self.data
    
    def imprimindo_resultado(self):
        print(f"""Na cotação de hoje*, R${self.reais} equivalem a:
            U$ {self.reais_dolar}
            € {self.reais_euro}
            ₿ {self.reais_btc}
        *Cotação obtida em {self.data}""")

ConversorDeMoedas()



