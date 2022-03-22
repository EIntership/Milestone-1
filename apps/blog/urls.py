from django.urls import path

from apps.blog.views import CategoryViewSet, BlogListView, BlogItemView, CommentItemView
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'categories', CategoryViewSet, basename='category')

urlpatterns = router.urls

urlpatterns += [
    path('blog/', BlogListView.as_view(), name='blog_list'),
    path('blog/<int:pk>/', BlogItemView.as_view(), name='blog_item'),
    path('comments/<int:pk>', CommentItemView.as_view(), name='comment_post'),
]
