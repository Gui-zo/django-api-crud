from rest_framework import serializers

from django.contrib.auth import get_user_model

User = get_user_model()


class UserPublicSerializer(serializers.Serializer):
    username = serializers.CharField(read_only=True)
    this_is_not_real = serializers.CharField(read_only=True)
    id = serializers.IntegerField(read_only=True)
    # other_products = serializers.SerializerMethodField(read_only=True)

    # def get_other_products(self, obj):
    #     user = obj
    #     my_products_qs = user.product_set.all()[:5]   # product_set = foreign key relationship; up to 5 related products
    #     return UserProductInlineSerializer(my_products_qs, many=True, context=self.context).data

    # class Meta:
    #     model = User
    #     fields = [
    #         'username',
    #         'this_is_not_real',
    #         'id'
    #     ]