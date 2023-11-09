from django.shortcuts import render,redirect
from .forms import ContactForm
from urllib.parse import quote
from django.http import HttpResponse


# Create your views here.


def index(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            
            return redirect('web:index')  
    else:
        form = ContactForm()
    
    return render(request, 'web/index.html', {'form': form})


