from django.urls import path
from . import views
urlpatterns = [
    path("", views.index, name="index"),
    path("login/", views.user_login, name="login"),
    path("logout/", views.user_logout, name="logout"),
    path("register/", views.user_reg, name="register"),
    path("record/<int:pk>", views.customer_record, name="record"),
    path("record/<int:pk>/delete", views.record_delete, name="record_delete"),
    path("record/<int:pk>/update", views.record_update, name="update_record"),
    path("record/create", views.record_create, name="record_create"),
]
