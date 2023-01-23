from django.urls import path
from knox import views as knox_views
from . import views

urlpatterns = [
    path('user/<int:kpi_id>', views.get_user, name='user'),
]