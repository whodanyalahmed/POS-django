from django.urls import path
from .views import Home,products,sells,ProductCreateView,ProductUpdateView

urlpatterns = [
    path('',Home,name='home'),
    path('products',products,name='products'),
    path('sells',sells,name="sells"),
    path("product/add",ProductCreateView.as_view(),name="addproduct"),
    path('product/<int:pk>/edit/',ProductUpdateView.as_view(),name="updateproduct")
    

]