from django.shortcuts import render,get_object_or_404
from django.contrib.auth.models import User
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from  productapp.models import ProductDB
from productapp.serializers import ProductSerializer
from rest_framework.permissions import IsAuthenticated
# Create your views here.

class RegistrationView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        username = request.data.get('username')
        email = request.data.get('email')
        password = request.data.get('password')

        user = User.objects.create_user(
            username=username,
            email=email,
            password=password
        )

        return Response("User registration successfully")



class ProductListCreateView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        products = ProductDB.objects.all()
        serializer_instance = ProductSerializer(products, many=True)
        return Response(serializer_instance.data)

    def post(self, request):
        serializer_instance = ProductSerializer(data=request.data)

        if serializer_instance.is_valid():
            serializer_instance.save()
            return Response("Product added successfully")

        else:
            return Response(serializer_instance.errors)


class ProductRetrieveUpdateDeleteView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, pk):
        product = get_object_or_404(ProductDB, id=pk)
        serializer_instance = ProductSerializer(product)
        return Response(serializer_instance.data)

    def put(self, request, pk):
        product = get_object_or_404(ProductDB, id=pk)

        serializer_instance = ProductSerializer(
            product, data=request.data
        )

        if serializer_instance.is_valid():
            serializer_instance.save()
            return Response("Product updated successfully")

        else:
            return Response(serializer_instance.errors)

    def delete(self, request, pk):
        product = get_object_or_404(ProductDB, id=pk)
        product.delete()
        return Response("Product deleted successfully")


class LogoutView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        request.user.auth_token.delete()
        return Response("Logout success")




