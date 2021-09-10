# Udacity FSD capstone project

## Casting Agency API

Come sit on my couch said the spider to the fly. A casting agency is in need of a back end to their system.  This project attemps to full fill those needs.  It models the actors and movies managed by the agency in a postgresql database.  There are api end points so that users with the correct permissions can view, add, delete or update both actors and movies. 


### Installing Dependencies for the Backend

1. **Python 3.7** - Follow instructions to install the latest version of python for your platform in the [python docs](https://docs.python.org/3/using/unix.html#getting-and-installing-the-latest-version-of-python)


2. **Virtual Enviornment** - We recommend working within a virtual environment whenever using Python for projects. This keeps your dependencies for each project separate and organaized. Instructions for setting up a virual enviornment for your platform can be found in the [python docs](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/)


3. **PIP Dependencies** - Once you have your virtual environment setup and running, install dependencies by naviging to the `/backend` directory and running:
```bash
pip install -r requirements.txt
```
This will install all of the required packages we selected within the `requirements.txt` file.


4. **Key Dependencies**
 - [Flask](http://flask.pocoo.org/)  is a lightweight backend microservices framework. Flask is required to handle requests and responses.

 - [SQLAlchemy](https://www.sqlalchemy.org/) is the Python SQL toolkit and ORM we'll use handle the lightweight sqlite database. You'll primarily work in app.py and can reference models.py. 


### Database Setup
With Postgres running, restore a database using the cast_agency.sql file provided. From the backend folder in terminal run:
```bash
psql cast_agency < cast_agency.psql
```

### Running the server

From within the `./src` directory first ensure you are working using your created virtual environment.

To run the server, execute:

```bash
flask run --reload
```

The `--reload` flag will detect file changes and restart the server automatically.

## Permissions
There are three roles with different permissions in the app.  They are:
 - assistant: can view actors and movies
 - director: can view and update actors and movies.  Can also add and delete actors
 - producer: all directors permissions plus can add and delete movies

## API Reference
Errors are returned in a json format.  They are in this format:
```
    {
        "success": False,
        "error": 404,
        "message": "resource not Found"
    }
```

The API has the following error codes:
- 400: bad request
- 401: invalid_header
- 403: unauthorized
- 404: resource not found
- 405: method not allowed
- 422: unprocessable

## Endpoint Library
### GET /movies
- General: 
    - Request Arguments: page (optional- integer)
    - Authorization: accessable by any assistant, director or producer
    - Returns a list of the movies, the total number of movies and a success value.
    - Results are paginated in groups of 10. Include a request argument to choose page number, starting from 1.
    - Sample: `curl http://127.0.0.1:5000/movies?page=1`
```
{
  "movies": [
    {
      "id": 1,
      "release_date": "Tue, 08 May 1990 00:00:00 GMT",
      "title": "Driving Miss Daisy"
    },
    {
      "id": 2,
      "release_date": "Fri, 20 May 1988 00:00:00 GMT",
      "title": "Willow"
    },
    {
      "id": 3,
      "release_date": "Fri, 28 Nov 1986 00:00:00 GMT",
      "title": "Labyrinth"
    },
    {
      "id": 4,
      "release_date": "Fri, 06 Dec 1985 00:00:00 GMT",
      "title": "The Goonies"
    },
    {
      "id": 5,
      "release_date": "Fri, 20 Dec 1985 00:00:00 GMT",
      "title": "Back to the Future"
    },
    {
      "id": 6,
      "release_date": "Fri, 09 Oct 1987 00:00:00 GMT",
      "title": "The Princess Bride"
    },
    {
      "id": 7,
      "release_date": "Fri, 13 Dec 1985 00:00:00 GMT",
      "title": "Legend"
    },
    {
      "id": 8,
      "release_date": "Sat, 06 Apr 1985 00:00:00 GMT",
      "title": "The Never Ending Story"
    },
    {
      "id": 9,
      "release_date": "Fri, 17 Dec 1982 00:00:00 GMT",
      "title": "The Dark Crystal"
    },
    {
      "id": 10,
      "release_date": "Fri, 21 Jun 1985 00:00:00 GMT",
      "title": "Cocoon"
    }
  ],
  "success": true,
  "total_movies": 11
}
```


### DELETE /movies
- General: 
    - Request Arguments: movie_id (int), page (optional- integer)
    - Authorization: accessable by any producer
    - Deletes the movie of the given ID if it exists. Returns the id of the deleted movie, success value, a list of the remaining movies, the total number of movies.
    - If no movie is deleted a 404 error is returned
    - Sample: `curl -X DELETE http://127.0.0.1:5000/movies/8`
```
{
    "deleted": 8,
    "movies": [
        {
            "id": 1,
            "release_date": "Tue, 08 May 1990 00:00:00 GMT",
            "title": "Driving Miss Daisy"
        },
        {
            "id": 2,
            "release_date": "Fri, 20 May 1988 00:00:00 GMT",
            "title": "Willow"
        },
        {
            "id": 3,
            "release_date": "Fri, 28 Nov 1986 00:00:00 GMT",
            "title": "Labyrinth"
        },
        {
            "id": 4,
            "release_date": "Fri, 06 Dec 1985 00:00:00 GMT",
            "title": "The Goonies"
        },
        {
            "id": 5,
            "release_date": "Fri, 20 Dec 1985 00:00:00 GMT",
            "title": "Back to the Future"
        },
        {
            "id": 6,
            "release_date": "Fri, 09 Oct 1987 00:00:00 GMT",
            "title": "The Princess Bride"
        },
        {
            "id": 7,
            "release_date": "Fri, 13 Dec 1985 00:00:00 GMT",
            "title": "Legend"
        },
        {
            "id": 9,
            "release_date": "Fri, 17 Dec 1982 00:00:00 GMT",
            "title": "The Dark Crystal"
        },
        {
            "id": 10,
            "release_date": "Fri, 21 Jun 1985 00:00:00 GMT",
            "title": "Cocoon"
        },
        {
            "id": 11,
            "release_date": "Fri, 08 Jun 1984 00:00:00 GMT",
            "title": "Gremlins"
        }
    ],
    "success": true,
    "total_movies": 10
}
```


### Patch /movie
- General: 
    - Request Arguments: movie_id (int)
    - Body Arguments: title (string), release_date (date time format object)
    - Authorization: accessable by any director or producer
    - Update the movie of the given ID if it exists. Some or all of the fields can be updated. You must supply at least one body arugument. Returns the new details of the movie and a success value.
    - If no movie is updated a 404 error is returned
    - Sample: `curl http://127.0.0.1:5000/actors/8 -X PATCH  -H "content-Type: application/json" -d '{"title": 'A New Movie', "release_date": "Fri, 13 Dec 1985 00:00:00 GMT"}'`
```
{
    'movie': 
    {
        'id': 8, 
        'release_date': 'Fri, 13 Dec 1985 00:00:00 GMT', 
        'title': 'A New Movie'
    }, 
    'success': True
}
```

### Post /movie
- General: 
    - Body Arguments: title (string), release_date (date time format object)
    - Authorization: accessable by producer
    - Add a movie to the database. All of the body fields must be supplied. Returns the new details of the new movie and a success value.
    - If no movie is updated a 404 error is returned
    - Sample: `curl http://127.0.0.1:5000/actors -X PATCH  -H "content-Type: application/json" -d '{"title": 'A New Movie', "release_date": "Fri, 13 Dec 1985 00:00:00 GMT"}'`
```
{
    'movie': 
    {
        'id': 7, 
        'release_date': 'Fri, 13 Dec 1985 00:00:00 GMT', 
        'title': 'A New Movie'
    }, 
    'success': True
}
```

### GET /actors
- General: 
    - Request Arguments: page (optional- integer)
    - Authorization: accessable by any assistant, director or producer
    - Returns a list of the actors, the total number of actors and a success value.
    - Results are paginated in groups of 10. Include a request argument to choose page number, starting from 1.
    - Sample: `curl http://127.0.0.1:5000/actors?page=1`
```
{
    "actors": [
        {
            "age": 62,
            "gender": "F",
            "id": 1,
            "name": "Jamie Lee Curtis"
        },
        {
            "age": 53,
            "gender": "M",
            "id": 2,
            "name": "Vin Diesel"
        },
        {
            "age": 53,
            "gender": "M",
            "id": 3,
            "name": "Will ferrell"
        },
        {
            "age": 51,
            "gender": "F",
            "id": 4,
            "name": "Cate Blanchett"
        },
        {
            "age": 54,
            "gender": "F",
            "id": 5,
            "name": "Halle Berry"
        },
        {
            "age": 40,
            "gender": "M",
            "id": 6,
            "name": "Ryan Gosling"
        },
        {
            "age": 30,
            "gender": "M",
            "id": 7,
            "name": "Thomas Brodie-Sangster"
        },
        {
            "age": 65,
            "gender": "F",
            "id": 8,
            "name": "Whoopi Goldberg"
        },
        {
            "age": 47,
            "gender": "M",
            "id": 9,
            "name": "Jim Parsons"
        },
        {
            "age": 35,
            "gender": "F",
            "id": 10,
            "name": "Kiera Knightly"
        }
    ],
    "success": true,
    "total_actors": 11
}
```


### DELETE /actors
- General: 
    - Request Arguments: actor_id (int)
    - Authorization: accessable by any director or producer
    - Deletes the actor of the given ID if it exists. Returns the id of the deleted actor, success value, a list of the remaining actors, the total number of actors.
    - If no actor is deleted a 404 error is returned
    - Sample: `curl -X DELETE http://127.0.0.1:5000/actors/8`
```
{
    'actors': [
        {
            'age': 62, 
            'gender': 'F', 
            'id': 1, 
            'name': 'Jamie Lee Curtis'
        }, 
        {
            'age': 53, 
            'gender': 'M', 
            'id': 2, 
            'name': 'Vin Diesel'
        }, 
        {
            'age': 53, 
            'gender': 'M', 
            'id': 3, 
            'name': 'Will ferrell'
        }, 
        {
            'age': 51, 
            'gender': 'F', 
            'id': 4, 
            'name': 'Cate Blanchett'
        }, 
        {
            'age': 40, 
            'gender': 'M', 
            'id': 6, 
            'name': 'Ryan Gosling'
        }, 
        {
            'age': 30, 
            'gender': 'M', 
            'id': 7, 
            'name': 'Thomas Brodie-Sangster'
        }, 
        {
            'age': 65, 
            'gender': 'F', 
            'id': 8, 
            'name': 'Whoopi Goldberg'
        }, 
        {
            'age': 47, 
            'gender': 'M', 
            'id': 9, 'name': 
            'Jim Parsons'
        }, 
        {
            'age': 35, 
            'gender': 'F', 
            'id': 10, 'name': 
            'Kiera Knightly'
        }, 
        {
            'age': 48, 
            'gender': 'M', 
            'id': 11, 'name': 
            'dwayne Johnson'
        }
    ], 
    'deleted': 5, 
    'success': True, 
    'total_actors': 10
}
```


### Patch /actor
- General: 
    - Request Arguments: actor_id (int), page (optional- integer)
    - Body Arguments: name (string), age (int), gender (string)
    - Authorization: accessable by any director or producer
    - Update the actor of the given ID if it exists. Some or all of the fields can be updated. You must supply at least one body arugument. Returns the new details of the actor and a success value.
    - If no actor is updated a 404 error is returned
    - Sample: `curl http://127.0.0.1:5000/actors/8 -X PATCH  -H "content-Type: application/json" -d '{"name": 'John Doe', "age": "52", "gender": "M"}'`
```
{
    'actor': 
    {
        'age': 52, 
        'gender': 'M', 
        'id': 8, 
        'name': 'John Doe'
    }, 
    'success': True
}
```


### Post /actor
- General: 
    - Request Arguments: none
    - Body Arguments: name (string), age (int), gender (string)
    - Authorization: accessable by any director or producer
    - add an actor to the database. All of the body fields must be supplied. Returns the details of the new actor and a success value.
    - Sample: `curl http://127.0.0.1:5000/actors/8 -X POST  -H "content-Type: application/json" -d '{"name": 'John Doe', "age": "52", "gender": "M"}'`
```
{
    'actor': 
    {
        'age': 52, 
        'gender': 'M', 
        'id': 8, 
        'name': 'John Doe'
    }, 
    'success': True
}
```

To run the tests, run
```
dropdb castin_agent_test
createdb castin_agent_test
psql castin_agent_test < castin_agent.psql
python -m unittest test_app.py
```


## Testing
To run the tests, run
```
dropdb casting_agency_test
createdb casting_agency_test
psql casting_agency_test < casting_agency.sql
python -m unittest test_app.py
```

## Deployment 
The server is deployed on Heroku

## Authors
Velda Conaty

## Acknowledgements 
The awesome team at Udacity for designing the assignement.