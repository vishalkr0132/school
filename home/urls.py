from home import views
from django.conf import settings
from django.urls import include, path

urlpatterns = [
    path('',views.index, name='home'),
    path('about',views.about, name='about'),
    path('language',views.language, name='language'),
    path('communication',views.communication, name='communication'),
    path('business',views.business, name='business'),
    path('software',views.software, name='software'),
    path('social_media',views.social_media, name='social_media'),
    path('photography',views.photography, name='photography'),
    path('course_details',views.course_details,name='course_details'),
    path('coming_soon',views.coming_soon,name='coming_soon'),
    path('blog',views.blog, name='blog'),
    path('gallery',views.gallery, name='gallery'),
    path('contact',views.contact, name='contact'),
    path('login',views.loginuser, name='login'),
    path('register',views.register, name='register'),
    path('form',views.form,name='form'),
    path('faq',views.faq,name='faq'),
    
]