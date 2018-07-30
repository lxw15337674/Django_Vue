from django.shortcuts import render

# Create your views here.
from rest_framework.generics import ListAPIView
from rest_framework.pagination import PageNumberPagination

from .serializers import GoodsSerializer
from rest_framework.views import APIView
from .models import Goods
from rest_framework.response import Response
from rest_framework import status, mixins, generics
from rest_framework import viewsets


class GoodsPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    page_query_param = 'p'
    max_page_size = 100


class GoodsListViewSet(mixins.ListModelMixin,viewsets.GenericViewSet):
    """
    商品列表页
    """
    queryset = Goods.objects.all()
    serializer_class = GoodsSerializer
    pagination_class = GoodsPagination
    # def get(self,request,*args,**kwargs):
    #     return self.list(request,*args,**kwargs)



# class GoodsListView(APIView):
#     def get(self, request, format=None):
#         goods = Goods.objects.all()[:10]
#         goods_serializer = GoodsSerializer(goods, many=True)
#         return Response(goods_serializer.data)
#
#     def post(self, request):
#         serializer = GoodsSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
