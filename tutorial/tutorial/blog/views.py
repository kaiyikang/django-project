# version 1
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Article, User
from .serializer import ArticleSerializer, UserSerializer
# version 2
from rest_framework.views import APIView
from django.http import Http404
# version 3
from rest_framework import mixins,generics
# version 4
# version 5
from rest_framework import viewsets, permissions
from .permissions import IsOwnerReadOnly

# 第五版本
# class ArticleViewSet(viewsets.ModelViewSet):
#     queryset = Article.objects.all()
#     serializer_class = ArticleSerializer

#     def perform_create(self, serializer):
#         serializer.save(author=self.request.user)

class UserViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer

# 第四版本
class ArticleList(generics.ListCreateAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

class ArticleDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,IsOwnerReadOnly)


# 第三版本
# class ArticleList(mixins.ListModelMixin, 
#                     mixins.CreateModelMixin,
#                     generics.GenericAPIView):
#     queryset= Article.objects.all()
#     serializer_class = ArticleSerializer
    
#     def get(self,request, *args, **kwargs):
#         return self.list(request, *args, **kwargs)
    
#     def post(self,request, *args, **kwargs):
#         return self.create(request, *args, **kwargs)
    
#     def perform_create(self, serializer):
#         """
#         serlialier应该包含author这个特殊项，为了满足，所以额外添加该函数。
#         调用 self.create 的时候会调用。
#         """
#         serializer.save(author=self.request.user)


# class ArticleDetail(mixins.RetrieveModelMixin,
#                     mixins.UpdateModelMixin,
#                     mixins.DestroyModelMixin,
#                     generics.GenericAPIView):
#     queryset = Article.objects.all()
#     serializer_class = ArticleSerializer

#     def get(self,request, *args, **kwargs):
#         return self.retrieve(request, *args, **kwargs)
    
#     def put(self, request, *args, **kwargs):
#         return self.put(request, *args, **kwargs)
    
#     def delete(self, request, *args, **kwargs):
#         return self.destroy(request, *args, **kwargs)


# 第二版版本，但是你可以看到，增删改查都是有重复的内容的
# class ArticleList(APIView):

#     def get(self,request , format = None):
#         articles = Article.objects.all()
#         serializer = ArticleSerializer(articles, many=True)
#         return Response(serializer.data)
    
#     def post(self,request, format=None):
#         serializer = ArticleSerializer(request.data)
#         if serializer.is_valid():
#             serializer.save(author=request.author)
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# class ArticleDetail(APIView):
#     def get_object(self,pk):
#         try:
#             return Article.objects.get(pk=pk)
#         except:
#             raise Http404
    
#     def get(self, request, pk, format=None):
#         article = self.get_object(pk)
#         serializer = ArticleSerializer(article)
#         return Response(serializer.data)
    
#     def put(self, request, pk, format=None):
#         article = self.get_object(pk)
#         serializer = ArticleSerializer(instance=article, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     def delete(self,request, pk, format= None):
#         article = self.get_object(pk)
#         article.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)




# 第一个基于 function 的版本，直观，但是非常难以 维护 和 继承
# @api_view(['GET','POST'])
# def article_list(request, format=None):
#     if request.method == 'GET':
#         article = Article.objects.all()
#         serializer = ArticleSerializer(article, many=True)
#         return Response(serializer.data)
    
#     elif request.method == "POST":
#         serializer = ArticleSerializer(data=request.data)
#         if serializer.is_valid():
#             # author is read-only, so 这里是绑定
#             serializer.save(author=request.user)
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.error, status=status.HTTP_400_BAD_REQUEST)

# @api_view(['GET','PUT','DELETE'])
# def article_detail(request, pk, format=None):
    
#     try:
#         article = Article.objects.get(pk=pk)
#     except Article.DoesNotExist:
#         return Response(status=status.HTTP_404_NOT_FOUND)

#     if request.method == "GET":
#         serializer = ArticleSerializer(article)
#         return Response(serializer.data)

#     elif request.method == "PUT":
#         serializer = ArticleSerializer(article, request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     elif request.method == 'DELETE':
#         article.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)