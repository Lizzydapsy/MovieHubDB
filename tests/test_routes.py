import pytest
from app import create_app
from app.models import db, Movie

@pytest.fixture
def app():
    app = create_app()
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://localhost/moviedb_test'
    yield app

@pytest.fixture
def client(app):
    return app.test_client()

@pytest.fixture
def init_db():
    db.create_all()
    movie1 = Movie(title="Movie 1", genre="Action", release_year=2022, rating=8.5)
    movie2 = Movie(title="Movie 2", genre="Comedy", release_year=2021, rating=7.0)
    db.session.add(movie1)
    db.session.add(movie2)
    db.session.commit()

    yield db

    db.drop_all()

def test_get_movies(client, init_db):
    response = client.get('/movies')
    assert response.status_code == 200
    assert len(response.json) == 2
