from django.shortcuts import render, redirect
from .models import Book
from django.contrib import messages

# Create your views here.



def create(request):
    if request.method == "POST":
        sn = request.POST.get("sname")
        sc = request.POST.get("scon")
        su = request.POST.get("surl")
        im = bool(request.POST.get("impo"))
        Book(site_name=sn,site_con=sc,site_url=su,impo=im,user=request.user).save()
        return redirect("book:index")
    return render(request,"book/create.html")

def index(request):
    b = request.user.book_set.all()

    context = {
        'bset' : b
    }
    return render(request,"book/index.html", context)

def delete(request,bpk):
    b = request.user.book_set.get(id=bpk)
    if request.user == b.user:
        b.delete()
    else:
        messages.error(request,"접근 금지")
    return redirect("book:index")

def update(request, bpk):
    b = request.user.book_set.get(id=bpk)

    if request.user != b.user:
        return redirect("book:index")
        
    if request.method == "POST":
        sn = request.POST.get("sname")
        sc = request.POST.get("scon")
        su = request.POST.get("surl")
        im = bool(request.POST.get("impo"))
        b.site_name, b.site_url, b.site_con, b.impo  = sn, su, sc, im
        b.save()
        return redirect("book:index")
    context = {
        "b" :b
    }
    return render(request, "book/update.html", context)