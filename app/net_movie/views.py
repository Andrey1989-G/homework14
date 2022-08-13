from flask import Blueprint, render_template

from utils import split_years_min, split_years_max

from app.net_movie.dao.netflix_movie_dao import Movie

blueprint_movie = Blueprint('blueprint_movie', __name__, template_folder='templates')


@blueprint_movie.route("/movie/<title>")
def page_movies_from_title(title):
    """выводим фильм по названию"""
    exemp_movie = Movie().movie_from_title(title)
    return render_template('page_from_title.html', exemp_movie=exemp_movie)

@blueprint_movie.route('/movie/year/to/year/<years>')
def page_movies_year_to_year(years):
    """выводим 100 фильмов по годам"""
    year_min = split_years_min(years)
    year_max = split_years_max(years)
    exemp_movie = Movie().movies_year_to_year(year_min, year_max)
    return render_template('page_year_to_year.html', exemp_movie=exemp_movie)

@blueprint_movie.route('/rating/children')
def page_rating_children():
    """выводим фильмs с рейтингом G"""
    exemp_movie = Movie().rating_children()
    return render_template('page_rating_children.html', exemp_movie=exemp_movie)

@blueprint_movie.route('/rating/family')
def page_rating_family():
    """выводим фильмs с рейтингом G, PG, PG-13"""
    exemp_mov = Movie().rating_family()
    return render_template('page_rating_family.html', exemp_mov=exemp_mov)

@blueprint_movie.route('/rating/adult')
def page_rating_adult():
    """выводим фильмs с рейтингом R, NC-17"""
    exemp_move = Movie().rating_adult()
    return render_template('page_rating_adult.html', exemp_move=exemp_move)



