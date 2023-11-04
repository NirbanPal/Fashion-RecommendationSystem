app_name = "ecom_recoapp"
from django.urls import path,reverse_lazy
from ecom_recoapp import views
# from django.conf import settings
# from django.conf.urls.static import static

urlpatterns = [
    # path('', views.home),
    # path('',views.ProductView.as_view(),name = "home"),
    # path('product-detail/<int:pk>', views.ProductDetailView.as_view(), name='product-detail'),
    # path('minuscart/', views.minus_cart, name='plus_cart'),

    path('', views.index_page, name='index'),
    path('product-detail/<int:id>', views.productdetails, name='product-detail'),
    path('add-to-cart/<int:id>', views.add_to_cart, name='add-to-cart'),
    path('cart/', views.showcart, name='showcart'),
    

]

