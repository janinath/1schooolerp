from django.urls import path
from . import views
app_name='school_admin'

urlpatterns=[
    path('schooladmin',views.home, name='sahome')

]