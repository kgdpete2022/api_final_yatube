from rest_framework import viewsets, permissions, filters
from posts.models import Post, Group, Comment, Follow
from .permissions import AuthorOrReadOnly
from .serializers import PostSerializer, GroupSerializer, CommentSerializer, FollowSerializer
from rest_framework.pagination import LimitOffsetPagination



class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (AuthorOrReadOnly,)
    pagination_class = LimitOffsetPagination



class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer


class FollowViewSet(viewsets.ModelViewSet):
    serializer_class = FollowSerializer
    permission_classes = [permissions.IsAuthenticated, AuthorOrReadOnly]
    pagination_class = None
    filter_backends = (filters.SearchFilter)
    search_fields = ('user__username')

    def get_queryset(self):
        return Follow.objects.filter(user=self.request.user)

        def perform_create(self, serializer):
            serializer.save(user=self.request.user)
