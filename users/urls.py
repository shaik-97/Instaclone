# users is an APP inside instaclone
from django.urls import path
from . import views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView
)
# localhost:4444/users/index
# localhost:4444/users
# localhost:4444/

print("This is from users/urls.py \n")
print("signup invoked")
urlpatterns = [
    path('index/', views.index, name="users_main_view"), # 1.function mapped to url, 2.instead of index regular exp can also be passed
    path('signup/', views.signup_user, name="users signup"),
    #path('login/', views.login_view, name='login'),
    path('token/refresh/', TokenRefreshView.as_view(), name="refresh_token_api"),
    path('token/verify/', TokenVerifyView.as_view(), name="Token_verify_api"),
    path('Login/', TokenObtainPairView.as_view(),name='readymade_login_api'),
    path('list/',views.user_list, name='user_list_api'),
    path('build/', views.JarBuild, name='jar_build'),
    path()
]