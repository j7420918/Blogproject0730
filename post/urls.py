from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('main/', views.main, name='main'),
    path('index/', views.index, name='index'),
    path('detail/<int:blog_id>', views.detail,name="detail"),
    path('new/', views.new, name='new'),
    path('renew/<int:blog_id>',views.renew, name="renew"),
    path('deldte/<int:blog_id>',views.delete, name="delete"),
    path('update/<int:blog_id>',views.update, name="update"),
    path('create/',views.create, name="create"),
    
]

