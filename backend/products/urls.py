from django.urls import path
from . import views
from .views import productdet

urlpatterns = [
    path('<int:pk>/', productdet, name = 'product-detail'),
    path('mix/<int:pk>', views.ProductMixinView.as_view()),
    path('<str:pk>/update', views.ProductUpdateAPIView.as_view(), name = 'product-edit'),
    path('list/', views.ProductListAPIView.as_view()),
    path('<int:pk>/delete', views.ProductDeleteApiView.as_view()),
    path('', views.ProductListCreateAPIView.as_view()),
    
    
] 

# if using function based apiview and not the generic one
# path('', views.product_alt_view),
# path('<str:pk>',views.product_alt_view)


# 
# 