from Datenbank.Datenbankverbindung import Datenbankverbindung

class Datenbankabfragen:



    def holeAktiveDebitoren(self, agenten=None):

        if agenten is None:
            agenten=['510808', '505177', '505197', '524339']

        agenten_sql = "(" + ", ".join(f"'{agent}'" for agent in agenten) + ")"

        abfrage_aktive_debitoren_pro_land = f"""
                                                    SELECT COUNT(ug3.p_uid) AS 'Anzahl aktive Debitoren', ug2.p_uid AS 'Ländercode'
                                                    FROM usergroups ug1
                                                    JOIN usergroups ug2 
                                                        ON ug1.p_kmgagentgroup = ug2.usergroups_Id
                                                    JOIN usergroups ug3
                                                        ON RIGHT(ug1.p_uid, 6) = ug3.p_uid
                                                    WHERE ug2.p_uid in {agenten_sql} AND ug3.p_uid NOT IN {agenten_sql}
                                                    GROUP BY ug2.p_uid
                                                    """

        db_instance = Datenbankverbindung()
        db_verbindung = db_instance.connect()
        db_cursor = db_verbindung.cursor()
        db_cursor.execute(abfrage_aktive_debitoren_pro_land)
        db_instance.close_connection()
        results = db_cursor.fetchall()
        for x in results:
            print(x)


        return results