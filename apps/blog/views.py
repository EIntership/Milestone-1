from rest_framework import viewsets
from rest_framework.generics import GenericAPIView, get_object_or_404, CreateAPIView,ListCreateAPIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from apps.blog.models import Category, Blog, Comment
from apps.blog.serializers import CategorySerializer, BlogSerializer , BlogCommentSerializer, CommentSerializer


class CategoryViewSet(viewsets.ModelViewSet):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()


class BlogListView(GenericAPIView):
    serializer_class = BlogSerializer

    permission_classes = (AllowAny,)
    authentication_classes = ()

    def get(self, request):
        blogs = Blog.objects.filter(published=True)
        return Response(BlogSerializer(blogs, many=True).data)


class BlogItemView(ListCreateAPIView):
    serializer_class = BlogCommentSerializer
    permission_classes = (AllowAny,)
    authentication_classes = ()

    def get(self, request, pk):
        blog = get_object_or_404(Blog.objects.filter(pk=pk, published=True))
        return Response(BlogCommentSerializer(blog).data)


class CommentItemView(ListCreateAPIView):
    serializer_class = CommentSerializer
    permission_classes = (AllowAny,)
    authentication_classes = ()

    def get(self, request, pk):
        comment = get_object_or_404(Comment.objects.filter(pk=pk))
        return Response(CommentSerializer(comment).data)

