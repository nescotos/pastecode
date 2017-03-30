import json
from webserver.models import User
from webserver import app

class TestUser(object):

    def test_post_user_with_missing_fields(self):
        with app.test_client(self) as client:
            response = client.post('/user')
            assert response.status_code == 400

    def test_post_user(self):
        with app.test_client(self) as client:
            response = client.post('/user', data=dict(
                name='pythonDev',
                email='pythondev@devs.com',
                password='123456'
            ))
            data = json.loads(response.data)
            assert data['status'] == True

    def test_get_specific_user(self):
        user = User.query.filter_by(name='pythonDev').first()
        with app.test_client(self) as client:
            response = client.get('/user/{0}'.format(user._id))
            data = json.loads(response.data)
            assert response.status_code == 200
            assert data['status'] == True
            assert data['message'] == 'Enjoy the data'

    def test_login_user_with_invalid_credentials(self):
        with app.test_client(self) as client:
            response = client.post('/login', data=dict(
                username='elmechon504',
                password='porxy'
            ))
            data = json.loads(response.data)
            assert response.status_code == 401
            assert data['message'] == 'Username or password incorrect'

    def test_login_user_with_no_credentials(self):
        with app.test_client(self) as client:
            response = client.post('/login')
            data = json.loads(response.data)
            assert response.status_code == 400
            assert data['message'] == 'Missing fields'

    def test_login_with_valid_credentials(self):
        with app.test_client(self) as client:
            response = client.post('/login', data=dict(
                username='pythonDev',
                password='123456'
            ))
            data = json.loads(response.data)
            assert response.status_code == 200
            assert data['access_token'] is not None

    