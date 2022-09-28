from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters, status
from rest_framework.response import Response
from core.serializers import ProductSerializer, ProductDetailSerializer, SortSerializer, HeightSerializer,\
    CommentSerializer, ProductCreate
from rest_framework.viewsets import ModelViewSet
from core.models import Product, Sort, Height, Comment


class ProductView(ModelViewSet):
    queryset = Product.objects.all().order_by('-id', '-price')
    serializer_class = ProductSerializer
    serializer_classes = {
        'retrieve': ProductDetailSerializer,
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
        try:
            serializer = self.get_serializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save(user=self.request.user,
                            product_id=kwargs.get('product_pk'))
            headers = self.get_success_headers(serializer.data)
            return Response(serializer.data, status=status.HTTP_201_CREATED,
                        headers=headers)
        except ValueError:
            return Response('Нельзя добовлять комментарии не авторизованным пользователям', status=status.HTTP_500_INTERNAL_SERVER_ERROR)
class CreateView(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductCreate





















# class ImageView(ModelViewSet):
#     queryset = ObjectImage.objects.all()
#     serializer_class = ImageSerializer
#     lookup_field = 'pk'
#
#     @action(detail=False, methods=["POST"])
#     def multiple_upload(self, request, *args, **kwargs):
#         serializer = MultipleImageSerializer(data=request.data or None)
#         serializer.is_valid(raise_exception=True)
#         user =serializer.save()
#
#         if User.objects.filter(user=user).exists():
#             images = serializer.validated_data.get("images")
#             images_list = []
#             for image in images:
#                 images_list.append(
#                     ObjectImage(image=image)
#                 )
#                 if images_list:
#                     ObjectImage.objects.bulk_create(images_list)
#                     return Response("Succes")


    # def post(self, request, *args, **kwargs):
    #     image_link = request.data['image_link']
    #     form_data = {}
    #     form_data['image_link'] = image_link
    #     success = True
    #     response = []
    #     for images in request.FILES.getlist('images'):
    #         form_data['images'] = images
    #         print(form_data)
    #         serializer = ImageSerializer(data=form_data)
    #         if serializer.is_valid():
    #             serializer.save()
    #             response.append(serializer.data)
    #         else:
    #             success = False
    #     if success:
    #         # return Response(response, status=status.HTTP_201_CREATED)
    #
    #         return Response({
    #             'status': 1,
    #             'message': 'Success',
    #             'Data': response,
    #         })
    #
    #     # returnResponse(response,status=status.HTTP_400_BAD_REQUEST)
    #
    #     return Response({
    #         'status': 0,
    #         'message': 'Error!',
    #     })
    # class ImageView(APIView):
#     parser_classes = (MultiPartParser, FormParser)
#
#     def get(self, request):
#         all_images = ObjectImage.objects.all()
#         serializer = ImageSerializer(all_images, many=True)
#         return JsonResponse(serializer.data, safe=False)
#
#     def post(self, request, *args, **kwargs):
#         image_link = request.data['image_link']
#
#         # converts querydict to original dict
#         images = dict((request.data).lists())['image']
#         flag = 1
#         arr = []
#         for img_name in images:
#             modified_data = modify_input_for_multiple_files(image_link,
#                                                             img_name)
#             file_serializer = ImageSerializer(data=modified_data)
#             if file_serializer.is_valid():
#                 file_serializer.save()
#                 arr.append(file_serializer.data)
#             else:
#                 flag = 0
#
#         if flag == 1:
#             return Response(arr, status=status.HTTP_201_CREATED)
#         else:
#             return Response(arr, status=status.HTTP_400_BAD_REQUEST)
#
