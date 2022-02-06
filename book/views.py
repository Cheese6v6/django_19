from django.shortcuts import render, redirect
from .models import Book
from django.utils import timezone


# Create your views here.

def delete(request, bpk):
    b = Book.objects.get(id=bpk)
    if b.user == request.user:
        b.delete()
    else:
        pass    #20일차
    return redirect('book:index')

def create(request):
    if request.method == "POST":
        n = request.POST.get('name')
        u = request.POST.get('url')
        c = request.POST.get('con')
        im = request.POST.get('impo')
        # print(n,u,c,im)
        if n and u and c:
            if im:
                im = True
            else:
                im = False
            Book(user=request.user, site_name=n, site_url=u, content=c, pubdate=timezone.now(), impo=im).save()
            return redirect("book:index")
    return render(request, 'book/create.html')

def index(request):
    b = request.user.book_set.all().order_by("-pubdate")
    
    context = {
        'blist' : b,
    }
    return render(request, 'book/index.html', context)