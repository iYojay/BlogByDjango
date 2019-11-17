from django.conf.urls import url
from django.urls import path
from blog import views

#from django.conf.urls import url

# urlpatterns = [
#     url(r'blog_index/',views.blog_index),
#     url(r'index/',views.index),
#
#
# ]


app_name = 'blog'

urlpatterns = [
    url(r'^$', views.index, name='index'),
    path('posts/<int:pk>/', views.detail, name='detail'),
    path('archives/<int:year>/<int:month>/', views.archive, name='archive'),
    path('categories/<int:pk>/', views.category, name='category'),
    path('tags/<int:pk>/', views.tag, name='tag'),
]
