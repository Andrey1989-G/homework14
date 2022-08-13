import sqlite3, json

from flask import jsonify

from app.config import DATA_DIR
from app.net_movie.dao.netflix_movie_dao import Movie

DATA_PATH = DATA_DIR.joinpath("netflix.db")


class MovieStepTwo:
    """
    для работы с БД на уровне запросов к БД
    """
    def get_movie_from_genre(self, genre):
        """
        возвращает базу данных по жанрам
        :param genre:
        :return:
        """
        #Comedies
        #строчка ниже шоб дыссонанса небыло
        genre = genre[1:]
        with sqlite3.connect(DATA_PATH) as connection:
            cursor = connection.cursor()
            query = f"""
                        SELECT *
                        FROM netflix
                        WHERE listed_in LIKE '%{genre}%'
                        ORDER BY release_year DESC
                        LIMIT 100
                    """
            cursor.execute(query)
            res = cursor.fetchall()
            #переводим в словарь
            exemp = Movie()
            results = exemp.compreh_key_values(res)
            return results

    def solution_step_five(self, name_one, name_two):
        """
        получает в качестве аргумента имена двух актеров,
        сохраняет всех актеров из колонки cast и
        возвращает список тех, кто играет с ними в
        паре больше 2 раз
        план:
        составляем два словаря и пробум через множества
        перебираем результат, и добавляем в множество всех актеров
        :param name_one: str
        :param name_two: str
        :return: list
        """
        with sqlite3.connect(DATA_PATH) as connection:
            cursor = connection.cursor()
            query = f"""
                        SELECT "cast"
                        FROM netflix
                        WHERE "cast" LIKE '%{name_one}%'
                        AND "cast" LIKE '%{name_two}%'
                        
                    """
            cursor.execute(query)
            res = cursor.fetchall()
            #уважаемый наставник! похоже, что дальше идет говнокод)))
            #почему-то я запарился почти на час, и моральных сил причесать
            #это уже не осталось(но я вижу что можно генератором сделать
            # в одну строку(или в две)).
            # 미안해~~~~
            #
            #получаем всех актеров
            s1 = []
            for i in range(len(res)):
                for j in range(len(res[i])):
                    s1.append((res[i][j]).split(','))
            #тут причесывал в состоянии аффекта
            s2 = []
            for i in range(len(s1)):
                for j in range(len(s1[i])):
                    tep = (s1[i][j]).strip()
                    s2.append(tep)
            res = []
            #тут считал количество вхождений
            for i in s2:
                if s2.count(i) > 2:
                    res.append(i)
        return res

    def solution_step_six(self, type_movie, release_year, listed_in):
        """
        удет передавать тип картины (фильм или сериал), год выпуска и ее жанр и
        получать на выходе список названий картин с их описаниями в JSON
        :param type_movie:
        :param release_year:
        :param listed_in:
        :return:
        """
        #'Movie', 2020, 'Comedies'
        with sqlite3.connect(DATA_PATH) as connection:
            cursor = connection.cursor()
            query = f"""
                        SELECT *
                        FROM netflix
                        WHERE type LIKE '%{type_movie}%'
                        AND release_year LIKE '%{release_year}%'
                        AND listed_in LIKE '%{listed_in}%'

                    """
            cursor.execute(query)
            res = cursor.fetchall()

        exemp = Movie()
        results = exemp.compreh_key_values(res)
        corr_key = ['title', 'description']
        list_with_results = []
        for i in results:
            for key, value in i.items():
                if key in corr_key:
                    list_with_results.append(i.setdefault(key, value))


        return json.dumps(list_with_results)


exem = MovieStepTwo()

# name_one = 'Rose McIver'
# name_two = 'Ben Lamb'
#print(exem.solution_step_five(name_one, name_two))
#print(exem.solution_step_six('Movie', 2020, 'Comedies'))