from http_client import GectaroHttpClient as ghc
import pytest


@pytest.mark.parametrize("type_request", ["check_id", "check status code"])
def test_get_resource_positive(td, type_request, base_url, token):
    project_id = td(type_request)
    if type_request == "check_id":
        assert ghc(base_url, token, project_id).get_resource.json()[0]['id']
    if type_request == "check status code":
        assert ghc(base_url, token, project_id).get_resource.status_code == 200


@pytest.mark.parametrize(
    ('project_id', 'result'),
    [
        ('False', 404),
        (None, 404)
    ],
    ids=["bad number of company", "company is None"]
)
def test_get_resource_negative(base_url, token, project_id, result):
    assert ghc(base_url, token, project_id).get_resource.status_code == result


@pytest.mark.parametrize("type_request", ["get_resource_id id", "get_resource_id status code"])
def test_get_resource_id_positive(td, type_request, base_url, token):
    project_id = td(type_request)
    resource = 9405830
    if type_request == 'get_resource_id id':
        assert ghc(base_url, token, project_id, resource).get_resource_id.json()['id']
    if type_request == 'get_resource_id status code':
        assert ghc(base_url, token, project_id, resource).get_resource_id.status_code == 200


@pytest.mark.parametrize(
    ('project_id', 'resource', 'result'),
    [
        ('85871', None ,404),
        ('85871', 444444444 ,404)
    ],
    ids=["invalid resource_id", "bad number resource_id"]
)
def test_get_resource_id_negative(base_url, project_id, resource, result, token):
    assert ghc(base_url, token, project_id, resource).get_resource_id.status_code == result


@pytest.mark.parametrize("type_request", ["post_resource_code", "post_resource_id"])
def test_post_resource_positive(td, type_request, base_url, token):
    project_id, data = td(type_request)
    if type_request == 'post_resource_code':
        assert ghc(base_url, token, project_id).post_resource(data).status_code == 201
    if type_request == 'post_resource_id':
        assert ghc(base_url, token, project_id).post_resource(data).json()["id"] is not None


@pytest.mark.parametrize(
    ('base_url', 'project_id', 'data', 'result'),
    [
        ('https://api.gectaro.com', '85871', None ,422),
        ('https://api.gectaro.com', '85871', {'':''} ,422)
    ],
    ids= ["body request is None", "body request is empty"]
)
def test_post_resource_negative(base_url, project_id, data, result, token):
    assert ghc(base_url, token, project_id).post_resource(data).status_code == result


# # @pytest.mark.parametrize("type_request", ["project_id", "id"])
# # def test_put_resource_id_positive(td, type_request):
# #     pass
# #
# #
# # @pytest.mark.parametrize()
# # def test_put_resource_id_negative():
# #     pass


@pytest.mark.parametrize("type_request", ["id_account"])
def test_delete_resource_id_positive(td, type_request, token, base_url):
    project_id = td(type_request)
    resource_id = 9405831
    print(ghc(base_url, token, project_id, resource_id).delete_resource_id.json())


@pytest.mark.parametrize(
    ('project_id', 'resource_id', 'result'),
    [
        ( None, 9405812, 404),
        ('85871', None, 404)
    ],
    ids=["invalid project_id", "invalid resource_id"]
)
def test_delete_resource_id_negative(base_url, project_id, resource_id, result, token):
    assert ghc(base_url, token, project_id).delete_resource_id.status_code == result



@pytest.mark.parametrize("type_request", ["get_company"])
def test_get_company_request_positive(td, type_request, base_url, token):
    project_id, company_id = td(type_request)
    assert 'id' in ghc(base_url, token, project_id).get_company_request(company_id).text


@pytest.mark.parametrize(
    ('project_id', 'company_id', 'result'),
    [
        ('85871', -940581236553666454, 404),
        ('85871', None, 404)
    ],
    ids=["invalid company_id", "company_is is None"]
)
def test_get_company_request_negative(base_url, project_id, company_id, result, token):
    assert ghc(base_url, token, project_id).get_company_request(company_id).status_code == result