from django.shortcuts import render

# create your views here.
def home(request):
    return render(request, 'blog/home.html',{'title':'Djangoblog Homepage.'})

def about(request):
    return render(request, 'blog/about.html',{'content':'Dandoblog teams.'})

def contact(request):
    return render(request, 'blog/contact.html', {'abc': 'Welcome to the Djangoblog contact page!'
    })

