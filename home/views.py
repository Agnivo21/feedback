from django.shortcuts import render

from django.http import HttpResponse

def home(request):
    
    return HttpResponse("Hello I am a djanjo server")

def landing_page(request):
    peoples=[
        {"name": "agnivo","age" : 26},
        {"name": "bubu","age" : 30},
        {"name": "nelo","age" : 15},
        {"name": "beleo","age" : 54},
        {"name": "choi","age" : 30},
    ]
    text ='''Lorem ipsum dolor sit amet consectetur adipisicing elit. Ab harum expedita officia dolore ullam ratione temporibus libero tenetur illo pariatur eos ex, asperiores aliquid sit consequuntur fugit non nostrum amet.'''
    return render(request,"landing_page.html",context={"peoples":peoples,"text" : text})