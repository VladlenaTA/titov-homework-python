from django.shortcuts import get_object_or_404, render
from .models import Category, Product
from .forms import ProductForm
from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect


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
    if request.method == "POST":
        product = Product.objects.get(id=id)
        product_form = ProductForm(instance=product, data=request.POST)
        if product_form.is_valid():
            product_form.save()
            return render(request, 'Products/change_product.html', {'product': product})
    else:
        product = Product.objects.get(id=id)
    return render(request, 'Products/change_product.html', {'product': product})

def delete_product(request, id):
    product = Product.objects.get(id=id)
    print(product.title)
    product.delete()
    return all_products(request)
