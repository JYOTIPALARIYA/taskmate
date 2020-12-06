from django.shortcuts import render,redirect
# from django.http import HttpResponse
# # Create your views here.
# def register(request):
#     return HttpResponse("user app working!")
#from django.contrib.auth.forms import UserCreationForm
from .forms import CustomRegisterForm
from django.contrib import messages
def register(request):
    if request.method=="POST":
        # register_form=UserCreationForm(request.POST)
        register_form=CustomRegisterForm(request.POST)
        
        if register_form.is_valid():
            register_form.save()
            messages.success(request, ("New User Account Created","**Login Please**"))
            return redirect('todolist')
    else:
        register_form=CustomRegisterForm()
    return render(request,'register.html',{'register_form':register_form})