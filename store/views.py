from django.shortcuts import get_object_or_404, render
from .models import Category, Product


def all_products(request):
    products = Product.objects.all()
    return render(request, 'store/home.html', {'products': products})


def home(request):
    return render(request, 'store/home.html')


def categories(request):
    return{
        'categories':Category.objects.all()
    }

def product_detail(request, slug):
    product = get_object_or_404(Product, slug=slug, in_stock=True)
    return render(request, 'Products/detail.html', {'product': product})

def change_product(request, id):
    product = Product.objects.get(id=id)
    #product.title = request.title
    #product.price = request.price
    # product.description = request.description
    # product.save()
    return render(request, 'Products/change_product.html', {'product': product})

