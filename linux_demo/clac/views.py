from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse,HttpResponseRedirect

from django.shortcuts import render,reverse

def index(request):
    return render(request,'home.html')

def add(request):
    a = request.GET['a']
    b = request.GET['b']
    c = int(a)+int(b)
    return HttpResponse(str(c))

def add2(request,a,b):
    return HttpResponse(str(int(a)+int(b)))

def old_add2_redirect(request, a, b):
    return HttpResponseRedirect(
        reverse('add2', args=(a, b))
    )