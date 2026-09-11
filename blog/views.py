from django.shortcuts import render

# create your views here.
def home(request):
    return render(request, 'blog/home.html',{'title':'Djangoblog Homepage.'})

def about(request):
    return render(request, 'blog/about.html',{'content':'Dandoblog teams.'})

def content(request):
    return render(request, 'blog/content.html', {'abc': 'Welcome to the Djangoblog content page!'
    })