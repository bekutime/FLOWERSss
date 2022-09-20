# from django.contrib.auth.base_user import BaseUserManager
#
# #Мэнэджер моделей нужна что бы взаимодействовать с вашей моделькой
# # чаще всего используется что бы возврощать преброзованные querset
# # то есть вы делаете запрос через orm в бд, и каким то особенным оброзам получаете преоброзованный querset получаете в ответ
#
# class UserManager(BaseUserManager):
#     use_in_migrations = True
#
#     ''' у нас есть метод _create_user_ который принимает данные пользователя  '''
#
#     def _create_user(self, username=None, phone=None, email=None, password=None, **extra_fields):
#         #'''здесь идут проверки'''
#         if not username:
#             if not email and not phone:
#                 raise ValueError('The given email/phone must be set')
#         # Контекст --- пользователь может зарегистрироваться через номер телефона так и по емаил
#         # Соответственно он выбирает либо емаил или номер телефона для регистраций
#         #  И ПО ЭТОМУ МЫ ОРЕНТИРУЕМСЯ, НА ТО ЧТО У НЕГО ЗАДАНО  ЛИБО ПО ЕМАИЛ ЛИБО ПО НОМЕР ТЕЛЕФОНУ
#         # Есть ли Емаил?
#         if email:
#             email = self.normalize_email(email)
#
#             if not username:
#                 username = email
#         # Если существует или есть  модель пользователя! то она будет выглядеть вот таким
#             user = self.model(
#                 email=email,
#                 username=username,
#                 **extra_fields
#             )
#         # Есть ли  номер ?
#         if phone:
#             if not username:
#                 username = phone
#             # Если есть номер телефона , то модель пользователся будет выглядеть вот таким
#             user = self.model(
#                 username=username,
#                 phone=phone,
#                 **extra_fields
#             )
#
#         # проверяем является ли пользователь
#         # суперпользователем
#         if extra_fields.get('is_superuser'):
#             user = self.model(
#                 username=username,
#                 **extra_fields
#             )
#             #user = self.model(email=email, **extra_fields)
#             user.set_password(password)
#             user.save(using=self._db)
#             return user
#
#     def create_user(self, username, email, password = None, **extra_fields ):
#         extra_fields.setdefault('is_superuser', False)
#         return self._create_user(username=username, email=email, password=password, **extra_fields)
#
#     def create_super_user(self, username, password=None, **extra_fields ):
#         # По дефолту внизу выстовляем, is_superuser, is_staff, is_active
#         extra_fields.setdefault('is_superuser', True)
#         extra_fields.setdefault('is_staff', True)
#         extra_fields.setdefault('is_active', True)
#         # И в том случае если к нам приходит наш супер юзер в значении False
#         # мы будем выбрасывать ошибочку raise ValueError
#         if extra_fields.get('is_superuser') is not True:
#             raise ValueError('Super user must have is_superuser=True.')
#
#         return self._create_user(
#             username=username,
#             password=password,
#             **extra_fields
#         )
