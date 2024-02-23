from django.urls import path
from . import views

urlpatterns = [
    path('', views.main_window, name='mainhost_window'),
    path('text', views.text_exercise_settings, name='text-settings'),
    path('text/create', views.create, name='create_text'),
    path('text/run/', views.run_text, name='run_text')
]
