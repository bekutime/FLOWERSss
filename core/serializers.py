from rest_framework import serializers
from core.models import Product, Sort, Height, ObjectImage, Comment


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'
        extra_kwargs = {
            'user': {'read_only': True},
            'product': {'read_only': True}
             }


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ObjectImage
        fields = '__all__'


class ProductDetailSerializer(serializers.ModelSerializer):
    image = ImageSerializer(many=True)
    comments = CommentSerializer(many=True)

    class Meta:
        model = Product
        fields = ('id', 'description', 'price', 'color', 'sum', 'image', 'comments','height')
        extra_kwargs = {
            'user': {'read_only': True}
        }


class SortSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sort
        fields = '__all__'


class HeightSerializer(serializers.ModelSerializer):
    sort = SortSerializer()

    class Meta:
        model = Height
        fields = ('id', 'name', 'height', 'sort')


class ProductSerializer(serializers.ModelSerializer):

    # height = HeightSerializer()

    class Meta:
        model = Product
        fields = ('id', 'name', 'photo', 'user')
        extra_kwargs = {
            'user': {'read_only': True}
        }

class ProductCreate(serializers.ModelSerializer):
    class Meta:
         model = Product
         fields = ('id', 'description', 'price', 'color', 'sum', 'height', 'name')
         extra_kwargs = {
             'user': {'read_only': True}
         }





#class MultipleImageSerializer(serializers.Serializer):
    # images = serializers.ListField(
    #     child=serializers.ImageField()
    # )
    # class Meta:
    #     model = ObjectImage
    #     fields = '__all__'
