from django.contrib.auth.hashers import check_password
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.views import APIView
from auth_app.serializer import RegisterSerializer


# ТЕПЕРЬ С СЕРИАЛАЙЗЕРОМ

class RegisterView(APIView):
    def post(self, request, *args, **kwargs):
        serialzer = RegisterSerializer(data=request.data)
        serialzer.is_valid(raise_exception=True)
        user = serialzer.save()
        token = Token.objects.create(user=user)
        return Response({'token': str(token.key)})


class LoginView(APIView):
    def post(self, request, *args, **kwargs):
        login = request.data.get('login')
        if not User.objects.filter(username=login).exists():
            return Response('Такой Логин или Пароль не сушетвуют')
        user = User.objects.get(username=login)
        password = request.data.get('password')
        pass_check = check_password(password, user.password)
        if not pass_check:
            return Response('Такой Логин или Пароль не сушетвуют')
        token = Token.objects.get(user=user)
        return Response({'token': str(token.key)})

















#ЭТО БЕЗ СЕРИАЛАЙЗЕРА
# '''username=login я его приравниваю потому-что в auth/models есть username , и мне нужны его свойства '''
# class Register(APIView):
#
#
#     def post(self,request,*args,**kwargs):
#         login = request.data.get('login')
#         email = request.data.get('email')
#         password = request.data.get('password')
#         user = User.objects.create(email=email,username=login)
#         user.set_password(password)
#         user.save()
#         token = Token.objects.create(user=user)
#         return Response({'token':str(token.key)})