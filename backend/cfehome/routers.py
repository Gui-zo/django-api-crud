# Tipically you write the routers inside the urls.py, but this file was created for learning purposes.

from rest_framework.routers import DefaultRouter

from products.viewsets import ProductGenericViewSet


router = DefaultRouter()
router.register('products', ProductGenericViewSet, basename='products')

urlpatterns = router.urls