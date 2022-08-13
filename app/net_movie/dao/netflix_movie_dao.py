import sqlite3, json

from flask import jsonify

from app.config import DATA_DIR

DATA_PATH = DATA_DIR.joinpath("netflix.db")
# колумнс в базе данных show_id, type,  title, director, cast, country, date_added, release_year,
# rating, duration, duration_type, listed_in, description """

class Movie:
    """
    для работы с БД на уровне функций и классов
    """
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


    def movie_from_title(self, titl) -> str:
        """
        поиск фильма по названию
        :param title:
        :return:
        """

        # temp = self.compreh_key_values(self.get_movie())
        # for i in range(len(temp)):
        #     if title in temp[i]["title"]:
        #         return temp[i]
        with sqlite3.connect(DATA_PATH) as connection:
            cursor = connection.cursor()
            query = f"""
                        SELECT *
                        FROM netflix
                        WHERE "title" LIKE '%{titl}%'
                    """
            cursor.execute(query)
            res = cursor.fetchall()
            result = self.compreh_key_values(res)
            return result

    def movies_year_to_year(self, year_min=int, year_max=int):
        """
        принимает два года, выводит 100 фильмов
        :param year_min:
        :param year_max:
        :return:
        """
        # temp = self.compreh_key_values(self.get_movie())
        # result = []
        # while len(result) <= 100:
        #     for i in range(len(temp)):
        #         if temp[i]["release_year"] == year_max or temp[i]["release_year"] == year_min:
        #             result.append(temp[i])
        with sqlite3.connect(DATA_PATH) as connection:
            cursor = connection.cursor()
            query = f"""
                        SELECT *
                        FROM netflix
                        WHERE release_year BETWEEN '{year_min}' AND '{year_max}'
                        
                    """
            cursor.execute(query)
            res = cursor.fetchall()
            result = self.compreh_key_values(res)
        return result

    def rating_children(self):
        """
        выводит ретинг G
        :return:
        """
        # temp = self.compreh_key_values(self.get_movie())
        # result = []
        # for i in range(len(temp)):
        #     if temp[i]["rating"] == 'G':
        #         result.append(temp[i])
        with sqlite3.connect(DATA_PATH) as connection:
            cursor = connection.cursor()
            query = f"""
                        SELECT *
                        FROM netflix
                        WHERE rating LIKE 'G'
                    """
            cursor.execute(query)
            res = cursor.fetchall()
            result = self.compreh_key_values(res)
        return result

    def rating_family(self):
        """
        выводит ретинг G, PG, PG-13
        :return:
        """
        # rating_family = ['G', 'PG', 'PG-13']
        # temp = self.compreh_key_values(self.get_movie())
        # result = []
        # for i in range(len(temp)):
        #     if temp[i]["rating"] in rating_family:
        #         result.append(temp[i])
        with sqlite3.connect(DATA_PATH) as connection:
            cursor = connection.cursor()
            query = f"""
                        SELECT *
                        FROM netflix
                        WHERE rating LIKE 'G'
                        OR rating LIKE 'PG'
                        OR rating LIKE 'PG-13'
                    """
            cursor.execute(query)
            res = cursor.fetchall()
            result = self.compreh_key_values(res)
        return result

    def rating_adult(self):
        """
        выводит ретинг R, NC-17
        :return:
        """
        # rating_adult = ['R', 'NC-17']
        # temp = self.compreh_key_values(self.get_movie())
        # result = []
        # for i in range(len(temp)):
        #     if temp[i]["rating"] in rating_adult:
        #         result.append(temp[i])
        with sqlite3.connect(DATA_PATH) as connection:
            cursor = connection.cursor()
            query = f"""
                        SELECT *
                        FROM netflix
                        WHERE rating LIKE 'R'
                        OR rating LIKE 'NC-17'
                    """
            cursor.execute(query)
            res = cursor.fetchall()
            result = self.compreh_key_values(res)
        return result

    def movies_from_genre(self, genre):
        temp = self.compreh_key_values(self.get_movie())



#tes = Movie()
#print(tes.get_movie())
# print(tes.compreh_key_values(tes.get_movie()))
#print(tes.movie_from_title('Tallulah'))
#print(tes.movies_year_to_year(2020, 2021))
# print(tes.rating_family())

