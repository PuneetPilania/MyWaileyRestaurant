from django.urls import path
from . views import HomeView, LocationView, RestaurantView, MenuView, CartView, PlaceOrder
from . import views

urlpatterns=[
	path('',HomeView.as_view(),name='home'),
	path('location/',LocationView.as_view(),name='city'),
	path('location/<int:pk>/',RestaurantView.as_view(),name='restaurant'),
	path('location/rpage/<int:id>/',MenuView.as_view(),name='menu'),
	path('cart/',CartView.as_view(),name="cart"),
	path('search/',views.search,name='Search'),
	path('placeOrder/',PlaceOrder.as_view(),name='placeOrder'),
]