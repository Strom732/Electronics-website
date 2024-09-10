# shop/views.py
from django.shortcuts import render

def shop_view(request):
    # Add your logic here, for example fetching products from the database
    return render(request, 'shop.html')
    
from django.shortcuts import render
from products.models import Product, Category
from django.core.paginator import Paginator
from django.db.models import Q

def shop_view(request):
    query = request.GET.get('query', '')
    category_id = request.GET.get('category', '')
    sort_by = request.GET.get('sort_by', '')

    # Fetch all products initially
    products = Product.objects.all()

    # Filter by search query if provided
    if query:
        products = products.filter(
            Q(name__icontains=query) | Q(description__icontains=query)
        )

    # Filter by category only if a category is selected (not "All")
    if category_id and category_id != 'all':
        products = products.filter(category__id=category_id)

    # Sorting logic
    if sort_by == 'popularity':
        products = products.order_by('-popularity')
    elif sort_by == 'newest':
        products = products.order_by('-id')
    elif sort_by == 'price':
        products = products.order_by('price')

    # Pagination
    paginator = Paginator(products, 12)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    categories = Category.objects.all()

    context = {
        'products': page_obj,
        'categories': categories,
        'selected_category': category_id,  # Pass selected category to the template
    }

    return render(request, 'shop.html', context)
