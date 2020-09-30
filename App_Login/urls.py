from django.urls import path
from App_Login import views

app_name = 'App_Login'

urlpatterns = [
path('signup/', views.sign_up, name='signup'),
path('logout/', views.logout_user, name='logout'),
path('profile/', views.user_profile, name='profile'),
path('login/', views.login, name='login'),
]
