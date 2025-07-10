from django.shortcuts import render, HttpResponse
from myapp.models import Contact
from datetime import datetime

# Create your views here.
def index(request):
    context = {
        'variable': "this is sent"
    }
    return render(request, 'index.html', context)
    #return HttpResponse('hello world')
def about(request):
    return render(request, 'about.html')
    #return HttpResponse('about page')
def services(request):
    return render(request, 'services.html')
    #return HttpResponse('services page')
def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        reason = request.POST.get('reason')
        contact = Contact(name=name, email=email, phone=phone, reason=reason, date=datetime.today())
        contact.save()
        return render(request, 'contact.html', {'message_sent': True})
    return render(request, 'contact.html')

def learn(request):
    return render(request, 'learn.html')

def smm(request):
    return render(request, 'smm.html')

def product_marketing(request):
    return render(request, 'product_marketing.html')

def automation(request):
    return render(request, 'automation.html')