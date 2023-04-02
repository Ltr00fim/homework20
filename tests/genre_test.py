from unittest.mock import MagicMock
import pytest
from dao.genre import GenreDAO
from dao.model.genre import Genre
from service.genre import GenreService


@pytest.fixture()
def genre_dao():
    genre_dao = GenreDAO(None)
    genre1 = Genre(id=1, name='genre1')
    genre2 = Genre(id=2, name='genre2')
    genre3 = Genre(id=3, name='genre3')
    genre_dao.get_one = MagicMock(return_value=genre1)
    genre_dao.get_all = MagicMock(return_value=[genre1, genre2, genre3])
    genre_dao.delete = MagicMock(return_value='')
    genre_dao.create = MagicMock(return_value='')
    genre_dao.update = MagicMock(return_value='')
    return genre_dao


class TestGenreService:

    @pytest.fixture()
    def genre_service(self, genre_dao):
        director_service = GenreService(dao=genre_dao)
        return director_service

    def test_get_one(self, genre_service):
        genr = genre_service.get_one(1)
        assert genr.name == 'genre1'

    def test_get_all(self, genre_service):
        genr = genre_service.get_all()[1]
        assert genr.name == 'genre2'

    def test_delete(self, genre_service):
        genr = genre_service.delete(7)
        assert genr is None

    def test_update(self, genre_service):
        genr = genre_service.update(4)
        assert genr is not None

    def test_create(self, genre_service):
        genr = genre_service.create(8)
        assert genr is not None
