#codes define the url patterns for the pages in my learning_log web app
"""The url function is imported as it is needed when mapping urls to views.
    the dot tells django to import views from the current working directory.
    The empty path signified by '' tells python to look for a url with nothing between the beginning and end of
    the url. Because of this, when you type in the local host ip, python will take you
    staright to the learning log homepage instead of the django welcome page. The third 
    arguement names the hompage url 'index' and the second argument calls the view function
    on this page"""

from django.urls import path
from . import views

app_name = 'learning_logs'

urlpatterns = [
        #Home page
        path('', views.index, name='index'),

        #page that shows all topics
        path('topics/', views.topics, name='topics'),

        #page that shows topic clicked and its entries
        path('topics/<int:topic_id>/', views.topic, name='topic'),  #second argument captures an integer and stores in topic_id

        #page for adding a new topic
        path('new_topic/', views.new_topic, name='new_topic'),

        #page for adding a new entry
        path('new_entry/<int:topic_id>/', views.new_entry, name='new_entry'),

        #page for editing an entry
        path('edit_entry/<int:entry_id>/', views.edit_entry, name='edit_entry'),
        ]
