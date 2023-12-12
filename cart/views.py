from django.shortcuts import render,redirect,get_object_or_404
from shop . models import *
from . models import *
from django.core.exceptions import ObjectDoesNotExist

# Create your views here.
def cart_details(request,total=0,count=0,cart_items=None):
    try:
        crt= cartlist.objects.get(cart_id=c_id(request))
        crt_items=items.objects.filter(cart=crt, active=True)
        for i in crt_items:
            total += (i.product.price * i.quantity)
            count += i.quantity
    except ObjectDoesNotExist:
        pass
    return render(request, 'cart.html', {'crt_itm':crt_items, 'tot':total, 'cont':count})

def c_id(request):
    crt_id=request.session.session_key
    if not crt_id:
        crt_id=request.session.create()
    return crt_id

def add_cart(request, product_id):
    prod=Products.objects.get(id=product_id)
    try:
        crt=cartlist.objects.get(cart_id=c_id(request))
    except cartlist.DoesNotExist:
        crt=cartlist.objects.create(cart_id=c_id(request))
        crt.save()

    try:
        c_items=items.objects.get(product=prod, cart=crt)
        if c_items.quantity < c_items.product.stock:
            c_items.quantity+=1
        c_items.save()
    except items.DoesNotExist:
        c_items=items.objects.create(product=prod,quantity=1,cart=crt)
        c_items.save()
    return redirect('cartDetails')



def min_cart(request, product_id):
    crt=cartlist.objects.get(cart_id=c_id(request))
    prodt=get_object_or_404(Products,id=product_id)
    c_items=items.objects.get(product=prodt,cart=crt)
    # for decrement
    if c_items.quantity > 1:
        c_items.quantity -= 1
        c_items.save()
    else:
        c_items.delete()
    return redirect('cartDetails')

def cart_delete(request,product_id):
    crt = cartlist.objects.get(cart_id=c_id(request))
    prodt = get_object_or_404(Products, id=product_id)
    c_items = items.objects.get(product=prodt, cart=crt)

    c_items.delete()
    return redirect('cartDetails')


