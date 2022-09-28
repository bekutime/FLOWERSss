from django.contrib.auth.models import User
from django.test import TestCase, Client
from rest_framework.authtoken.models import Token

class AccountsTest(TestCase):
    def test_create_success(self):
        c = Client()
        response = c.post("http://127.0.0.1:8000/auth-employe/register/",
                          data={
                              "login": "asdqwerty2387y2",
                              "password": "asd12asd234",
                          })
        assert response.status_code == 200

    #ТЕСТ-2: авторизация
    def test_should_login(self):
        c = Client()
        response = c.post(
            "http://127.0.0.1:8000/auth-employe/login/",
            data={
                "login": "bekdsdca",
                "password": "passadssword1",
                }
            )

        assert response.status_code == 200


    def test_should_not_login(self):
        c = Client()
        response = c.post(
            "http://127.0.0.1:8000/auth-employe/login/",
            data={
                'login': "beka",
                "password": "passwosard1",
                }
            )
        assert response.status_code == 200

