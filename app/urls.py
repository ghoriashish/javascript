from django.urls import path,include
from.import views

urlpatterns = [
    
    path( "js/",views.JSPage,name="js"),

]

