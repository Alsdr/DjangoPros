from rest_framework import viewsets
from escola.models import Client, Product, Employee, Sale
from escola.serializers import ClientSerializer, ProductSerializer, EmployeeSerializer, SaleSerializer
from escola.filters import ClientFilter, ProductFilter, EmployeeFilter, SaleFilter
from django_filters.rest_framework import DjangoFilterBackend


class ClientViewSet(viewsets.ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    filter_backends = (DjangoFilterBackend,)
    filter_class = ClientFilter


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = (DjangoFilterBackend,)
    fitler_class = ProductFilter



class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    filter_backends = (DjangoFilterBackend,)
    filter_class = EmployeeFilter


class SaleViewSet(viewsets.ModelViewSet):
    queryset = Sale.objects.all()
    serializer_class = SaleSerializer
    filter_backends = (DjangoFilterBackend,)
    filter_class = SaleFilter