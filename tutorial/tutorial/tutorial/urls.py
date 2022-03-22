from django.urls import path, include
from django.contrib import admin

# 空的url，要加入snippets文件夹下面的urls
urlpatterns = [
    # path('',include('snippets.urls')),
    path('admin/',admin.site.urls),
    path('v1/',include('blog.urls')),
    path('api-auth/', include('rest_framework.urls'))
]