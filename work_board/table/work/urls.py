from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_views

app_name = 'work'


urlpatterns = [
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('', include('django.contrib.auth.urls')),
    path('register/', views.register, name='register'),
    path('search/', views.announcement_search, name='search'),
    path('all/', views.announcement_list, name='announcement_list'),
    path('tag/<slug:tag_slug>/',views.announcement_list, name='announcement_list_by_tag'),
    path('<int:year>/<int:month>/<int:day>/<slug:announcement>/',views.announcement_detail,
         name='announcement_detail'),
    path('edit/', views.edit, name='edit'),
    path('create/', views.announcement_create, name='create'),
    path('profile/', views.profile, name='profile'),
]
