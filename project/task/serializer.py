# serializers.py
from rest_framework import serializers
from .models import Product, Category
from rest_framework.response import Response


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = "__all__"


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ["name"]


class ProductParams(serializers.ModelSerializer):
    category = serializers.CharField()

    class Meta:
        model = Product
        fields = ["name", "description", "price", "image", "stock_quantity", "category"]


def APIResponse(status, data=None, redirect_to=None):
    response = {"status": status}
    response["data"] = data if data else None
    if redirect_to:
        response["redirect_to"] = redirect_to
    return Response(response)
