from django.urls import path

# import home.views import home_page
from home import views as home


urlpatterns = [
    path("", home.home_page, name="home_page"),
]