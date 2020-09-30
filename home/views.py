from django.shortcuts import render
from django.http import HttpResponse
from home.models import Contact

# Create your views here.
def home(request):
    #return HttpResponse("This is the home page (/)")
    return render(request, 'home.html')

def about(request):
    #return HttpResponse("This is the about page (/about)")
    return render(request, 'about.html')
def projects(request):
        #return HttpResponse("This is the contact page (/projects)")
        return render(request, 'projects.html')
def contact(request):
    if request.method=="POST":
        name = request.POST['name']
        email = request.POST['email']
        subject = request.POST['subject']
        message = request.POST['message']

        contact = Contact(name=name, email=email, subject=subject, message=message)
        contact.save()
        print(contact)
    #return HttpResponse("This is the contact page (/contact)")
    return render(request, 'contact.html')
