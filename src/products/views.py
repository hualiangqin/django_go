from django.shortcuts import render, get_object_or_404, redirect

from .models import Product
from .forms import ProductForm, RawProductForm
# Create your views here.

def product_update_view(request, id):
    obj = get_object_or_404(Product, id=id)
    form = ProductForm(request.POST or None, instance=obj)
    if form.is_valid():
        form.save()
    context = {
        "form": form
    }
    return render(request, "products/product_create.html", context)

def render_initial_data(request):   # modified the first object
    initial_data = {
        'title': "This is my awsome title"
    }
    obj = Product.objects.get(id=1)
    # form = ProductForm(request.POST or None, initial=initial_data ,instance=obj)
    form = ProductForm(request.POST or None, instance=obj)
    if form.is_valid():
        form.save()
    context = {
        "form": form
    }
    return render(request, "products/product_create.html", context)

def product_lookup_view(request):
    title = request.POST.get("title")
    print(title)
    context = {}
    return render(request, "products/product_lookup.html", context)

def product_delete_view(request, id):
    obj = get_object_or_404(Product, id=id)
    if request.method == "POST":
        obj.delete()
        # redirect("../../")
    context = {
        "object": obj
    }
    return render(request, "products/product_delete.html", context)

# def product_create_view(request):
#     form = RawProductForm()
#     if request.method == "POST":
#         form = RawProductForm(request.POST)
#         if form.is_valid():
#             print(form.cleaned_data)
#             Product.objects.create(**form.cleaned_data)
#         else:
#             print(form.errors)
#     context = {
#         "form": form
#     }
#     return render(request, "products/product_create.html", context)

def product_create_view(request):
    # form = ProductForm(request.POST or None)
    form = RawProductForm(request.POST or None)
    if form.is_valid():
        # form.save()     # save is for formModel only
        # form = ProductForm()
        Product.objects.create(**form.cleaned_data)

    context = {
        "form": form
    }
    # here it will go to the templates in src first to look for this template
    return render(request, "products/product_create.html", context)

def product_detail_view(request, id):
    obj = Product.objects.get(id=id)
    context = {
        # "title": obj.title,
        # "description": obj.description
        "object": obj
    }
    # here it will go to the templates in src first to look for this template
    return render(request, "products/product_detail.html", context)

def product_list_view(request):
    queryset = Product.objects.all()
    context = {
        "object_list": queryset
    }
    return render(request, "products/product_list.html", context)