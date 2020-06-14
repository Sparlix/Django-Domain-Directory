from django.shortcuts import render
from .models import Domain
from .models import Contact


def home(request):
    domain = Domain.objects
    return render(request, 'home.html', {'domain': domain})

def contact(request):
    contact = Contact.objects
    return render(request,'contact.html', {'contact': contact})
# Create your views here.
