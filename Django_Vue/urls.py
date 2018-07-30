"""Django_Vue URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# from django.contrib import admin
from django.urls import path, re_path, include
import xadmin
from Django_Vue.settings import MEDIA_ROOT
from django.views.static import serve
from rest_framework.documentation import include_docs_urls
# from goods.views.base import GoodsListView
from goods.views import GoodsListViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
# 配置goods的url
router.register('goods', GoodsListViewSet)

urlpatterns = [
    path('xadmin/', xadmin.site.urls),
    path('', include(router.urls)),
    path('doc/', include_docs_urls(title="生鲜")),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
