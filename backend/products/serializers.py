from rest_framework import serializers
from .models import Product 
from rest_framework.reverse import reverse
from .validators import validate_title
from api.serializers import UserPublicSerializer

# Serializer for Product model, including custom fields and methods
class ProductSerializer(serializers.ModelSerializer):
    user = UserPublicSerializer(read_only=True)  # Serialize the associated user
    my_discount = serializers.SerializerMethodField(read_only=True)  # Custom field to show discount
    edit_url = serializers.SerializerMethodField(read_only=True)  # URL for editing the product
    url = serializers.HyperlinkedIdentityField(view_name='product-detail', lookup_field='pk')  # Detail view URL
    address = serializers.CharField(source='content', read_only=True)  # Maps 'address' field to 'content'

    class Meta:
        model = Product
        fields = [
            'user',
            'url',
            'edit_url',
            'pk',
            'title',
            'content',
            'price',
            'sale_price',
            'address',
            'my_discount',
        ]

    # Custom validation for the title to ensure uniqueness
    def validate_title(self, value):
        qs = Product.objects.filter(title__iexact=value)
        if qs.exists():
            raise serializers.ValidationError(f'{value} is already a product name')
        return value

    # Method to construct edit URL, dynamically generating it based on the request context
    def get_edit_url(self, obj):
        request = self.context.get('request')
        return reverse("product-edit", kwargs={'pk': obj.pk}, request=request)

    # Method to calculate and return discount for a product, if applicable
    def get_my_discount(self, obj):
        try:
            return obj.get_discount()
        except:
            return None
