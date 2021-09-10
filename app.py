import os
from flask import Flask, request, abort, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from models import setup_db, Movie, Actor, db
from auth import AuthError, requires_auth
from datetime import datetime
import sys

DATA_PER_PAGE = 10


def paginate_data(request, selection):
    page = request.args.get("page", 1, type=int)
    start = (page - 1) * DATA_PER_PAGE
    end = start + DATA_PER_PAGE

    formattedData = [data.format() for data in selection]
    current_data = formattedData[start:end]
    return current_data


def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__)
    setup_db(app)
    CORS(app)

    # CORS Headers
    @app.after_request
    def after_request(response):
        response.headers.add(
            "Access-Control-Allow-Headers", "Content-Type,Authorization,true"
        )
        response.headers.add(
            "Access-Control-Allow-Methods", "GET,PUT,POST,DELETE,OPTIONS"
        )
        return response

    # restricted endpoint, returns movies
    @app.route('/movies')
    @requires_auth('get:movies')
    def get_movies(payload):
        try:
            movies = Movie.query.order_by('id').all()
            current_movies = paginate_data(request, movies)
            if len(current_movies) == 0:
                abort(404)
            else:
                return jsonify(
                    {
                        "success": True,
                        "movies": current_movies,
                        "total_movies": len(movies),
                    }
                )
        except:
            # print("get movies:", sys.exc_info())
            abort(422)

    # restricted endpoint, returns movies
    @app.route('/movies/<int:movie_id>', methods=["DELETE"])
    @requires_auth('delete:movie')
    def delete_movies(payload, movie_id):
        try:
            movie = Movie.query.filter(Movie.id == movie_id).one_or_none()
            if movie is None:
                abort(404)
            movie.delete()
            movies = Movie.query.order_by('id').all()
            current_movies = paginate_data(request, movies)
            return jsonify(
                {
                    "success": True,
                    "deleted": movie_id,
                    "movies": current_movies,
                    "total_movies": len(movies),
                }
            )
        except:
            # print("delete movie:", sys.exc_info())
            abort(422)

    # restricted endpoint, updates a movies
    @app.route('/movies/<int:movie_id>', methods=["PATCH"])
    @requires_auth('patch:movie')
    def update_movies(payload, movie_id):
        body = request.get_json()
        newTitle = body.get("title", None)
        newReleaseDate = body.get("release_date", None)
        if newReleaseDate == "":
            newReleaseDate = None
        if (newTitle is None or newTitle == "") and (newReleaseDate is None):
                abort(400)

        try:
            movie = Movie.query.get_or_404(movie_id)
            if newTitle is not None or newTitle != "":
                movie.title = newTitle
            if newReleaseDate is not None:
                movie.release_date = \
                    datetime.strptime(newReleaseDate, '%Y-%m-%d %H:%M:%S')
            movie.update()
            return jsonify(
                {
                    "success": True,
                    "movie": movie.format(),
                }
            )
        except:
            # print("patch movie:", sys.exc_info())
            abort(422)

    # restricted endpoint, posts a movies
    @app.route('/movies', methods=["POST"])
    @requires_auth('post:movies')
    def insert_movie(payload):
        body = request.get_json()
        newTitle = body.get("title", None)
        newTitle = None if newTitle == "" else newTitle
        newReleaseDate = body.get("release_date", None)
        newReleaseDate = None if newReleaseDate == "" else newReleaseDate

        if newTitle is None or newReleaseDate is None:
            abort(400)

        try:
            movie = Movie(title=newTitle, release_date=newReleaseDate)
            movie.insert()
            return jsonify(
                {
                    "success": True,
                    "movie": movie.format(),
                }
            )
        except:
            # print("post movie:", sys.exc_info())
            abort(422)

    # restricted endpoint, returns movies
    @app.route('/actors')
    @requires_auth('get:actors')
    def get_actors(payload):
        try:
            actors = Actor.query.order_by('id').all()
            current_actors = paginate_data(request, actors)
            if len(current_actors) == 0:
                abort(404)
            else:
                return jsonify(
                    {
                        "success": True,
                        "actors": current_actors,
                        "total_actors": len(actors),
                    }
                )
        except:
            # print("get actors:", sys.exc_info())
            abort(422)

    # restricted endpoint, deletes an actor
    @app.route('/actors/<int:actor_id>', methods=["DELETE"])
    @requires_auth('delete:actor')
    def delete_actors(payload, actor_id):
        try:
            actor = Actor.query.filter(Actor.id == actor_id).one_or_none()
            if actor is None:
                abort(404)
            actor.delete()
            actors = Actor.query.order_by('id').all()
            current_actors = paginate_data(request, actors)
            return jsonify(
                {
                    "success": True,
                    "deleted": actor_id,
                    "actors": current_actors,
                    "total_actors": len(actors),
                }
            )
        except:
            # print("delete actor:",sys.exc_info())
            abort(422)

    # restricted endpoint, updates a actors
    @app.route('/actors/<int:actor_id>', methods=["PATCH"])
    @requires_auth('patch:actor')
    def update_actor(payload, actor_id):
        body = request.get_json()
        newName = body.get("name", None)
        newName = None if newName == "" else newName
        newAge = body.get("age", None)
        newAge = None if newAge == "" else newAge
        newGender = body.get("gender", None)
        newGender = None if newGender == "" else newGender
        print(body)
        if newName is None and newAge is None and newGender is None:
            abort(400)

        try:
            actor = Actor.query.get_or_404(actor_id)
            if newName is not None:
                actor.name = newName
            if newAge is not None:
                actor.age = newAge
            if newGender is not None:
                actor.gender = newGender
            actor.update()
            return jsonify(
                {
                    "success": True,
                    "actor": actor.format(),
                }
            )
        except:
            # print("patch actor:", sys.exc_info())
            abort(422)

    # restricted endpoint, posts a actors
    @app.route('/actors', methods=["POST"])
    @requires_auth('post:actors')
    def insert_actor(payload):
        body = request.get_json()
        newName = body.get("name", None)
        newName = None if newName == "" else newName
        newAge = body.get("age", None)
        newAge = None if newAge == "" else newAge
        newGender = body.get("gender", None)
        newGender = None if newGender == "" else newGender

        if newName is None or newAge is None or newGender is None:
            abort(400)

        try:
            actor = Actor(name=newName, age=newAge, gender=newGender)
            actor.insert()
            return jsonify(
                {
                    "success": True,
                    "actor": actor.format(),
                }
            )
        except:
            # print("post actor:", sys.exc_info())
            abort(422)

    # error handlers
    @app.errorhandler(400)
    def bad_request(err):
        return jsonify({
            "success": False,
            "error": 400,
            "message": "bad request"
        }), 400

    @app.errorhandler(AuthError)
    def auth_error(ex):
        response = jsonify({
            "success": False,
            "error": ex.status_code,
            "message": ex.error['description']
        })
        response.status_code = ex.status_code
        return response

    @app.errorhandler(401)
    def unauthorized(err):
        return jsonify({
            "success": False,
            "error": 401,
            "message": "unauthorized"
        }), 401

    @app.errorhandler(404)
    def not_found(err):
        return jsonify({
            "success": False,
            "error": 404,
            "message": "resource not Found"
        }), 404

    @app.errorhandler(405)
    def not_allowed(err):
        return jsonify({
            "success": False,
            "error": 405,
            "message": "method not allowed"
        }), 405

    @app.errorhandler(422)
    def unprocessable(err):
        return jsonify({
            "success": False,
            "error": 422,
            "message": "unprocessable"
        }), 422

    return app

app = create_app()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)
