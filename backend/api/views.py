import json
from django.shortcuts import render
from django.http import JsonResponse
from products.models import Product
from django.forms.models import model_to_dict
from rest_framework.response import Response
from rest_framework.decorators import api_view
from products.serializers import ProductSerializer

# Create your views here.

# def api_home(request, *args, **kwargs):

#     # Mirror responde from client
        
#     # print(request.GET) #collects url query parameters
#     # body = request.body
#     # data = {}
#     # try:
#     #     data = json.loads(body) #String of json data
#     # except:
#     #     pass
    
#     # print(data)
#     # data['params'] = dict(request.GET)
#     # data['headers'] = dict(request.headers)
#     # data['content_type'] = request.content_type
 



#     # Convert model to dictionary and return to client using jsonresponse 
#     model_data = Product.objects.all().order_by("?").first()
#     data = {}
#     if model_data:
#         # data['title'] = model_data.title
#         # data['content'] = model_data.content
#         # data['price'] = model_data.price
        
#         data = model_to_dict(model_data,fields = ['id','title','price','content'])
    
#     return JsonResponse(data) 

@api_view(["POST"])
def api_home(request, *args, **kwargs):
    data = request.data
    instance = Product.objects.all().order_by("?").first()
    # data = {}
    # if instance:
    #     # data['title'] = instance.title
    #     # data['content'] = instance.content
    #     # data['price'] = instance.price
       
        
    #     # data = model_to_dict(instance,fields = ['id','title','price','content',"sale_price"])
    #     # data['sale_price'] = instance.sale_price
    #     data = ProductSerializer(instance).data 

    serializer = ProductSerializer(data = request.data)
    if serializer.is_valid(raise_exception=True):
        instance = serializer.save() 
        print(serializer.data)
        
        
        return Response(serializer.data)