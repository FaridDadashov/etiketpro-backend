from django.shortcuts import render,redirect
from . models import Product,ProductImage,OurProduct,Projects,Friends
from .forms import ContactForm,RegisterForm
from django.contrib.auth import login,authenticate
# Create your views here.
def home(request):
    products=Product.objects.all()
    product_images=ProductImage.objects.all()
    ourproducts=OurProduct.objects.all()
    projects=Projects.objects.all()
    friends=Friends.objects.all()
    context = {
        'products': products,
        'product_images': product_images,
        'ourproducts':ourproducts,
        'projects':projects,
        'friends':friends
    }
    return render(request,'home.html',context)


def contact(request):
    form=ContactForm()
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'contact.html', {'form': form, 'result': 'success'})
        return render(request, 'contact.html', {'form': form, 'result': 'fail'})
    return render(request, 'contact.html', {'form': form})



def detail(request):
    ourproducts=OurProduct.objects.all()
    context={
        'ourproducts':ourproducts
    }
    return render(request,'detail.html',context)


def products(request):
    ourproducts=OurProduct.objects.all()
    context={
        'ourproducts':ourproducts
    }
    
    return render(request,'products.html',context)


def register(request):
    form=RegisterForm()
    if request.method=='POST':
        form=RegisterForm(request.POST)
        if form.is_valid():
            customer=form.save()
            login(request, customer.user)  
            return redirect('shop:login')
    return render(request,'register.html',{'form':form})




def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password) 
        if user:
                login(request,user)
                return redirect('shop:home')
        return render(request,'login.html',{'fail':True})
    return render(request,'login.html',{})