import pytest


body = {'project_id ': 85871,
        'project_tasks_resource_id': 12749740,
        'volume': '31.0200000000',
        'cost': '160.0000000000',
        'needed_at': 1719675230,
        'batch_number': 999999,
        'batch_parent_request_id': 99888,
        'is_over_budget': 0}


def pytest_addoption(parser):
    parser.addoption("--token", help="token for test API")
    parser.addoption("--base_url", default = "https://api.gectaro.com")


@pytest.fixture(scope='session')
def token(request):
    return request.config.getoption('--token')


@pytest.fixture(scope='session')
def base_url(request):
    return request.config.getoption('--base_url')


@pytest.fixture(scope="session")
def td(request):
    def _wrapper(type_request):
        project_id = '85871'
        if type_request == 'post_resource_code':
            data = body
            return project_id, data
        if type_request == 'post_resource_id':
            data = body
            return project_id, data
        if type_request == 'put_resource_id':
            project_id = [85871, 85872]
            _id = [9405828, 9405827]
            return project_id, _id
        if type_request == 'get_company':
            company_id = 722
            return project_id, company_id
        return project_id
    yield _wrapper


