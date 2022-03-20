from wsgiref import validate
from rest_framework import serializers
from rest_framework.reverse import reverse

from api.serializers import UserPublicSerializer

from .models import Product
from . import validators


class ProductInlineSerializer(serializers.Serializer):
    url = serializers.HyperlinkedIdentityField(
        view_name='product-detail',
        lookup_field='pk',
        read_only=True
    )
    title = serializers.CharField(read_only=True)


class ProductSerializer(serializers.ModelSerializer):
    owner = UserPublicSerializer(source="user", read_only=True)    
    edit_url = serializers.SerializerMethodField(read_only=True)
    # A HyperlinkedIdentityField only works inside a ModelSerializer, whereas a SerializerMethod field works anywhere.
    url = serializers.HyperlinkedIdentityField(
        view_name='product-detail',
        lookup_field='pk'
    )
    title = serializers.CharField(
        validators=[validators.validate_title_no_hello, validators.unique_product_title])
    body = serializers.CharField(source='content')
    # name = serializers.CharField(source='title', read_only=True)
    # email = serializers.EmailField(write_only=True)
    # related_products = ProductInlineSerializer(source='user.product_set.all', read_only=True, many=True) # many is always associated to a queryset

    class Meta:
        model = Product
        fields = [
            'owner',  # user_id
            'url',
            'edit_url',
            'pk',
            'title',
            # 'name',
            'body',
            'price',
            'sale_price',
            'public',
            'path',
            # 'my_discount',
            # 'related_products'
        ]

    # def validate_title(self, value):      # def validate_<fieldname>
    #     queryset = Product.objects.filter(title__iexact=value)   # iexact = case insensitive
    #     if queryset.exists():
    #         raise serializers.ValidationError(f"{value} is already a product name.")
    #     return value

    # def create(self, validated_data):
    #     # email = validated_data.pop('email')
    #     obj = super().create(validated_data)
    #     # print(email, obj)
    #     return obj

    # def update(self, instance, validated_data):
    #     email = validated_data.pop('email')
    #     return super().update(instance, validated_data)

    def get_edit_url(self, obj):
        request = self.context.get('request')  # self.request
        if request is None:
            return None
        return reverse("product-edit", kwargs={"pk": obj.pk}, request=request)

    # def get_my_discount(self, obj):
    #     if not hasattr(obj, 'id'):
    #         return None
    #     if not isinstance(obj, Product):
    #         return None
    #     return obj.get_discount()
