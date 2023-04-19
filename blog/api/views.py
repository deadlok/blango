from rest_framework import generics
from blog.api.permissions import AuthorModifyOrReadonly, IsAdminUserForObject

from blog.api.serializers import PostSerializer, UserSerializer
from blog.models import Post, Tag
from blango_auth.models import User


class PostList(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [AuthorModifyOrReadonly|IsAdminUserForObject]
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class UserDetail(generics.RetrieveAPIView):
    lookup_field = "email"
    queryset = User.objects.all()
    serializer_class = UserSerializer