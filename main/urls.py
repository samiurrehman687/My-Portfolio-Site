from django.urls import path
from main import views as v1
urlpatterns = [
    path('', v1.home.as_view(), name='home'),
    path('project/', v1.PorjectView.as_view() , name='project'),
    path('contact/', v1.ContactView.as_view(), name='contact'),
    path('about/', v1.AboutView.as_view(), name='about'),
]
