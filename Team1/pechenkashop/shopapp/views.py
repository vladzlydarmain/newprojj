from django.shortcuts import render
from .models import *

# Create your views here.

def show_main(request):
    products = Product.objects.all()
    context = {
        'products':products
    }

    response = render(request,"shopapp/index.html", context=context)

    if request.method == "POST":
        article = request.POST["article"]
        amount = request.POST["amount"]
        if "products" in request.COOKIES:
            old_products = request.COOKIES["products"]
            list_old_products = old_products.split(' ')
            for product in list_old_products:
                a = product.split(":")
                if a[0] == article:
                    return response
            new_products = f"{article}:{amount}" + " " + old_products
            response.set_cookie("products",new_products)
        else:
            response.set_cookie("products",f"{article}:{amount}")

    
    return response

def show_basket(request):
    models_list = []
    cookie = ''
    new_cookie = ""
    response = render(request, "shopapp/basket.html")
    if "products" in request.COOKIES:
        products = request.COOKIES["products"]
        list_products = products.split(" ")
        model_products = []
        models_list = []
        for product in list_products:
            a = product.split(":")
            model_products.append(Product.objects.get(pk = a[0]))
            model_products.append(a[1])
            models_list.append(model_products)
            
        # cookie = ''
        if request.method == "POST":
            id_del = request.POST.get('cross')
            # new_cookie = ""
            # cookie = ''
            # for i in models_list:
            #     print(id_del)
            #     print(i[0].pk)
            #     if int(i[0].pk) == int(id_del):
            #         print(i)
            #         models_list.remove(i)
            #         print(models_list)
            #         continue
                
            response.set_cookie("products",new_cookie)   


    context = {
        "products": models_list
    }
    response.context = context
    print(models_list)

    return response

