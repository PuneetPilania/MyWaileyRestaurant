from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import TemplateView,ListView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Location, Restaurant, Menu, Orders
from math import ceil


class HomeView(TemplateView):
	template_name='myapp/home.html'


# for all locations
class LocationView(ListView):
	model=Location
	context_object_name='location'


# search
def searchMatch(query, item):
    '''return true only if query matches the item'''
    if query in item.loc.lower():
        return True
    else:
        return False

def search(request):
    query = request.GET.get('search')
    allCity = []

    city=Location.objects.all()
    
    prod = [item for item in city if searchMatch(query, item)]
    n = len(prod)
    nSlides = n // 4 + ceil((n / 4) - (n // 4))
    if len(prod) != 0:
    	allCity.append([prod, range(1, nSlides), nSlides])
    context = {'location': allCity, "msg": ""}
    if len(allCity) == 0 or len(query)<2:
        context = {'msg': "Please make sure to enter relevant search query"}
    return render(request, 'myapp/search.html', context)


class RestaurantView(ListView):
    model=Restaurant
    context_object_name='restaurant'

    def get_context_data(self, **kwargs):
        context=super(RestaurantView, self).get_context_data(**kwargs)
        pk=self.kwargs['pk']
        context['location']=Location.objects.get(id=pk)
        context['restaurant']=Restaurant.objects.filter(location=pk)
        return context




class MenuView(ListView):
    model=Menu
    context_object_name='menu'

    def get_context_data(self, **kwargs):
        context=super(MenuView, self).get_context_data(**kwargs)
        pk=self.kwargs['id']
        context['restaurant']=Restaurant.objects.get(id=pk)
        context['menu']=Menu.objects.filter(restaurant=pk)
        return context


class CartView(LoginRequiredMixin,TemplateView):
    model=Restaurant
    template_name="myapp/cartView.html"


class PlaceOrder(LoginRequiredMixin,CreateView):
    model=Orders
    template_name='myapp/placeOrder.html'
    fields=['item_json','amount','name','email','address','city','state','zip_code','phone']
    success_url='/'

    def form_valid(self, form):
        form.save()
        return HttpResponseRedirect("/")



    

