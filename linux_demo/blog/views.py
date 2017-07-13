from django.shortcuts import render

# Create your views here.
def index(reuqest):
    return render(reuqest, 'blog/index.html')


def columns(request):
    return render(request, 'blog/columns.html')