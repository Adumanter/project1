from django.urls import path
from .views import index, about, my_skills, my_experience

urlpatterns = [
    path('', index, name='index'),
    path('about/', about, name='about'),
    path('skills/', my_skills, name='skills'),
    path('experience/', my_experience, name='experience'),
]