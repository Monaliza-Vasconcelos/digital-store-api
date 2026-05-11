from rest_framework import serializers
from django.contrib.auth.models import User

from .models import Product, ProductImage


class ProductImageSerializer(serializers.ModelSerializer):

    image = serializers.CharField()

    class Meta:
        model = ProductImage
        fields = ["id", "product", "image"]


class ProductSerializer(serializers.ModelSerializer):

    images = ProductImageSerializer(
        many=True,
        read_only=True
    )

    class Meta:
        model = Product
        fields = [
            "id",
            "name",
            "price",
            "price_discount",
            "reference",
            "description",
            "rating",
            "images",
        ]


class RegisterSerializer(serializers.ModelSerializer):

    class Meta:
        model = User

        fields = [
            "id",
            "username",
            "email",
            "password"
        ]

        extra_kwargs = {
            "password": {
                "write_only": True
            }
        }

    def create(self, validated_data):

        user = User.objects.create_user(
            username=validated_data["username"],
            email=validated_data["email"],
            password=validated_data["password"]
        )

        return user