from django.urls import path
from .views import PostListView, post_detail, post_share

app_name = 'blog'

urlpatterns = [
    path('', PostListView.as_view(), name='post_list'),
    path('<int:year>/<int:month>/<int:day>/<slug:slug>/', post_detail, name='post_detail'),
    path('post_share/<int:post_id>/', post_share, name='post_share')
]