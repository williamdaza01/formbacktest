from django.urls import path
from app import views

app_name = 'app'

urlpatterns = [
    path('api/v1/upload-csv/', views.upload_csv, name='upload_csv'),
]
