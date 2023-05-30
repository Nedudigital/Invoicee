from django.shortcuts import render
from . models import product, buyer, seller
import datetime
# Create your views here.
def index(request):
    products = product.objects.all()
    sell = seller.objects.all()
    return render(request, 'index.html', {'products': products, 'seller': sell})


def buy(request,pk):
    print(pk)
    products = product.objects.get(pk=pk)
    

    if request.method == "POST":
        name = request.POST['name']
        address = request.POST['address']
        phone = request.POST['phone']
        quantity = int(request.POST['quantity'])

        buy = buyer(name=name, address=address,phone=phone)
        buy.save()
        amount = float(product.price)
        product_name = products.name
        description = product.description
        price = amount
        product_quantity = quantity
        product_total = amount*quantity
        sell = seller.objects.all()
        data = {'product_name': product_name, 'product_price': price,'buyer_name':name,'buyer_address':address,'buyer_phone':phone,'product_description':description,'product_quantity':product_quantity, 'product_total':product_total}
        return render(request, 'pdf.html', {'data': data, 'seller': sell})
    return render(request, 'buy.html')


def pdf(request):
    sell = seller.objects.all()
    return render(request, 'pdf.html', {'seller': seller})