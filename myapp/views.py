from django.shortcuts import render
from.models import Content

def index(request):
    contents = Content.objects.all()
    return render(request,'index.html',{'contents':contents})

