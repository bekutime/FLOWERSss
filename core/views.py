from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters, status
from rest_framework.response import Response
from core.serializers import ProductSerializer, ProductDetailSerializer, SortSerializer, HeightSerializer,\
    CommentSerializer
from rest_framework.viewsets import ModelViewSet
from core.models import Product, Sort, Height, Comment


class ProductView(ModelViewSet):
    queryset = Product.objects.all().order_by('-id', '-price')
    serializer_class = ProductSerializer
    serializer_classes = {
        'retrieve': ProductDetailSerializer
    }
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['height']
    search_fields = ['id', 'name']
    ordering_fields = ['id', 'price']

    def get_serializer_class(self):
        return self.serializer_classes.get(self.action, self.serializer_class)


class HeightView(ModelViewSet):
    queryset = Height.objects.all()
    serializer_class = HeightSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = []


class SortView(ModelViewSet):
    queryset = Sort.objects.all()
    serializer_class = SortSerializer


class CommentView(ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    lookup_field = 'pk'

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(
            user=self.request.user,
            product_id=kwargs.get('product_pk')
        )
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED,
                        headers=headers)


