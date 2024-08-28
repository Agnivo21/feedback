from django.shortcuts import render,redirect
from .models import *

# Create your views here.
def feedback(request):
    if request.method == "POST":
        data = request.POST
        customername = data.get('customerName')
        email = data.get('customerEmail')
        phone = data.get('phone')
        ordernumber = data.get('orderNumber')
        message = data.get('message')
        print(customername,email,phone,ordernumber,message)
        Feedback.objects.create(
            customername = customername,
            email = email,
            phone = phone,
            ordernumber = ordernumber,
            message = message,
        )
        return redirect('/feedback/')
    return render(request,"feedback.html")