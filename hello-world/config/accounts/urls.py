from django.urls import path
from .views import RegisterView, LoginView, HelloView

urlpatterns = [
    path("signup/", RegisterView.as_view(), name="signup"),
    path("login/", LoginView.as_view(), name="login"),
    path("hello/", HelloView.as_view(), name="hello"),
]
