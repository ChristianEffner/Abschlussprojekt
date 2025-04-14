from matplotlib import pyplot as plt

class AktiveDebitoren:


    def generiereAktiveDebitorenDiagramm(gesamtanzahl, debitoren):

        country_dict = {"510808": "Germany", "505177": "USA", "505197": "China", "524339": "BeNeLux"}

        for anzahlDebitoren, laendercode in debitoren:
            if laendercode in country_dict:
                land_name = country_dict[laendercode]
                anzahlDebitor = anzahlDebitoren







