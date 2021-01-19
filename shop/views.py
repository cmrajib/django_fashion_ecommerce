from decimal import Decimal

from django.core.paginator import Paginator
from django.db.models import Q
from django.shortcuts import render, get_object_or_404

# Create your views here.
from shop.models import Product, Category, Subcategory, Brand


def product(request, subcategory_id=None):
    categories = Category.objects.all()
    subcategories = Subcategory.objects.all()
    products = Product.objects.all()[:6]

    deals = Product.objects.filter(deals_of_the_week=True)


    # products = Product.objects.filter(discountprice__lte=0.0)
    # latestproduct = Product.objects.all().order_by('DateArrived').filter(discountprice__lte=0.0)[:3]
    # discountproduct = Product.objects.filter(discountprice__gte=0.1)



    # search by category
    subcategory=False
    if subcategory_id:
        products = Product.objects.filter(subcategory=subcategory_id)
        # subcategories = Subcategory.objects.filter(subcategory=subcategory_id)
        subcategory = True




    # search by name
    # search = ''
    # if 'search' in request.GET:
    #     search = request.GET['search']
    #     if search:
    #         products = products.filter(title__icontains=search)






    # pagination
    paginator = Paginator(products, 1)
    page = request.GET.get('page')
    paged_product = paginator.get_page(page)

    context = {

        'categories': categories,
        'subcategories': subcategories,
        'products': paged_product,
        'subcategory': subcategory,
        'deals': deals,

    }

    return render(request, 'shop/product.html', context)


def productdetail(request, id):

    product = Product.objects.get(id=id)


    context = {
        'product': product,
    }


    return render(request,'shop/productdetail.html', context)
