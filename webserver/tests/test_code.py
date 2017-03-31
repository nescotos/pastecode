import json
from webserver.models import Code
from webserver import app
import logging

class TestCode(object):
    bearer = 'Bearer '
    code_id = ''
    with app.test_client() as client:
        response = client.post('/login', data=dict(username='pythonDev',password='123456'))
        data = json.loads(response.data)
        bearer = bearer + str(data['access_token'])  
        logging.error(bearer)

    def test_post_code_without_access_token(self):
        with app.test_client(self) as client:
            response = client.post('/code')
            assert response.status_code == 401

    def test_post_code_with_missing_fields(self):
        with app.test_client(self) as client:
            logging.debug(self.bearer)
            response = client.post('/code',
            headers={
                'Authorization' : self.bearer
            })
            assert response.status_code == 400

    def test_post_code(self):
        with app.test_client(self) as client:
            response = client.post('/code', data=dict(
                code='var j = 7; \n var l = 14;',
                language=1,
                isPublic=True
            ),
            headers={
                'Authorization' : self.bearer
            })
            data = json.loads(response.data)
            assert response.status_code == 200
            assert data['status'] == True


    code = Code.query.filter_by(code='var j = 7; \n var l = 14;').first()
    code_id = code._id

    def test_updated_code_without_authorization(self):
        with app.test_client(self) as client:
            response = client.put('/code/{0}'.format(self.code_id))
            data = json.loads(response.data)
            assert response.status_code == 401

    def test_updated_code(self):
        with app.test_client(self) as client:
            response = client.put('/code/{0}'.format(self.code_id), data=dict(
                isPublic=False
            ),
            headers={
                'Authorization' : self.bearer
            })
            data = json.loads(response.data)
            assert response.status_code == 200
            assert data['message'] == 'Updated'
            assert data['status'] == True
    

    def test_get_specific_code_with_inexistent_id(self):
        with app.test_client(self) as client:
            response = client.get('/code/56')
            data = json.loads(response.data)
            assert response.status_code == 200
            assert data['status'] == False
            assert data['message'] == 'Code does not exist'


    def test_get_specific_code(self):
        with app.test_client(self) as client:
            response = client.get('/code/{0}'.format(self.code_id))
            data = json.loads(response.data)
            assert response.status_code == 200            
            assert data['status'] == True
            assert data['code']['code'] == 'var j = 7; \n var l = 14;'


    def test_delete_specific_code(self):
        with app.test_client(self) as client:
            response = client.delete('/code/{0}'.format(self.code_id),
            headers={
                'Authorization' : self.bearer
            })
            data = json.loads(response.data)
            assert response.status_code == 200
            assert data['status'] == True
            assert data['message'] == 'Code Deleted'

            
    def test_delete_specific_code_with_invalid_id(self):
        with app.test_client(self) as client:
            response = client.delete('/code/85965',
            headers={
                'Authorization' : self.bearer
            })
            data = json.loads(response.data)
            assert response.status_code == 200
            assert data['status'] == False
            assert data['message'] == 'Code does not exist o does not belong to you'
