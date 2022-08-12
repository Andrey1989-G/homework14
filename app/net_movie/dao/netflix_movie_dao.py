import sqlite3

from app.config import DATA_DIR

DATA_PATH = DATA_DIR.joinpath("netflix.db")
# колумнс в базе данных show_id, type,  title, director, cast, country, date_added, release_year,
# rating, duration, duration_type, listed_in, description """

class Movie:
    def get_movie(self):
        """
        возвращает всю базу данных
        :return: список
        """
        with sqlite3.connect(DATA_PATH) as connection:
            cursor = connection.cursor()
            query = """
                        SELECT *
                        FROM netflix
                    """
            cursor.execute(query)
            results = cursor.fetchall()
            return results

    def compreh_key_values(self, valus):
        """
        Делает словарь где ключ это колумнс в датабазе
        а валюес то, что возвращает гетмуви
        :param valus: список
        :return: словарь
        """
        keys = ["show_id", "type",  "title", "director", "cast", "country", "date_added",
                "release_year", "rating", "duration", "duration_type", "listed_in", "description"
                ]
        result = []

        for i in range(len(valus)):
            res = {}
            result.append(res)
            for j in range(len(keys)):
                res.setdefault(keys[j], valus[i][j])
        return result


    def movie_from_title(self, title) -> str:
        temp = self.compreh_key_values(self.get_movie())
        for i in range(len(temp)):
            if title in temp[i]["title"]:
                return temp[i]





tes = Movie()
# print(tes.get_movie())
# print(tes.compreh_key_values(tes.get_movie()))
print(tes.movie_from_title('Tallulah'))

