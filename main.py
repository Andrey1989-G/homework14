from flask import Flask, request, render_template

from app.net_movie.views import blueprint_movie
from app.net_movie_step_two.views_step_two import blueprint_movie_step_two

app = Flask(__name__)

app.register_blueprint(blueprint_movie)

app.register_blueprint(blueprint_movie_step_two)

@app.route('/')
def start_page():
    return render_template('index.html')

@app.errorhandler(404)
def page_not_found(e):
    return render_template('page404.html'), 404

@app.errorhandler(500)
def page_enternal(e):
    return render_template('page500.html'), 500


if __name__ == "__main__":
    app.run(debug=True)
