from django.contrib import admin
from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
urlpatterns = [
path('admin/', admin.site.urls),
path('',views.indexpage,name='indexpage'),
path('submit',views.submit,name='submit'),
path('delete/<int:myid>',views.delete,name='delete'),
path('view/<int:myid>',views.view,name='view'),
path('edit/<int:myid>',views.edit,name='edit'),
]
