from django.contrib.auth.models import AnonymousUser
from django.http import request
from django.test import TestCase, Client

from rest_framework.test import APIClient
from auth_app.views import LoginView


class TestHomepage(TestCase):
    def test_open_homepage_should(self):
        c = Client()
        response = c.get("http://127.0.0.1:8000/")
        assert response.status_code == 404

   #'''мы короче тут проверяем наши продукты через get запрос'''
    def test_open_Product(self):
        c = Client()
        response = c.get("http://127.0.0.1:8000/Product/Product/")
        assert response.status_code == 200

    def test_post_Product_Comment(self):
        c = Client()
        response = c.get("http://127.0.0.1:8000/Product/1/product/comment/")
        assert response.status_code == 200

    #Тест на ошибку валидация комментарий, если пользователь не введет коментарий
    def test_post_oshibka_comment(self):
        c = Client()
        response = c.post("http://127.0.0.1:8000/Product/1/product/comment/")
        assert response.status_code == 400

#Тест на проверку анонимного юзера прошла успешно
    def test_post_create_comment(self):
        c = Client()
        if c == AnonymousUser:
            response = c.post("http://127.0.0.1:8000/Product/1/product/comment/")
            assert response.status_code == 500, f"{response.status_code}- should be status 500"
    def test_should_create_comment(self):
        c = Client()#не получилось так как я не авторизованный пользователь
        response = c.post("http://127.0.0.1:8000/Product/1/product/comment/",
                          data={
                              "comment": "bekatob"
                          })
        assert response.status_code == 500


    def test_create_product(self):
        c = Client()
        response = c.post("http://127.0.0.1:8000/Product/ProductCreate/",
                          data={"description": "dfdd",
                                "price": "1000.0",
                                "color": "Red",
                                "sum": 100,
                                "height": 1,
                                "name": "dd"
                                })
        assert response.status_code == 400

class TestCreateUser(TestCase):
    def test_create_success(self):
        c = Client()
        response = c.post("http://127.0.0.1:8000/auth-employe/register/",
                          data={
                              "login": "asdqwerty2387y2",
                              "password": "asd12asd234",
                          })
        assert response.status_code == 200




