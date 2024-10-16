from django.urls import path
from . import views

app_name='shop'

urlpatterns = [
    path('',views.home,name='home'),
    path('contact/',views.contact,name='contact'),
    path('detail/',views.detail,name='detail'),
    path('products/',views.products,name='products'),
    path('register/',views.register,name='register'),
    path('login/',views.login_view,name='login')
]
