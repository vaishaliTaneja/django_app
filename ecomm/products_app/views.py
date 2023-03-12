import base64
from django.shortcuts import render, redirect
from .models import Products
from .forms import ProductCreate
from django.http import HttpResponse
from base64 import b64encode

#DataFlair
def index(request):
    shelf = Products.objects.all()
    products = []
    for product in shelf:
        temp = {
            "productid": product.productid,
            "image": b64encode(product.image).decode("utf-8"),
            "price": product.price,
            "productname": product.productname,
            "productdec" : product.productdec,
            "quantity": product.quantity
        }
        products.append(temp)
    return render(request, 'list.html', {'shelf': products})

# def upload(request):
#     upload = BookCreate()
#     if request.method == 'POST':
#         upload = BookCreate(request.POST, request.FILES)
#         if upload.is_valid():
#             upload.save()
#             return redirect('index')
#         else:
#             return HttpResponse("""your form is wrong, reload on <a href = "{{ url : 'index'}}">reload</a>""")
#     else:
#         return render(request, 'upload_form.html', {'upload_form':upload})

def update_product(request, product_id):
    product_id = int(product_id)
    product = Products.objects.get(productid = product_id)
    product_values = ProductCreate(request.POST or None, instance = product)
    productDetails= {
        "name": product_values.productname
    }
    if product_values.is_valid():
       product_values.save()
       return redirect('index')
    return render(request, 'update_create.html', {'upload_form':productDetails})

def remove_product(request, product_id):
    product_id = int(product_id)
    product = Products.objects.get(productid = product_id)
    product.delete()
    return redirect('index')