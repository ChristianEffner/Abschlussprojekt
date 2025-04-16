from Datenbank.Datenbankverbindung import Datenbankverbindung
from Datenbank.Datenabfragen import Datenbankabfragen
from Datenvisualisierung.DiagrammeErstellen import DiagrammeErstellen


def main():


    db_abfragen = Datenbankabfragen()
    diagramme = DiagrammeErstellen()

    diagramme.generiereDebitorenIMMsDiagramm(1500, 4000)

    #diagramme.generiereAktiveDebitorenDiagramm(1180, db_abfragen.holeAktiveDebitoren(['510808']))

    #diagramme.generiereAktiveUserDiagramm(db_abfragen.holeAktiveDebitoren(['510808']), db_abfragen.holeAktiveUser(['510808']))



if __name__ == "__main__":
    main()

