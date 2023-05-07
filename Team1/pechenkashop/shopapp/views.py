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
    new_cookie = ""
    if "products" in request.COOKIES:
        products = request.COOKIES["products"]
        list_products = products.split(" ")
        for product in list_products:
            model_products = []
            a = product.split(":")
            model_products.append(Product.objects.get(pk = a[0]))
            model_products.append(a[1])
            print("prod",model_products)
            models_list.append(model_products)
            print("models-list",models_list)

    context = {
        "products": models_list
    }
    response = render(request, "shopapp/basket.html",context=context)
        
    if request.method == "POST":
        id_del = request.POST.get('cross')
        if "products" in request.COOKIES:
            cookies = request.COOKIES["products"].split(' ')
            print(id_del)
            for i in models_list:
                if i[0].pk == int(id_del):
                    print(i)
                    models_list.remove(i)
                    for prod_cookie in cookies:
                        prod_info = prod_cookie.split(":")
                        if prod_info[0] == str(i[0].pk):
                            cookies.remove(prod_cookie)
                            print(cookies)
                    continue
                
            for cookie in cookies:
                new_cookie += cookie
                print("new_cookie -------",new_cookie)
            if new_cookie != '':
                print("----------------------------------------")
                response.set_cookie("products",new_cookie)
                return response
            else:
                print("----------------1111111111111-------------------")
                response.delete_cookie("products")
                return response



    return response

