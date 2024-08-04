from django.urls import path
from . import views

app_name = 'userprofile'

urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('signup/', views.signup_view, name='signup'),
    path('my-account/', views.my_account, name='my_account'),    
]