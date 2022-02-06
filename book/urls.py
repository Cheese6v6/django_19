from django.urls import path
from . import views

app_name="book"

urlpatterns = [
    path('index/', views.index, name="index"),
    path('cre/', views.create, name="create"),
    path('del/<bpk>', views.delete, name="delete"),
]