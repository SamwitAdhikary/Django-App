from django.shortcuts import render, HttpResponse
from .models import Conatct
# Create your views here.
def index(request):
    return render(request, 'home/index.html')
    # return HttpResponse('This is home page')

def contact(request):
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        content = request.POST['content']
        print(name, email, phone, content)

        contact = Conatct(name=name, email=email, phone=phone, content=content)
        contact.save()

    return render(request, 'home/contact.html')
    # return HttpResponse('This is contact page')