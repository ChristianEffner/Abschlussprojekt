import os
import matplotlib.pyplot as plt

class DiagrammeErstellen:

    def __init__(self):
        # Dictionary für Ländercodes und dazugehörigen Länder
        self.country_dict = {"510808": "Germany", "505177": "USA", "505197": "Schweiz", "524339": "BeNeLux"}

    #Funktion zur Generierung von dem Diagramm aktive Debitoren pro Land
    def generiereAktiveDebitorenDiagramm(self, gesamtanzahl, debitoren):

        #Parameter debitoren ist ein Tupel aus der Anzahl und dem Ländercode, diese werden mit einer Schleife iteriert
        for anzahlDebitoren, laendercode in debitoren:

            #Wenn der Ländercode im Dictionary vorhanden ist wird das Diagramm generiert
            if laendercode in self.country_dict:

                # Daten für das Diagramm
                land_name = self.country_dict[laendercode]
                anzahlDebitor = anzahlDebitoren
                kategorien = ['All Debitors', 'Debitors ' + land_name]
                werte = [gesamtanzahl, anzahlDebitor]

                # Zur Ausrichtung der Balken
                x_positionen = [0, 1]
                balken_breite = 0.3

                # Erstelle das Balkendiagramm
                plt.bar(x_positionen, werte, width=balken_breite, color=["royalblue", "dodgerblue"])

                # Beschriftungen auf der x-Achse setzen
                plt.xticks(x_positionen, kategorien)

                # Oberes Limit der y-Achse festlegen
                plt.ylim(0, gesamtanzahl + 300)

                # Gitterlinien
                plt.grid(axis='y', linestyle='-', color='grey', alpha=0.7)

                # Beschriftung für die Balken
                for i, wert in enumerate(werte):
                    plt.text(x_positionen[i], wert, str(wert), ha='center', va='bottom', fontsize=8)

                # Rahmen oben und rechts entfernen
                ax = plt.gca()
                ax.spines['top'].set_visible(False)
                ax.spines['right'].set_visible(False)

                # Titel hinzufügen
                plt.title("aktiv Debitors " + land_name)

                # Pfad zur Speicherung der Diagramme
                pfad = 'Diagramme'

                # Sicherstellung ob Pfad existiert
                if not os.path.exists(pfad):
                    os.makedirs(pfad)

                # Speicherung Diagramm
                dateiname = f"aktiv Debitors {land_name}.png"
                voller_dateiname = os.path.join(pfad, dateiname)
                plt.savefig(voller_dateiname, dpi=300, bbox_inches='tight')
                plt.close()

            #Wenn Ländercode nicht vorhanden ist
            else:
                print("Ländercode " + laendercode + " nicht gefunden")

    # Funktion zur Generierung des Diagramms aktive User
    def generiereAktiveUserDiagramm(self, debitoren_funktion, user_funktion):

        # For Schleife um durch die Liste von Tupeln zu iterieren, von der Funktion des ersten Parameters
        for debitor, landercode in debitoren_funktion:

            # Überprüfen, ob Ländercode im Dictionary vorhanden ist
            if landercode in self.country_dict:

                # Temporäre Variable zum Speichern der identischen User
                matching_user = None

                # For Schleife um durch die Liste von Tupeln zu iterieren, von der Funktion des zweiten Parameters
                for lc, user in user_funktion:

                    # Prüfen, ob die beiden Ländercodes der Parameter identisch sind
                    if lc == landercode:
                        matching_user = user
                        #sobald der passende Eintrag gefunden ist, kann die Schleife beendet werden, da sonst nicht zugehörige Werte in Diagrammen dargestellt werden
                        break

                if matching_user is None:
                    print("Kein passender User für Ländercode " + landercode + " gefunden")


                else:

                    # Daten für das Diagramm
                    laendername = self.country_dict[landercode]
                    anzahl_debitoren = debitor
                    anzahl_user = matching_user
                    kategorien = ['aktiv Debitors', 'users']
                    werte = [anzahl_debitoren, anzahl_user]

                    x_positionen = [0, 1]
                    balken_breite = 0.3

                    # Balkendiagramm erstellen
                    plt.bar(x_positionen, werte, width=balken_breite, color=["royalblue", "orangered"])
                    plt.xticks(x_positionen, kategorien)
                    plt.ylim(0, matching_user + 150)
                    plt.grid(axis='y', linestyle='-', color='grey', alpha=0.7)

                    # Balken mit Werten beschriften
                    for i, wert in enumerate(werte):
                        plt.text(x_positionen[i], wert, str(wert), ha='center', va='bottom', fontsize=8)

                    # Rahmen oben und rechts entfernen
                    ax = plt.gca()
                    ax.spines['top'].set_visible(False)
                    ax.spines['right'].set_visible(False)

                    # Titel setzen
                    plt.title("aktiv Users " + laendername)

                    # Diagramm in Verzeichnis speichern
                    pfad = 'Diagramme'

                    # Stelle sicher, dass das Verzeichnis existiert
                    if not os.path.exists(pfad):
                        os.makedirs(pfad)
                    dateiname = f"aktiv Users {laendername}.png"
                    voller_dateiname = os.path.join(pfad, dateiname)
                    plt.savefig(voller_dateiname, dpi=300, bbox_inches='tight')
                    plt.close()

            else:
                print("Ländercode " + landercode + " nicht gefunden")



    def generiereDebitorenIMMsDiagramm(self, debitoren, imms):

        #Daten für Diagramm
        anzahl_debitoren = debitoren
        anzahl_imms = imms
        kategorien = ['Debitors', 'IMMs']
        werte = [anzahl_debitoren, anzahl_imms]
        x_positionen = [0, 1]
        balken_breite = 0.3

        #Diagramm erstellen
        plt.bar(x_positionen, werte, width=balken_breite, color=["royalblue", "orangered"])
        plt.xticks(x_positionen, kategorien)
        plt.ylim(0, anzahl_imms + 500)
        plt.grid(axis='y', linestyle='-', color='grey', alpha=0.7)

        # Balken mit Werten beschriften
        for i, wert in enumerate(werte):
            plt.text(x_positionen[i], wert, str(wert), ha='center', va='bottom', fontsize=8)

        # Rahmen oben und rechts entfernen
        ax = plt.gca()
        ax.spines['top'].set_visible(False)
        ax.spines['right'].set_visible(False)

        # Titel setzen
        plt.title("database")

        # Diagramm in Verzeichnis speichern
        pfad = 'Diagramme'

        # Stelle sicher, dass das Verzeichnis existiert
        if not os.path.exists(pfad):
            os.makedirs(pfad)
        dateiname = "database.png"
        voller_dateiname = os.path.join(pfad, dateiname)
        plt.savefig(voller_dateiname, dpi=300, bbox_inches='tight')
        plt.close()








