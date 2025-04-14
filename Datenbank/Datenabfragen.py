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

    def holeAktiveUser(self, users=None):

        if users is None:
            users=['510808', '505177', '505197', '524339']

        users_sql = "(" + ", ".join(f"'{user}'" for user in users) + ")"

        abfrage_aktive_user_pro_land = f"""
                                        SELECT ug2.p_uid AS 'aktive Debitoren', COUNT(*) AS 'Anzahl Users'
                                        FROM
                                            usergroups ug1
                                        JOIN
                                            usergroups ug2
                                            ON ug1.p_kmgagentgroup = ug2.usergroups_Id
                                        JOIN
                                            usergroups ug3
                                            ON RIGHT(ug1.p_uid, 6) = ug3.p_uid
                                        JOIN
                                            (
                                                SELECT
                                                    us.p_uid as user_id,
                                                    us.p_name as user_name, 
                                                    ug4.p_uid AS user_debitor
                                                FROM
                                                    users us
                                                LEFT JOIN pgrels rel1
                                                ON us.user_Id = rel1.SourcePK
                                                LEFT JOIN usergroups ug4
                                                ON rel1.TargetPK = ug4.usergroups_Id
                                               LEFT JOIN pgrels rel2
                                                ON ug4.usergroups_Id = rel2.SourcePK
                                            ) AS usercompanies
                                            ON ug3.p_uid = usercompanies.user_debitor
                                        WHERE ug2.p_uid in {users_sql} AND ug3.p_uid NOT IN {users_sql}
                                        GROUP BY 1
                                        ORDER BY 2 DESC
                                        """

        db_instance = Datenbankverbindung()
        db_verbindung = db_instance.connect()
        db_cursor = db_verbindung.cursor()
        db_cursor.execute(abfrage_aktive_user_pro_land)
        db_instance.close_connection()
        results = db_cursor.fetchall()
        for x in results:
            print(x)

        return results