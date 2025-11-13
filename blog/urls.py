from django.urls import path
from .views import home_page, login, signup, main, api_login, api_signup, forgot

app_name = "blog"

urlpatterns = [
    path("", home_page, name="home"),
    path("main/", main, name="main"),
    path("login/", login, name="login"),  
    path("api/login/", api_login, name="api_login"), 
    path("signup/", signup, name="signup"),
    path("api/signup/", api_signup, name="api_signup"),
    path("forgot/", forgot, name="forgot")
]
