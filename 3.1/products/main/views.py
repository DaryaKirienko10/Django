from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from .models import Product
from .serializers import ProductListSerializer, ProductDetailsSerializer


@api_view(['GET'])
def products_list_view(request):
    products = Product.objects.all()
    serializer = ProductListSerializer(products, many=True)
    return Response(serializer.data)


class ProductDetailsView(APIView):
    def get(self, request, product_id):
        try:
            product = Product.objects.get(pk=product_id)
            serializer = ProductDetailsSerializer(product)
            return Response(serializer.data)
        except Product.DoesNotExist:
            return Response({"detail": "Not found."}, status=status.HTTP_404_NOT_FOUND)


# доп задание:
class ProductFilteredReviews(APIView):
    def get(self, request, product_id):
        """обработайте значение параметра mark и
        реализуйте получение отзывов по конкретному товару с определённой оценкой
        реализуйте сериализацию полученных данных
        отдайте отсериализованные данные в Response"""
        pass
