from django.urls import path

from . import views


urlpatterns = [
    path("january", views.january),
    path("february", views.febuary),
    path("march", views.march),
    path("april", views.april)

]
