from Datenbank import Datenbankverbindung

class Datenbankabfragen:


    def aktiveDebitorenAbfragen(self):

        abfrage_aktive_Debitoren_pro_Land = """
                                            SELECT COUNT(ug3.p_uid) AS 'Anzahl aktive Debitoren', ug2.p_uid AS 'Ländercode'
                                            FROM usergroups ug1
                                            JOIN usergroups ug2 
                                                ON ug1.p_kmgagentgroup = ug2.usergroups_Id
                                            JOIN usergroups ug3
                                                ON RIGHT(ug1.p_uid, 6) = ug3.p_uid
                                            WHERE ug2.p_uid in ('510808', '505177', '505197', '524339') AND ug3.p_uid NOT IN ('510808', '505177', '505197', '524339')
                                            GROUP BY ug2.p_uid
                                            """

        db_instance = Datenbankverbindung.Datenbankverbindung()
        db_verbindung = db_instance.connect()
        db_cursor = db_verbindung.cursor()
        db_cursor.execute(abfrage_aktive_Debitoren_pro_Land)
        result = db_cursor.fetchall()
        for x in result:
            print(x)