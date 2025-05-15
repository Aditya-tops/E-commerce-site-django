from django.shortcuts import render
from .models import Products
from django.core.paginator import Paginator
# Create your views here.

def index(request):
    products = Products.objects.all()
    #search code
    item_name = request.GET.get('item_name')
    if item_name != '' and item_name is not None:
        # products = products.filter(title=item_name)
        products = products.filter(title__icontains=item_name)
    #paginator code
    paginator = Paginator(products,4)
    page = request.GET.get('page')
    products = paginator.get_page(page)

    return render(request,'shop/index.html',{'products':products})

# from django.shortcuts import get_object_or_404

# def detail(request, id):
#     product = get_object_or_404(Products, id=id)
#     return render(request, 'shop/detail.html', {'product': product})

def detail(request,id):
     product = Products.objects.get(id=id)
     print(product)
     return render(request,'shop/detail.html',{'product':product})




