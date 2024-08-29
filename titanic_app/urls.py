# urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('upload_excel/', views.upload_excel, name='upload_excel'),
    path('manage_titanic/', views.manage_titanic, name='manage_titanic'),
    path('delete_titanic/<int:pk>/', views.delete_titanic, name='delete_titanic'),
    path('edit_titanic/<int:pk>/', views.edit_titanic, name='edit_titanic'),  # URL جدید برای ویرایش
]
