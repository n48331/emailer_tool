from django.urls import path


from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('filter/<int:country>/<int:product>',
         views.filterProject, name='filter'),
    path('filter/',
         views.filterProject, name='notfound'),
     path('accounts/register/', views.register, name='register'),
]
