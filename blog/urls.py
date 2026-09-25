from django.urls import path 
from.import views
from.views import PostListView,PostDetailView, about, contact

urlpatterns = [
    path('', views.PostListView.as_view(), name='home'),
    path('posts/<slug:slug>/',views.post_detail, name='post_detail'),
    path('about/', views.about, name='about'),
    path('contact/',views.contact, name='contact'), 
   ]