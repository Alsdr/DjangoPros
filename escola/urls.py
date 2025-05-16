from django.urls import path, include
from rest_framework.routers import DefaultRouter
from escola.views import ClientViewSet, ProductViewSet, EmployeeViewSet, SaleViewSet

router = DefaultRouter()
router.register('clients', ClientViewSet)
router.register('products', ProductViewSet)
router.register('employees', EmployeeViewSet)
router.register('sales', SaleViewSet)

urlpatterns = [
    path('', include(router.urls)),
]

