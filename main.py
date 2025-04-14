from Datenbank.Datenbankverbindung import Datenbankverbindung
from Datenbank.Datenabfragen import Datenbankabfragen

def main():


    db_verbindung = Datenbankverbindung()
    db_abfragen = Datenbankabfragen()


    db_abfragen.holeAktiveDebitoren(['510808'])
    db_abfragen.holeAktiveUser(['510808'])


if __name__ == "__main__":
    main()

