# views.py
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import Product
from .serializer import ProductSerializer, ProductParams, APIResponse
from .logging_utils import log_info, log_error
from drf_spectacular.utils import extend_schema
from .models import Product

# Create a logger


class CreateProduct(APIView):
    permission_classes = [IsAuthenticated]

    @extend_schema(
        request={
            "application/json": ProductParams,
        }
    )
    def post(self, request):
        try:
            product = Product.creator(request.data)
            data = ProductSerializer(product).data
            log_info(f"Product created: {data}")
            return APIResponse(status.HTTP_201_CREATED, data)
        except Exception as e:
            log_error(f"Error creating product: {str(e)}")
            return APIResponse(status.HTTP_400_BAD_REQUEST, e)
