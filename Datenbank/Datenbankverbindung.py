import mysql.connector
import configparser

class Datenbankverbindung:

        def __init__(self):
            self.connection = None

        def getProperties(self):
            """
            Liest die Datenbank-Konfiguration aus der config.ini und
            gibt den Abschnitt 'Datenbank' als Dictionary Objekt zurück.
            """
            config = configparser.ConfigParser()
            config.read('Datenbank/config.ini')
            if 'Datenbank' in config:
                return config['Datenbank']
            else:
                raise ValueError("In der config.ini wurde kein [Datenbank]-Abschnitt gefunden!")


        def connect(self):
            """
            Stellt eine Verbindung zur Datenbank her, indem ausschließlich die in getProperties
            gelesenen Konfigurationswerte verwendet werden ohne das die Werte preisgegeben werden
            """
            props = self.getProperties()

            try:
                self.connection = mysql.connector.connect(
                    host=props.get('host'),
                    user=props.get('user'),
                    password=props.get('password'),
                    database=props.get('database'),
                    charset=props.get('charset'),
                    collation=props.get('collation')
                )
                print("Verbindung zur Datenbank wurde hergestellt.")

            except mysql.connector.Error as err:
                print("Fehler bei der Verbindung:", err)
                self.connection = None

            return self.connection



        def close_connection(self):
            if self.connection:
                try:
                    self.connection.close()
                    print("Verbindung wurde erfolgreich geschlossen.")
                except Exception as e:
                    print("Fehler beim Schließen der Verbindung:", e)
            else:
                print("Es besteht keine Verbindung, die geschlossen werden kann.")
