from django.urls import path
from app.views import *


urlpatterns = [
    path("",home,name="home"),
    path("register/",register,name="register"),
    path("LOGIN/",LOGIN,name="login"),
    path("blog/",blog,name="blog"),
    path("create/",create,name="create"),
    path("continue/<int:id>",cont,name="continue"),
    path("delete_blog/<int:id>",delete_blog,name="delete_blog"),
    path("edit_blog/<int:id>",edit_blog,name="edit_blog")
]
