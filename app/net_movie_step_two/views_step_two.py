from flask import Blueprint, render_template

from app.net_movie_step_two.dao_step_two.netflix_movie_dao_step_two import MovieStepTwo

blueprint_movie_step_two = Blueprint('blueprint_movie_step_two', __name__, template_folder='templates')

@blueprint_movie_step_two.route('/genre/<genre>')
def page_movies_from_genre(genre):
    """выводим фильмы по жанру"""
    exemp_move = MovieStepTwo().get_movie_from_genre(genre)
    return render_template('page_movies_from_genre.html', exemp_move=exemp_move)