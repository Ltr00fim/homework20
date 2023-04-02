from unittest.mock import MagicMock
import pytest
from dao.director import DirectorDAO
from dao.model.director import Director
from service.director import DirectorService


@pytest.fixture()
def director_dao():
    director_d = DirectorDAO(None)
    Pasha = Director(id=1, name='Pasha')
    Masha = Director(id=2, name='Masha')
    Sasha = Director(id=3, name='Sasha')
    director_d.get_one = MagicMock(return_value=Pasha)
    director_d.get_all = MagicMock(return_value=[Pasha, Masha, Sasha])
    director_d.delete = MagicMock(return_value='')
    director_d.create = MagicMock(return_value='')
    director_d.update = MagicMock(return_value='')
    return director_d


class TestDirectorService:

    @pytest.fixture()
    def director_service(self, director_dao):
        director_ser = DirectorService(dao=director_dao)
        return director_ser

    def test_get_one(self, director_service):
        direct = director_service.get_one(1)
        assert direct.name == 'Pasha'

    def test_get_all(self, director_service):
        directs = director_service.get_all()
        assert len(directs) > 0

    def test_delete(self, director_service):
        direct = director_service.delete(5)
        assert direct is None

    def test_update(self, director_service):
        direct = director_service.update(9)
        assert direct is not None

    def test_create(self, director_service):
        direct = director_service.create(2)
        assert direct is not None
