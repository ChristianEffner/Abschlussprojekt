from Datenbank import Datenbankverbindung

class Datenbankabfragen:


    def aktiveDebitorenAbfragen(self, agenten=['510808', '505177', '505197', '524339']): # hier sagen wir das der default die 4 agenten sein sollen
    
       agenten_sql = "(" + [f"'{agent}'"  for agent in agenten] + ")" # hier wandeln wir die agenten_liste aus dem parameter in einem sql string, also wir fügen single-quotes für jede angenten nummer und packen es in runde klammern

        abfrage_aktive_Debitoren_pro_Land = f"""
                                            SELECT COUNT(ug3.p_uid) AS 'Anzahl aktive Debitoren', ug2.p_uid AS 'Ländercode'
                                            FROM usergroups ug1
                                            JOIN usergroups ug2 
                                                ON ug1.p_kmgagentgroup = ug2.usergroups_Id
                                            JOIN usergroups ug3
                                                ON RIGHT(ug1.p_uid, 6) = ug3.p_uid
                                            WHERE ug2.p_uid in {agenten_sql} AND ug3.p_uid NOT IN {agenten_sql }
                                            GROUP BY ug2.p_uid
                                            """

        db_instance = Datenbankverbindung.Datenbankverbindung() #du kannst in deinem import auc schreiben from Datenbankverbindung import Datenbankverbindung  und den Befehl als db_instance = Datenbankverbindung() schreiben
        db_verbindung = db_instance.connect()
        db_cursor = db_verbindung.cursor()
        db_cursor.execute(abfrage_aktive_Debitoren_pro_Land)
        # hier müsstest du die Verbindung auch wieder schließen, auch würde es sin machen, deinen abfragen, eine datenbankverbindungscursor instanz zu übergeben, oder du instanzierst die Datenbankverbindung in einer __init__ methode
        results = db_cursor.fetchall() # da du hier multiple result(s) kannst du den plural nehmen
        for x in results:
            print(x) 
           
        # deine funktion sollte ideallerweise etwas zurückgeben, hier in deinem Fall results
        return results