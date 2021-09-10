'''
Tests for casting agency flask app.
'''
import os
import unittest
import json
from flask_sqlalchemy import SQLAlchemy

from app import create_app
from models import setup_db, Movie, Actor
from dotenv import load_dotenv
from datetime import datetime

load_dotenv()


class CastingAgentTestCase(unittest.TestCase):
    def repopulateData(self):
        Movie.query.delete()
        Actor.query.delete()
        movie1 = Movie(
            title='Driving Miss Daisy',
            release_date=datetime.strptime('1988/05/20', '%Y/%m/%d'))
        movie1.id = 1
        movie2 = Movie(
            title='Willow',
            release_date=datetime.strptime('1985/12/06', '%Y/%m/%d'))
        movie2.id = 2
        movie3 = Movie(
            title='Labyrinth',
            release_date=datetime.strptime('1987/10/09', '%Y/%m/%d'))
        movie3.id = 3
        movie4 = Movie(
            title='The Goonies',
            release_date=datetime.strptime('1985/04/06', '%Y/%m/%d'))
        movie4.id = 4
        movie5 = Movie(
            title='Back to the Future',
            release_date=datetime.strptime('1986/11/28', '%Y/%m/%d'))
        movie5.id = 5
        movie6 = Movie(
            title='The Princess Bride',
            release_date=datetime.strptime('1985/12/20', '%Y/%m/%d'))
        movie6.id = 6
        movie7 = Movie(
            title='Legend',
            release_date=datetime.strptime('1982/12/17', '%Y/%m/%d'))
        movie7.id = 7
        movie8 = Movie(
            title='The Never Ending Story',
            release_date=datetime.strptime('1985/12/13', '%Y/%m/%d'))
        movie8.id = 8
        movie9 = Movie(
            title='The Dark Crystal',
            release_date=datetime.strptime('1990/05/08', '%Y/%m/%d'))
        movie9.id = 9
        movie10 = Movie(
            title='Cocoon',
            release_date=datetime.strptime('1984/06/08', '%Y/%m/%d'))
        movie10.id = 10
        movie11 = Movie(
            title='Gremlins',
            release_date=datetime.strptime('1985/06/21', '%Y/%m/%d'))
        movie11.id = 11

        actor1 = Actor(name='Vin Diesel', age=53, gender='M')
        actor1.id = 1
        actor2 = Actor(name='Cate Blanchett', age=51, gender='F')
        actor2.id = 2
        actor3 = Actor(name='Ryan Gosling', age=40, gender='M')
        actor3.id = 3
        actor4 = Actor(name='Whoopi Goldberg', age=65, gender='F')
        actor4.id = 4
        actor5 = Actor(name='Will ferrell', age=53, gender='M')
        actor5.id = 5
        actor6 = Actor(name='Halle Berry', age=54, gender='F')
        actor6.id = 6
        actor7 = Actor(name='Jim Parsons', age=47, gender='M')
        actor7.id = 7
        actor8 = Actor(name='Thomas Brodie-Sangster', age=30, gender='M')
        actor8.id = 8
        actor9 = Actor(name='Jamie Lee Curtis', age=62, gender='F')
        actor9.id = 9
        actor10 = Actor(name='dwayne Johnson', age=48, gender='M')
        actor10.id = 10
        actor11 = Actor(name='Kiera Knightly', age=35, gender='F')
        actor11.id = 11

        actor1.insert()
        actor2.insert()
        actor3.insert()
        actor4.insert()
        actor5.insert()
        actor6.insert()
        actor7.insert()
        actor8.insert()
        actor9.insert()
        actor10.insert()
        actor11.insert()
        movie1.insert()
        movie2.insert()
        movie3.insert()
        movie4.insert()
        movie5.insert()
        movie6.insert()
        movie7.insert()
        movie8.insert()
        movie9.insert()
        movie10.insert()
        movie11.insert()

    def setUp(self):
        """Define test variables and initialize app."""
        self.app = create_app()
        self.client = self.app.test_client

        self.database_name = os.environ.get('DB_TEST_NAME')
        self.database_path = os.environ.get('DB_PATH_TEST')
        setup_db(self.app, self.database_path)

        # binds the app to the current context
        with self.app.app_context():
            self.db = SQLAlchemy()
            self.db.init_app(self.app)
            # create all tables
            self.db.create_all()

        # Headers for different roles
        self.assistant_header = {
            "Authorization": "Bearer {}"
            .format(os.environ.get('ASSISTANT_TOKEN'))
            }
        self.director_header = {
            "Authorization": "Bearer {}"
            .format(os.environ.get('DIRECTOR_TOKEN'))
            }
        self.producer_header = {
            "Authorization": "Bearer {}"
            .format(os.environ.get('PRODUCER_TOKEN'))
            }

        self.repopulateData()
        self.updateActorName = {"name": 'Bob Marley'}
        self.fullActor = {"name": 'John Lennon', "age": '49',  "gender": 'M'}
        self.updatemovieTitle = {"title": 'Dune'}
        self.fullMovie = {
            "title": 'Top Gun',
            "release_date": '1986-08-11 00:00:00'}

    def tearDown(self):
        """Executed after each test"""
        # Movie.query.delete()
        # Actor.query.delete()
        pass

    def test_404_when_url(self):
        res = self.client().get('/invalid/url')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], "resource not Found")

        ######################################
        #              no headers            #
        ######################################
    def test_401_unauthorised_get_movies(self):
        res = self.client().get('/movies')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 401)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], "Authorization header is expected.")

    def test_401_unauthorised_get_actors(self):
        res = self.client().get('/actors')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 401)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], "Authorization header is expected.")

    def test_401_unauthorised_delete_movies(self):
        res = self.client().delete('/movies/3')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 401)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], "Authorization header is expected.")

    def test_401_unauthorised_delete_actors(self):
        res = self.client().delete('/actors/3')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 401)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], "Authorization header is expected.")

    def test_401_unauthorised_patch_movies(self):
        res = self.client().patch('/movies/3', json=self.fullMovie)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 401)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], "Authorization header is expected.")

    def test_401_unauthorised_patch_actors(self):
        res = self.client().patch('/actors/3', json=self.fullActor)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 401)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], "Authorization header is expected.")

    def test_401_unauthorised_post_actors(self):
        res = self.client().post('/actors', json=self.fullActor)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 401)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], "Authorization header is expected.")

    def test_401_unauthorised_post_movies(self):
        res = self.client().post('/movies', json=self.fullMovie)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 401)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], "Authorization header is expected.")

        ######################################
        #               assistant            #
        ######################################
    def test_assistant_get_movies(self):
        res = self.client().get('/movies', headers=self.assistant_header)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['movies'])
        self.assertGreater(data['total_movies'], 4)

    def test_assistant_get_actors(self):
        res = self.client().get('/actors', headers=self.assistant_header)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['actors'])
        self.assertGreater(data['total_actors'], 4)

    def test_403_assistant_delete_movies(self):
        res = self.client().delete('/movies/4', headers=self.assistant_header)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 403)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], "Permission not found.")

    def test_403_assistant_delete_actors(self):
        res = self.client().delete('/actors/4', headers=self.assistant_header)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 403)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], "Permission not found.")

    def test_403_assistant_patch_movies(self):
        res = self.client().patch(
            '/movies/3',
            headers=self.assistant_header,
            json=self.fullMovie)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 403)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], "Permission not found.")

    def test_403_assistant_patch_actors(self):
        res = self.client().patch(
            '/actors/3',
            headers=self.assistant_header,
            json=self.fullActor)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 403)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], "Permission not found.")

    def test_403_assistant_post_actors(self):
        res = self.client().post(
            '/actors',
            headers=self.assistant_header,
            json=self.fullActor)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 403)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], "Permission not found.")

    def test_403_assistant_post_movies(self):
        res = self.client().post(
            '/movies',
            headers=self.assistant_header,
            json=self.fullMovie)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 403)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], "Permission not found.")

        ######################################
        #               director             #
        ######################################
    def test_director_get_movies(self):
        res = self.client().get('/movies', headers=self.director_header)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['movies'])
        self.assertGreater(data['total_movies'], 4)

    def test_director_get_actors(self):
        res = self.client().get('/actors', headers=self.director_header)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['actors'])
        self.assertGreater(data['total_actors'], 4)

    def test_403_director_delete_movie(self):
        res = self.client().delete('/movies/5', headers=self.director_header)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 403)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], "Permission not found.")

    def test_director_delete_actor(self):
        res = self.client().delete('/actors/5', headers=self.director_header)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertEqual(data['deleted'], 5)
        self.assertTrue(data['actors'])
        self.assertGreater(data['total_actors'], 4)

    def test_director_patch_movie_title(self):
        res = self.client().patch(
            '/movies/7',
            headers=self.director_header,
            json=self.updatemovieTitle)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertEqual(
            data['movie']['title'],
            self.updatemovieTitle['title'])

    def test_director_patch_movie(self):
        res = self.client().patch(
            '/movies/8',
            headers=self.director_header,
            json=self.fullMovie)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertEqual(data['movie']['title'], self.fullMovie['title'])
        self.assertEqual(
            data['movie']['release_date'],
            'Mon, 11 Aug 1986 00:00:00 GMT')

    def test_422_director_patch_unknown_movie(self):
        res = self.client().patch(
            '/movies/189',
            headers=self.director_header,
            json=self.fullMovie)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 422)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], "unprocessable")

    def test_director_patch_actor_name(self):
        res = self.client().patch(
            '/actors/7',
            headers=self.director_header,
            json=self.updateActorName)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertEqual(data['actor']['name'], self.updateActorName['name'])

    def test_director_patch_actor(self):
        res = self.client().patch(
            '/actors/8',
            headers=self.director_header,
            json=self.fullActor)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertEqual(data['actor']['name'], self.fullActor['name'])
        self.assertEqual(data['actor']['age'], int(self.fullActor['age']))
        self.assertEqual(data['actor']['gender'], self.fullActor['gender'])

    def test_422_director_patch_unknown_actor(self):
        res = self.client().patch(
            '/actors/189',
            headers=self.director_header,
            json=self.fullActor)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 422)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], "unprocessable")

    def test_403_director_post_movie(self):
        res = self.client().post(
            '/movies',
            headers=self.director_header,
            json=self.fullMovie)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 403)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], "Permission not found.")

    def test_director_post_actor(self):
        res = self.client().post(
            '/actors',
            headers=self.director_header,
            json=self.fullActor)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertEqual(data['actor']['name'], self.fullActor['name'])
        self.assertEqual(data['actor']['age'], int(self.fullActor['age']))
        self.assertEqual(data['actor']['gender'], self.fullActor['gender'])

    def test_400_director_post_actor_missing_details(self):
        res = self.client().post(
            '/actors',
            headers=self.director_header,
            json=self.updateActorName)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 400)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], "bad request")

        ######################################
        #               producer             #
        ######################################
    def test_producer_get_movies(self):
        res = self.client().get('/movies', headers=self.producer_header)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['movies'])
        self.assertGreater(data['total_movies'], 4)

    def test_producer_get_actors(self):
        res = self.client().get('/actors', headers=self.producer_header)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['actors'])
        self.assertGreater(data['total_actors'], 4)

    def test_producer_delete_movies(self):
        res = self.client().delete('/movies/6', headers=self.producer_header)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertEqual(data['deleted'], 6)
        self.assertTrue(data['movies'])
        self.assertGreater(data['total_movies'], 4)

    def test_422_producer_delete_movie_doesnt_exist(self):
        res = self.client().delete('/movies/527', headers=self.producer_header)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 422)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], "unprocessable")

    def test_producer_delete_actor(self):
        res = self.client().delete('/actors/6', headers=self.producer_header)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertEqual(data['deleted'], 6)
        self.assertTrue(data['actors'])
        self.assertGreater(data['total_actors'], 4)

    def test_422_producer_delete_actor_doesnt_exist(self):
        res = self.client().delete(
            '/actors/527',
            headers=self.producer_header)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 422)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], "unprocessable")

    def test_producer_patch_movie_name(self):
        res = self.client().patch(
            '/movies/9',
            headers=self.producer_header,
            json=self.updatemovieTitle)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertEqual(
            data['movie']['title'],
            self.updatemovieTitle['title'])

    def test_producer_patch_movie(self):
        res = self.client().patch(
            '/movies/10',
            headers=self.producer_header,
            json=self.fullMovie)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertEqual(data['movie']['title'], self.fullMovie['title'])
        self.assertEqual(
            data['movie']['release_date'],
            'Mon, 11 Aug 1986 00:00:00 GMT')

    def test_producer_patch_movie(self):
        res = self.client().patch(
            '/movies/159',
            headers=self.producer_header,
            json=self.fullMovie)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 422)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], "unprocessable")

    def test_producer_patch_actor_name(self):
        res = self.client().patch(
            '/actors/9',
            headers=self.producer_header,
            json=self.updateActorName)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertEqual(data['actor']['name'], self.updateActorName['name'])

    def test_producer_patch_actor(self):
        res = self.client().patch(
            '/actors/10',
            headers=self.producer_header,
            json=self.fullActor)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertEqual(data['actor']['name'], self.fullActor['name'])
        self.assertEqual(data['actor']['age'], int(self.fullActor['age']))
        self.assertEqual(data['actor']['gender'], self.fullActor['gender'])

    def test_422_producer_patch_unknown_actor(self):
        res = self.client().patch(
            '/actors/159',
            headers=self.producer_header,
            json=self.fullActor)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 422)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], "unprocessable")

    def test_producer_post_movie(self):
        res = self.client().post(
            '/movies',
            headers=self.producer_header,
            json=self.fullMovie)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertEqual(data['movie']['title'], self.fullMovie['title'])
        self.assertEqual(
            data['movie']['release_date'],
            'Mon, 11 Aug 1986 00:00:00 GMT')

    def test_400_producer_post_movie_missing_details(self):
        res = self.client().post(
            '/movies',
            headers=self.producer_header,
            json=self.updatemovieTitle)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 400)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], "bad request")

    def test_producer_post_actor(self):
        res = self.client().post(
            '/actors',
            headers=self.producer_header,
            json=self.fullActor)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertEqual(data['actor']['name'], self.fullActor['name'])
        self.assertEqual(data['actor']['age'], int(self.fullActor['age']))
        self.assertEqual(data['actor']['gender'], self.fullActor['gender'])

    def test_400_producer_post_actor_missing_details(self):
        res = self.client().post(
            '/actors',
            headers=self.producer_header,
            json=self.updateActorName)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 400)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], "bad request")
