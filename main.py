from Datenbank import Datenbankverbindung

def main():
    db_verbindung = Datenbankverbindung.Datenbankverbindung()

    db_verbindung.connect()
    db_verbindung.close_connection()

if __name__ == "__main__":
    main()

