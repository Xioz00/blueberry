from .models import *
from django.db.models import Q
from django.core.paginator import Paginator,EmptyPage,InvalidPage
from django.core.exceptions import ObjectDoesNotExist

# Create your views here.

from django.shortcuts import render, get_object_or_404

def home(request, c_slug=None):
    c_page = None
    product_list= None
    if c_slug!=None:
        c_page = get_object_or_404(Category, slug=c_slug)
        product_list = Products.objects.filter(cat=c_page, available=True)
    else:
        product_list = Products.objects.filter(available=True)

        cat = Category.objects.all()

        paginator=Paginator(product_list,4)
    try:
        page=(request.GET.get('page', '1'))
    except ValueError:
        page=1
    try :
        products = paginator.page(page)

    except (EmptyPage,InvalidPage):
        products = paginator.page(paginator.num_pages)

    return render(request, 'home.html', {'pr': products, 'ct': cat})

def prodDetails(request,c_slug,Products_slug):
    try:
        prod=Products.objects.get(cat__slug=c_slug,slug=Products_slug)
    except Exception as e:
        raise e
    return render(request, 'detail.html',{'pr': prod})

def searching(request):
    prod=None
    query=None
    if 'q' in request.GET:
        query = request.GET.get('q')
        prod = Products.objects.all().filter(Q(name__contains=query) | Q (description__contains=query))
    return render (request ,'search.html', {'qr':query,'pr':prod})

def cart(request):
    return render(request,'cart.html')

def accounts(request):
    return render(request,'accounts.html')


