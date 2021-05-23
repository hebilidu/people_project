from django.urls import path
from . import views

urlpatterns = [
    path('people/', views.peopleall),
    path('people/<str:pid>', views.peopleid),
]