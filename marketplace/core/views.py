from django.shortcuts import redirect, render
from item.models import Category , Item


from .forms import SignupForm
# Create your views here.

def index(request):
    items=Item.objects.all()
    categories=Category.objects.all()
    return render(request,'core/index.html',{
        'categories':categories,
        'items':items,
    })


def Signup (request):
    if request.method=='POST':
        form=SignupForm(request.POST)

        if form.is_valid():
            form.save()

            return redirect('/login/')
    else:
       form=SignupForm()
    return render  (request,'core/signup.html',{
        'form':form
    } )
from django.contrib.auth import logout


def logout_view(request):
    logout(request)
    return redirect ('/')