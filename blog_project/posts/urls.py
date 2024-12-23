from rest_framework.routers import SimpleRouter

from .views import PostViewSet, UserViewSet
"""urlpatterns = [

    path('<int:pk>/', PostDetail.as_view()),
    path('', PostList.as_view()),
    path('users/', UserList.as_view()),
    path('users/<int:pk>/', UserDetail.as_view())

]"""
router = SimpleRouter()
router.register('users', UserViewSet, basename='user')
router.register('', PostViewSet, basename='post')


urlpatterns = router.urls
