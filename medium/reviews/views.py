from .models import Product, Image
from .serializers import ImageSerializer, ProductSerializer
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_flex_fields.views import FlexFieldsMixin, FlexFieldsModelViewSet
from rest_flex_fields import is_expanded


class ImageViewSet(FlexFieldsModelViewSet):
    serializer_class = ImageSerializer
    queryset = Image.objects.all()


class ProductViewSet(FlexFieldsMixin, viewsets.ReadOnlyModelViewSet):

    serializer_class = ProductSerializer
    permit_list_expands = ['category','sites','comments','sites.company','sites.productsize']
    filterset_fields = ('category',)

    def get_queryset(self):
        queryset = Product.objects.all()

        if is_expanded(self.request, 'category'):
            queryset = queryset.prefetch_related('category')

        if is_expanded(self.request, 'comments'):
            queryset = queryset.prefetch_related('comments')

        if is_expanded(self.request, 'sites'):
            print(ProductSerializer)
            queryset = queryset.prefetch_related('sites')
        
        if is_expanded(self.request, 'company'):
            queryset = queryset.prefetch_related('sites__company')

        if is_expanded(self.request, 'productsize'):
            queryset = queryset.prefetch_related('sites__productsize')
        
        return queryset