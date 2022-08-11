import sqlite3
#что не так то...хз
# class Import_data:
#     def __int__(self, base_data, path_to_basedata, condition):
#         self.base_data = base_data
#         self.path_to_base_data = path_to_basedata
#         self.condition = condition
#
#     def import_data(self):
#         with sqlite3.connect(self.path_to_base_data) as connection:
#             cur = connection.cursor()
#             sqlite_query = (f"""SELECT *
#                                 FROM {self.base_data}
#                                 condition
#                             """
#                             )
#             cur.execute(sqlite_query)
#             res = []
#             for row in cur.fetchall():
#                 res.append(row)
#
#             return res
#
# film = Import_data()
# print(film("netflix", "../../data/netflix.db"))


def load_data():
    with sqlite3.connect("../../data/netflix.db") as connection:
        cur = connection.cursor()
        sqlite_query = ("""
                            SELECT title, country, release_year, description
                            FROM netflix
                            LIMIT 10
                            """
                            )
        cur.execute(sqlite_query)
        for row in cur.fetchall():
            return row

print(load_data())
