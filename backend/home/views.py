from django.shortcuts import render
from .models import Certificate

# Create your views here.
def about(request):
    certificates=Certificate.objects.all()
    context={
        'certificates':certificates
    }
    return render (request,'about.html',context)