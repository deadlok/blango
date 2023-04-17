from rest_framework import generics
from blog.api.permissions import AuthorModifyOrReadonly, IsAdminUserForObject

from blog.api.serializers import PostSerializer
from blog.models import Post


class PostList(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [AuthorModifyOrReadonly|IsAdminUserForObject]
    queryset = Post.objects.all()
    serializer_class = PostSerializer