from django.shortcuts import render,redirect
from django.http import HttpResponse
from todolist_app.models import TaskList
from todolist_app.forms import TaskForm
from django.contrib import messages
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
# Create your views here.
@login_required

def todolist(request):
    if request.method=="POST":
        form=TaskForm(request.POST or None)
        if form.is_valid():
            # form.save(commit=False).manage = request.user
            # form.save()
            instance=form.save(commit=False)
            instance.manage = request.user
            form.save()
        messages.success(request,("New Task Added"))
        return redirect('todolist')
    else:
        # all_tasklist=TaskList.objects.all()
        
        all_tasklist=TaskList.objects.filter(manage=request.user)#to see particular user can access his tasks only
        paginator=Paginator(all_tasklist,5)
        page=request.GET.get('pg')
        all_tasklist=paginator.get_page(page)

        return render(request,'templ.html',{'all_tasklist':all_tasklist})
    #return HttpResponse("Welcome to TaskPage")
    # return render(request,'templ.html', {})
    # return render(request,'templ.html', {'welcome_text':"Welcome from Jinja2"}) #using jinja2,which is used if u wanna add python code in ur html page
    # context={
    #     'welcome_text':"Welcome from Jinja2"
    #     }
    # return render(request,'templ.html', context)
@login_required

def contact(request):
    context={
        'con_text':"Welcome to contact us"
        }
    return render(request,'contact.html', context)

def delete_task(request,task_id):
    
    task=TaskList.objects.get(pk=task_id)
    if task.manage == request.user:
            
        task.delete()
    else:
        messages.error(request,("You Are not Allowed "))
    return redirect('todolist')


def edit_task(request,task_id):
    if request.method=="POST":
        task=TaskList.objects.get(pk=task_id)
        form=TaskForm(request.POST or None, instance=task)
        if form.is_valid():
            form.save()
        messages.success(request,("New Task Added"))
        return redirect('todolist')
    else:
        task_obj=TaskList.objects.get(pk=task_id)
        return render(request,'edit.html',{'task_obj':task_obj})

def complete_task(request,task_id):
    task=TaskList.objects.get(pk=task_id)
    if task.manage == request.user:
        task.done=True
        task.save()
    else:
        messages.error(request,("You Are not Allowed "))
    return redirect('todolist')


def pending_task(request,task_id):
    task=TaskList.objects.get(pk=task_id)
    task.done=False
    task.save()
    return redirect('todolist')

def index(request):
    context={
        'index_text':"Welcome to index page2"
        }
    return render(request,'index.html', context)    

def about(request):
    context={
        'ab_text':"Welcome to about page2"
        }
    return render(request,'about.html', context)