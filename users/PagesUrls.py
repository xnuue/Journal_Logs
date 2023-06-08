"""File defines url patterns for users. Because we are using the custom view for django which includes predefined
   url patterns for user related activities like login , out, password chnges etc, we import it here as auth_views
   which gives us the power to customize the urls to our own application requirements. for eg, I needed to specify the
   path the view should use for my login template, hence the template name below. note that am able to import views here
   because i have already included it in my urls.py in the config in the users project path"""

from django.urls import path
from django.contrib.auth import views as auth_views

from . import views

app_name = 'users'

urlpatterns = [
        #login page
        path('login/', auth_views.LoginView.as_view(template_name='usersApp/login.html'), name='login'),
        
        #logout page - its important to create a personalized view for the logout because we need to specify where the user will be redirected to when they log out of their account
        path('logout/', views.logout_view, name='logout'),

        #registeration page for new users
        path('register/', views.register, name='register'),
        ]
