from django.shortcuts import render
from .models import Product, Category
from cart.models import CartItem
from django.db.models import Sum
from django.contrib.auth.decorators import login_required

def home(request):
    products = Product.objects.all()
    categories = Category.objects.all().order_by('name')

    context = {
        'Products': products,  # Consider renaming this to 'products' for consistency
        'categories': categories
    }

    if request.user.is_authenticated:
        cart_item_count = CartItem.objects.filter(user=request.user).aggregate(Sum('quantity'))['quantity__sum'] or 0
        context['cart_item_count'] = cart_item_count

    return render(request, 'index.html', context)

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')
