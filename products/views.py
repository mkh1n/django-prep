from django.shortcuts import render, redirect, get_object_or_404
from .models import Product, Supplier
from .forms import ProductForm

def product_list(request):
    products = Product.objects.all()
    suppliers = Supplier.objects.all()

    return render(request, 'products/product_list.html', {'products': products, 'suppliers': suppliers})

def product_add(request):
    if not request.user.is_admin_user:
        return redirect('products:product_list')
   
    if request.method == 'POST':
        form = ProductForm()
        if form.is_valid():
            form.save()
            return redirect('products:product_list')
    else:
        form = ProductForm()
    return render(request, 'products/product_form.html', {'form': form, 'title': 'Добавление товара'})

def product_edit(request, pk):
    if not request.user.is_admin_user:
        return redirect('products:product_list')
    
    product = get_object_or_404(Product, pk=pk)

    if request.method == 'POST':
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            return redirect('products:product_list')
    else:
        form = ProductForm(instance=product)
    return render(request, 'products/product_form.html', {'form': form, 'title': 'Редактирование товара'})\
    

def product_delete(request, pk):
    if not request.user.is_admin_user:
        return redirect('products:product_list')
    
    product = get_object_or_404(Product, pk=pk)

    if request.method == 'POST':
        product.delete()
        return redirect('products:product_list')

    return render(request, 'products/product_confirm_delete.html', {'product': product})