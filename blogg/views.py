from django.shortcuts import render

from . models import Post

# Create your views here.
def home(request):
    data = {
        "posts":Post.objects.all()
    }
    return render(request,'home.html',data)