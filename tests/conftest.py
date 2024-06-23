import pytest


@pytest.fixture(scope="session")
def db(request):
    def _wraper(type_of_figure, type_of_number):
        if type_of_figure == 'rectangle':
            if type_of_number == 'integer':
                return 3, 5, 15
            if type_of_number == 'float':
                return 3.5, 5.5, 19.25
        if type_of_figure == 'square':
            if type_of_number == 'integer':
                return 5, 50
            if type_of_number == 'float':
                return 5.5, 60.5
        if type_of_figure == 'circle':
            if type_of_number == 'integer':
                return 5, 78.53981633974483
            if type_of_number == 'float':
                return 5.5, 95.03317777109125
        if type_of_figure == 'triangle':
            if type_of_number == 'integer':
                return 6, 5, 7, 264.5448922205832
            if type_of_number == 'float':
                return 6.5, 5.5, 7.7, 346.0752994590735
    yield _wraper


@pytest.fixture()
def api_server(db):
    yield db