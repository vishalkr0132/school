from admins import views
from django.conf import settings
from django.urls import include, path
from django.conf.urls.static import static

urlpatterns = [
    path('',views.index, name='home'),
    path('gallery',views.gallery, name='gallery'),
    path('inbox',views.inbox, name='inbox'),
    path('graphs',views.graphs, name='graphs'),
    path('logout', views.logoutuser, name='logout'),
    path('Add_image',views.Add_image,name='Add_image'),
    path('Contact',views.Contact,name='Contact'),
]