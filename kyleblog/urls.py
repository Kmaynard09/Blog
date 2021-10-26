from django.urls import path
from .views import HomeView, ArticleDetailView
from django.conf.urls.static import static

urlpatterns = [
    #path('', views.home, name= "home"),
    path('', HomeView.as_view(), name="home"),
    path('article/<int:pk>', ArticleDetailView.as_view(), name='blog-detail')
]
