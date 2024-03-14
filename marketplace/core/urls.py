from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from . import views
from .forms import LoginForm 
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('',views.index,name='index'),
    path('contact-us/',views.contact,name='contact'),
    path('signup/',views.signup,name='signup'),
    path('login/',auth_views.LoginView.as_view(template_name='core/login.html' , authentication_form=LoginForm),name='login'), 
    path('logout/',views.logout_view,name='logout'), 
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)