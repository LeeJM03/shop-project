from django.shortcuts import render
#from django.http import HttpResponse
from .models import Shop
# Create your views here.

def index(request) :
    shop_list = Shop.objects.all
    context = {'shop_list' : shop_list}
 #  return HttpResponse("Shop index page.")
    return render(request, 'shop_list.html', context)

def detail(request, shop_id):
  shop = Shop.objects.get(id=shop_id)
  context = {'shop': shop}
  return render(request, 'shop_detail.html', context)
