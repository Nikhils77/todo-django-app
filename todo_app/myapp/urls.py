from django.urls import path
from . import views


urlpatterns=[
    path('',views.home,name="home"),
    path('add/',views.add,name="add"),
    path('edit/<int:id>/',views.edit,name="edit"),
    path('complete/<int:id>/',views.complete_task,name="complete"),
    path('delete/<int:id>',views.delete_task,name="delete"),
    path("register/",views.register,name="register"),
    

]