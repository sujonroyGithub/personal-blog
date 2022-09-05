from django.shortcuts import render
from .models import Post ,Contact
from datetime import datetime
from blog_app.models import Contact,Post
from django.contrib import messages
# Create your views here.
def index(request):
    posts = Post.objects.all()
    return render(request,'index.html', {'posts':posts})

def contact(request):
    if request.method == "POST":
        fname = request.POST.get('fname')
        lname =request.POST.get('lname')
        email =request.POST.get('email')
        adress =request.POST.get('adress')
        city =request.POST.get('city')
        state =request.POST.get('state')
        
        
        contact = Contact(fname= fname, lname=lname,email=email,adress=adress,city=city, state=state,date=datetime.today())
        contact.save()
        messages.success(request, ' Your Information Has been Sent Sucessfully..')
    return render(request, 'contact.html')

def about(request):
    return render(request, 'about.html')