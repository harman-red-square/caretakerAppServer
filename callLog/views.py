from django.shortcuts import render
from caretaker import caretakerGlobalConstants

# Create your views here.
def home(request):
    print caretakerGlobalConstants.a;
    return render(request,"home.html",{})