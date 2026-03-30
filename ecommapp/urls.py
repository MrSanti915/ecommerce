from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProductViewset, OrderViewset

router=DefaultRouter()
router.register('products', ProductViewset)
router.register('order', OrderViewset)

urlpatterns = [
   path('', include(router.urls),)
]