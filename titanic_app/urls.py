# urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.upload_excel, name='upload_excel'),
    path('manage_titanic/', views.manage_titanic, name='manage_titanic'),
    path('delete_titanic/<int:pk>/', views.delete_titanic, name='delete_titanic'),
    path('edit_titanic/<int:pk>/', views.edit_titanic, name='edit_titanic'),
    path('titanic_data_grid/', views.titanic_data_grid, name='titanic_data_grid'),
]
