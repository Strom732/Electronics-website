from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Product, CartItem
from django.db.models import Sum
from django.contrib import messages

def product_list(request):
    products = Product.objects.all()
    return render(request, '../Pages/index.html', {'products': products})
 
def view_cart(request):
    cart_items = CartItem.objects.filter(user=request.user)
    total_price = sum(item.product.price * item.quantity for item in cart_items)
    return render(request, '../Pages/cart.html', {'cart_items': cart_items, 'total_price': total_price})
 
def add_to_cart(request, product_id):
    user = request.user
    product = get_object_or_404(Product, id=product_id)
    cart_item, created = CartItem.objects.get_or_create(product=product, user=user)
    cart_item.quantity += 1
    cart_item.save()
    
    # Add a success message
    messages.success(request, 'Item added to cart!')
    
    # Redirect back to the home page
    return redirect('home')
 
def remove_one_from_cart(request, item_id):
    cart_item = get_object_or_404(CartItem, id=item_id)

    if cart_item.quantity > 1:
        cart_item.quantity -= 1
        cart_item.save()
    else:
        cart_item.delete()
    
    messages.success(request, 'Cart Updated')    

    return redirect('cart:view_cart')

def remove_all_from_cart(request, item_id):
    cart_item = get_object_or_404(CartItem, id=item_id)
    cart_item.delete()
    messages.success(request, 'Cart Updated')

    return redirect('cart:view_cart')
 
def view_cart(request):
    cart_items = CartItem.objects.filter(user=request.user).order_by('id')  # Order by id to maintain the order
    total_price = sum(item.product.price * item.quantity for item in cart_items)
    cart_items_count = cart_items.aggregate(Sum('quantity'))['quantity__sum'] or 0
    item_total = [(item, item.product.price * item.quantity) for item in cart_items]
    for item in cart_items:
        item.total = item.quantity * item.product.price
    context = {
        'cart_items': cart_items,
        'total_price': total_price,
        'cart_items_count': cart_items_count,
    }

    return render(request, '../Pages/cart.html', context)

def add_one_to_cart(request, item_id):
    cart_item = get_object_or_404(CartItem, id=item_id)
    cart_item.quantity += 1
    cart_item.save()
    messages.success(request, 'Cart Updated')

    return redirect('cart:view_cart')
