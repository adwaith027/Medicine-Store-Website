from django.contrib import admin
from django.urls import path
from medstoreapp import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('signup/',views.signup,name='signup'),
    path('login/',views.userlogin,name='login'),
    path('logout/',views.userlogout,name='logout'),
    path('home/',views.home,name='home'),
    path('about-us/',views.aboutus,name='aboutus'),
    path('create/',views.create,name='create'),
    path('view/',views.viewall,name='viewall'),
    path('update/<int:num>',views.update,name='update'),
    path('delete/<int:num>',views.deletemed,name='delete'),
]

urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)