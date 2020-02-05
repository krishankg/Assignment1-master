from django.urls import path
from . import views

app_name='post'

urlpatterns=[
   path('',views.PostListView.as_view(),name='list'),
   # path('post/<int:pk>/',views.PostDetailView.as_view(),name='detail'),
   path('like/<int:id>/',views.like,name='like'),
   path('dashboard/',views.dashboard,name='dashboard'),
]