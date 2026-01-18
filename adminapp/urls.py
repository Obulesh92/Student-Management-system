from django.urls import path
from .views import home, admin_login, admin_dashboard, contact_us
urlpatterns = [
    # Define your adminapp URL patterns here
    path("",home,name="home"),
    path("admin_login/",admin_login,name="admin_login"),
    path("admin_dashboard/",admin_dashboard,name="admin_dashboard"),
    path("contact/",contact_us,name="contact"),
]