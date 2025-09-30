from django.urls import path
from . import views as authenticationappviews
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', authenticationappviews.index, name ='index'),
    path('login/', authenticationappviews.Login, name ='login'),
    path("logout/", authenticationappviews.logout_view, name="logout"),
    path('register/', authenticationappviews.register, name ='register'),
]