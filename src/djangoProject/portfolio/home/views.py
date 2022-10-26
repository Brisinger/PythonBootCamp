from unicodedata import name
from django.shortcuts import render, HttpResponse
from .models import Contact


# Create your views here.
def home(request):
    return render(request, template_name='index.html')

def about(request):
    # return HttpResponse('about')
    return render(request, template_name='about.html')

def contact(request):
    # return HttpResponse('contact')
    if request.method == "POST":
        name = request.POST['name']
        phone = request.POST.get('phone', "Not available")
        email = request.POST.get('email', None)
        message = request.POST.get('message', None)
        # Creating Contact model instance
        contact = Contact(name=name, phone=phone, email=email, message=message)
        # Saving the model instance into database
        contact.save()
    return render(request, template_name='contact.html')