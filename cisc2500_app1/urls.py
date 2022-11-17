from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('learning', views.learning, name='learning'),
    path('fordham',views.fordham,name='fordham'),
    path('survey', views.get_name, name='survey'),
    path('thanks',views.thanks,name='thanks'),
    path('opensecrets',views.opensecrets,name='opensecrets')
]

from django.contrib.staticfiles.urls import staticfiles_urlpatterns
urlpatterns += staticfiles_urlpatterns()