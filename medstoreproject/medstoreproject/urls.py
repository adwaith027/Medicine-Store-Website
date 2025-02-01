from django.contrib import admin
from django.urls import path
from medstoreapp import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('signup/',views.signup,name='signup'),
    path('login/',views.login,name='login'),
    path('create/',views.create,name='create'),
    path('signup/',views.signup,name='signup'),
    path('signup/',views.signup,name='signup'),

]

urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)