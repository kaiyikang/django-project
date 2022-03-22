from django.urls import re_path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views
from rest_framework.routers import DefaultRouter

# article_list = views.ArticleViewSet.as_view(
#     {
#         'get':'list',
#         'post':'create'
#     }
# )

# article_detail = views.ArticleViewSet.as_view(
#     {
#         'get':'retrieve',
#         'delete':'destroy',
#     }
# )

user_list = views.UserViewSet.as_view({
    'get':'list',
})


# urlpatterns = [
#     re_path(r'^articles/$', article_list),
#     re_path(r'^articles/(?P<pk>[0-9]+)$', article_detail,name='article-detail'),
#     re_path(r'^users/$', user_list),
# ]

# urlpatterns = format_suffix_patterns(urlpatterns)

# 因为views里面使用了viewSet，因此url绑定需要借助router
# router = DefaultRouter()
# router.register(r'articles', viewset=views.ArticleViewSet)

urlpatterns = [
    re_path(r'^articles/$', views.ArticleList.as_view()),
    re_path(r'^articles/(?P<pk>[0-9]+)$', views.ArticleDetail.as_view(), name="article-detail"),
    re_path(r'^users/$', user_list),
]

# 添加格式后缀
urlpatterns = format_suffix_patterns(urlpatterns)
# urlpatterns += router.urls

