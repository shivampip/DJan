from django.shortcuts import render
from .models import Product

# Create your views here.

def product_detail_view(request):
    obj= Product.objects.get(id= 1)
    #context= {
    #    'name': obj.title,
    #    'des': obj.description
    #}
    context = { 'object' : obj }
    #return render(request, "product/detail.html", context)
    return render(request, 'mypro/pro_details.html', context) 