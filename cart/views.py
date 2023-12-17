from django.shortcuts import get_object_or_404, redirect, render
from cart.models import Cart, CartItem
from shop.models import Shop

# Create your views here.
def _cart_id(request) :
    cart = request.session.session_key
    if not cart :
        cart = request.session.create()
    return cart

def add_cart(request, shop_id) :
    shop = Shop.objects.get(id=shop_id)
    try :
        cart = Cart.objects.get(cart_id = _cart_id(request))
    except Cart.DoesNotExist :
        cart = Cart.objects.create(
            cart_id = _cart_id(request)
        )
        cart.save()

    try :
        cart_item = CartItem.objects.get(shop = shop, cart = cart)
        cart_item.quantity += 1
        cart_item.save()
    except CartItem.DoesNotExist :
        cart_item = CartItem.objects.create(
            shop = shop,
            quantity = 1,
            cart = cart
        )
        cart_item.save()
    
    return redirect('cart:cart_detail')

def cart_detail(request, total = 0, counter = 0, cart_items = None) :
    try :
        cart = Cart.objects.get(cart_id = _cart_id(request))
        cart_items = CartItem.objects.filter(cart = cart, active = True)
        for cart_item in cart_items :
            total += (cart_item.shop.price * cart_item.quantity)
            counter += cart_item.quantity
    except Cart.DoesNotExist :
        pass
    except CartItem.DoesNotExist :
        pass 

    return render(request, 'cart.html', dict(cart_items = cart_items, total=total, counter=counter))

def cart_remove(request, shop_id) :
    cart = Cart.objects.get(cart_id = _cart_id(request))
    shop = get_object_or_404(Shop, id = shop_id)
    cart_item = CartItem.objects.get(shop = shop, cart = cart)

    if cart_item.quantity > 1 :
        cart_item.quantity -= 1
        cart_item.save()
    else :
        cart_item.delete()
    
    return redirect('cart:cart_detail')

