from django.urls import path
from . import views

app_name = 'contacts'

urlpatterns = [
    path('', views.contact_list, name='contact_list'),
    path('contact/<int:pk>/', views.contact_detail, name='contact_detail'),
    path('create/', views.contact_create, name='contact_create'),
    path('<int:pk>/update/', views.contact_update, name='contact_update'),
    path('<int:pk>/delete/', views.contact_delete, name='contact_delete'),
    path('churches/', views.church_list, name='church_list'),
    path('churches/create/', views.church_create, name='church_create'),
    path('churches/<int:pk>/', views.church_detail, name='church_detail'),
    path('prospects/', views.prospect_list, name='prospect_list'),
    path('prospects/create/', views.prospect_create, name='prospect_create'),
    path('prospects/<int:pk>/', views.prospect_detail, name='prospect_detail'),
    path('non-prospects/', views.non_prospect_list, name='non_prospect_list'),
    path('non-prospects/create/', views.non_prospect_create, name='non_prospect_create'),
    path('non-prospects/<int:pk>/', views.non_prospect_detail, name='non_prospect_detail'),    
]