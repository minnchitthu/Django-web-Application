from django.urls import path
from . import views

urlpatterns = [
    path('',views.dashboard,name='dashboard'),
    path('customers/<int:id>',views.customers,name='customer.show'),
    path('order/update/<int:orderId>',views.orderUpdate,name='order.update'),
    path('products/',views.products,name='product'),
    path('order/create/<int:customerId>',views.orderCreate,name='order.create'),
    path('order/delete/<int:orderId>',views.orderDelete,name='order.delete'),
    path('register/',views.register,name='register'),
    path('login/',views.userLogin,name='login'),
    path('logout/',views.userLogout,name='logout'),
    path('customer_profile/',views.customer_profile,name='customer.customer_profile'),
    path('customer_profile/setting/',views.customer_profile_setting,name='customer.customer_profile_setting'),
]
