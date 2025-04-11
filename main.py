import Datenbank
from Datenbank import Datenbankverbindung
from Datenbank import Datenabfragen

def main():
    db_verbindung = Datenbankverbindung.Datenbankverbindung()
    db_abfragen = Datenabfragen.Datenbankabfragen()


    db_abfragen.aktiveDebitorenAbfragen()
    #db_verbindung.close_connection()

if __name__ == "__main__":
    main()

