# from auth_app.models import User
# from django.db.models import Q
#
#
# class AuthBackend(object):
#     # Пермишены на уровне обьекта модели
#     supports_object_permissions = True
#     # Также выключения поддержки анонимных пользователей, что бы они не могли у нас логиниться
#     supports_anonymous_user = False
#     # И выключения поддрежки не активных пользователей, если у пользователя выставлен is_active= False
#     # мы его соответственно не авторизуем
#     supports_inactive_user = False
#
#     # Есть у нас служебный метод get_user
#     #  Без него наша история наша система просто работать не будет
#     def get_user(self, user_id):
#         try:
#             return User.objects.get(pk=user_id)
#         except User.DoesNotExist:
#             return None
#
#     #У нас есть метод аунтентикейт который будет получать пользователя
#     # По одному из трех полей
#     def authhenticate(self, request, username, password):
#         try:
#             user = User.objects.get(
#                 Q(username=username) | Q(email=username) | Q(phone=username)
#             )
#         except User.DoesNotExist:
#             return None
#         return user if user.check_password(password) else None
#     # Есть метод который правельно ли , пользователь ввел пароль