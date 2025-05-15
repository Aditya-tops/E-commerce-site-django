from django.shortcuts import render
from .models import Products
# Create your views here.

def index(request):
    product = Products.objects.all()
    
    item_name = request.GET.get('item_name')
    if item_name != '' and item_name is not None:
        # product = product.filter(title=item_name)
        product = product.filter(title__icontains=item_name)

    return render(request,'shop/index.html',{'product':product})







