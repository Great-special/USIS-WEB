from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required, user_passes_test
from .models import Product, OrderItem
from .forms import ProductForm, OrderForm


# Create your views here.

def is_allowed(user):
    if user.is_superuser:
        return True
   


@login_required(login_url='user-login')
def index(request):
    products = Product.objects.all()
    product_count = products.count()
    orders = OrderItem.objects.all()
    order_count = orders.count()
    customer = User.objects.filter(groups=1)
    customer_count = customer.count()


    if request.method == 'POST':
        prd_name = request.POST.get('product_name')
        product = Product.objects.filter(name=prd_name).first()
        print(product)
        context = {
            'orders': orders,
            'products': products,
            'product':product,
            'product_count': product_count,
            'order_count': order_count,
            'customer_count': customer_count,
        }
        
        return render(request, 'store/index.html', context)
    else:
        form = OrderForm()
    
        
    context = {
        'form': form,
        'orders': orders,
        'products': products,
        'product_count': product_count,
        'order_count': order_count,
        'customer_count': customer_count,

    }
    return render(request, 'store/index.html', context)


@login_required(login_url='user-login')
def product_order(request, pk):
    products = Product.objects.all()
    product_count = products.count()
    orders = OrderItem.objects.all()
    order_count = orders.count()
    customer = User.objects.filter(groups=1)
    customer_count = customer.count()

    product = Product.objects.filter(id=pk).first()

    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            if product.quantity < obj.order_quantity:
                messages.error(request, f'{product.name} quantity is insufficient, available qty: {product.quantity}')
                return redirect('product-order')
            else:
                new_qty = product.quantity - obj.order_quantity
                obj.seller_id = request.user
                obj.product = product
                obj.order_price = product.price
                obj.total_price = product.price * obj.order_quantity
                obj.save()
                # updating product quantity
                product.quantity = new_qty
                product.save()
    else:
        form = OrderForm()
        
    context = {
        'form': form,
        'orders': orders,
        'products': products,
        'product':product,
        'product_count': product_count,
        'order_count': order_count,
        'customer_count': customer_count,

    }
    return render(request, 'store/customer_index.html', context)

@login_required(login_url='user-login')
@user_passes_test(is_allowed)
def products(request):
    product = Product.objects.all()
    product_count = product.count()
    orders = OrderItem.objects.all()
    order_count = orders.count()
    customer = User.objects.filter(groups=1)
    customer_count = customer.count()
    
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            prd = form.save(commit=False)
            prd.name = prd.name.lower()
            prd.save()
            product_name = form.cleaned_data.get('name')
            messages.success(request, f'{product_name} has been added')
            return redirect('store-products')
    else:
        form = ProductForm()
    
    context = {
        'product': product,
        'form': form,
        'product_count': product_count,
        'order_count': order_count,
        'customer_count': customer_count,
    }
    return render(request, 'store/products.html', context)

@login_required(login_url='user-login')
@user_passes_test(is_allowed)
def product_edit(request, pk):
    item = Product.objects.get(id=pk)
    if request.method == 'POST':
        form = ProductForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect('store-products')
    else:
        form = ProductForm(instance=item)
        
    context = {
        'form': form,
    }
    return render(request, 'store/products_edit.html', context)


@login_required(login_url='user-login')
@user_passes_test(is_allowed)
def product_detail(request, pk):
    product = Product.objects.get(id=pk)
    context = {
        'product': product,
    }
    return render(request, 'store/products_detail.html', context)


@login_required(login_url='user-login')
@user_passes_test(is_allowed)
def product_delete(request, pk):
    item = Product.objects.get(id=pk)
    if request.method == 'POST':
        item.delete()
        return redirect('store-products')
    context = {
        'item': item
    }
    return render(request, 'store/products_delete.html', context)

@login_required(login_url='user-login')
@user_passes_test(is_allowed)
def order(request):
    orders = OrderItem.objects.all()
    order_count = orders.count()
    customer = User.objects.filter(groups=1).all()
    customer_count = customer.count()
    product = Product.objects.all()
    product_count = product.count()
    
    context = {
        'orders': orders,
        'customer_count': customer_count,
        'product_count': product_count,
        'order_count': order_count,
    }
    return render(request, 'store/order.html', context)

@login_required(login_url='user-login')
@user_passes_test(is_allowed)
def customers(request):
    customers = User.objects.filter(groups=1)
    customer_count = customers.count()
    product = Product.objects.all()
    product_count = product.count()
    order = OrderItem.objects.all()
    order_count = order.count()
    context = {
        'customers': customers,
        'customer_count': customer_count,
        'product_count': product_count,
        'order_count': order_count,
    }
    return render(request, 'store/customers.html', context)

@login_required(login_url='user-login')
@user_passes_test(is_allowed)
def customer_detail(request, pk):
    customer = User.objects.filter(groups=1)
    customer_count = customer.count()
    product = Product.objects.all()
    product_count = product.count()
    order = OrderItem.objects.all()
    order_count = order.count()
    customers = User.objects.get(id=pk)
    context = {
        'customers': customers,
        'customer_count': customer_count,
        'product_count': product_count,
        'order_count': order_count,

    }
    return render(request, 'store/customers_detail.html', context)

