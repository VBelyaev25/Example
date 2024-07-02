import requests


class GectaroHttpClient:

    def __init__(self, base_url, token, project_id, resource = None):
        self.session = requests.Session()
        self.session.headers['Authorization'] = f'Bearer {token}'
        self.base_url = base_url
        self.project_id = project_id
        self.resource_id = resource


    @property
    def get_resource(self):
        url = f'{self.base_url}/v1/projects/{self.project_id}/resource-requests'
        return self.session.get(url, verify=False)


    def post_resource(self, data):
        url = f'{self.base_url}/v1/projects/{self.project_id}/resource-requests'
        return self.session.post(url, data=data, verify=False)


    @property
    def get_resource_id(self):
        url = f'{self.base_url}/v1/projects/{self.project_id}/resource-requests/{self.resource_id}'
        return self.session.get(url, verify=False)


    @property
    def put_resource_id(self):
        url = f'{self.base_url}/v1/projects/{self.project_id}/resource-requests/{self.resource_id}'
        return self.session.put(url, verify=False)


    @property
    def delete_resource_id(self):
        url = f'{self.base_url}/v1/projects/{self.project_id}/resource-requests/{self.resource_id}'
        return self.session.delete(url, verify=False)


    def get_company_request(self, company_id):
        url = f'{self.base_url}/v1/companies/{company_id}/resource-requests'
        return self.session.get(url, verify=False)