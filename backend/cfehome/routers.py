from products.viewsets import ProductViewSet, ProductGenericViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('products-abc', ProductGenericViewSet, basename = 'products')


print(router.urls)
urlpatterns = router.urls   