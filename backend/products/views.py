from rest_framework import generics
from .models import Product
from .serializers import ProductSerializer
from api.mixins import StaffEditorPermissionMixin

# API view for retrieving a single product detail
class ProductDetailAPIView(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

# Shortcut to call the view
productdet = ProductDetailAPIView.as_view()

# API view for listing all products and creating a new one, with custom permissions
class ProductListCreateAPIView(generics.ListCreateAPIView, StaffEditorPermissionMixin):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    
    # Custom creation to handle additional logic
    def perform_create(self, serializer):
        email = serializer.validated_data.pop('email')  # Example of handling extra data
        title = serializer.validated_data.get('title')
        content = serializer.validated_data.get('content') or title  # Use title as content if not provided
        serializer.save(user=self.request.user, content=content)  # Save with user and modified content

    # Filter queryset to return products created by the current user
    def get_queryset(self, *args, **kwargs):
        qs = super().get_queryset(*args, **kwargs)
        return qs.filter(user=self.request.user)

# API view for listing all products, with custom permissions
class ProductListAPIView(generics.ListAPIView, StaffEditorPermissionMixin):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

# API view for updating a product, with custom permissions
class ProductUpdateAPIView(generics.UpdateAPIView, StaffEditorPermissionMixin):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'pk'  # Lookup field for finding the model instance

    # Ensure the content field is filled during update
    def perform_update(self, serializer):
        instance = serializer.save()
        if not instance.content:
            instance.content = instance.title  # Default content to title if empty

# API view for deleting a product, with custom permissions
class ProductDeleteApiView(generics.DestroyAPIView, StaffEditorPermissionMixin):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'pk'  # Lookup field for finding the model instance

    # Custom delete logic can be added here
    def perform_destroy(self, instance):
        super().perform_destroy(instance)

# Combined API view for create, list, and retrieve operations, using mixins
class ProductMixinView(mixins.CreateModelMixin, mixins.ListModelMixin, mixins.RetrieveModelMixin, generics.GenericAPIView, StaffEditorPermissionMixin):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'pk'  # Used by RetrieveModelMixin to find the model instance

    # Handle GET requests, dynamically choosing between list and retrieve operations
    def get(self, request, *args, **kwargs):
        pk = kwargs.get('pk')
        if pk is not None:
            return self.retrieve(request, *args, **kwargs)  # Retrieve a single instance
        return self.list(request, *args, **kwargs)  # List all instances

    # Handle POST requests for creating new instances
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
