from django.conf.urls import url
from django.urls import path,include

#views
from django.db import router
from .views import PostDetail,Postlist,UserDetail,UserList,PostViewset,UserViewset

#viewsets
from rest_framework.routers import SimpleRouter
router = SimpleRouter()
router.register("Userlar",UserViewset,basename='users')
router.register('Postlar',PostViewset,basename='posts')


# from rest_framework.schemas import get_schema_view #schima va dokumentla
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

#dokumitatsiya
schema_view = get_schema_view(
    openapi.Info(
        title='Blog API',
        description="Firdavs Dev uz",
        default_version='v1',
        terms_of_service='https://www.google.com/policies/terms/',
        contact=openapi.Contact(email="xackercoder@gmail.com"),
        license=openapi.License(name='Blog api lisensiyasi')
    ),
    public=True,
    permission_classes=(permissions.AllowAny,)
)

urlpatterns = [
    #post
    path('posts/',Postlist.as_view(),name='Posts'),
    path('posts/<int:pk>/',PostDetail.as_view(),name='Post_id'),
    #login register ...
    path('api-auth/', include('rest_framework.urls')),
    #user
    path('users/',UserList.as_view(),name='Users'),
    path('users/<int:pk>/',UserDetail.as_view(),name='User_id'),
                    #schema and documentatsiya
    #swaggger
    # path('swagger/',schema_view.with_ui(
    #     'swagger',cache_timeout=0
    # ),name='schema-swagger-ui'),

    #redoc
    # path('redoc/',schema_view.with_ui(
    #     'redoc',cache_timeout=0
    # ),name='schema-redoc'),

    path('dj_rest_auth/',include('dj_rest_auth.urls')),

    url(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    url(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    url(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
   
]
#coonect to viewset
urlpatterns += router.urls