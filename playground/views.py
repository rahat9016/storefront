from django.shortcuts import render
from store.models import Product, OrderItem
from django.http import HttpResponse
from django.core.exceptions import ObjectDoesNotExist
from django.db.models import Q, F
# Create your views here.
def say_hello(request):
    
    # gt = Product.objects.filter(Q(unit_price__gt=20) & ~Q(title__icontains='Mustard'))
    # gt = Product.objects.filter(inventory=F('unit_price'))
    # products = Product.objects.order_by('-unit_price', '-title')
    # product = Product.objects.earliest('unit_price')
    # products = Product.objects.all()[5:15]
    orders = OrderItem.objects.filter(id__in=OrderItem.objects.values('product__id').distinct())
    
    products = Product.objects.filter(title__icontains='ss').filter(Q(unit_price__gt=20)).values_list("id", 'title', 'collection__title')
    count = products.count()
    # print(gt)
    
    return render(request, 'index.html', {'products': list(products), 'count':count, 'orders': orders})