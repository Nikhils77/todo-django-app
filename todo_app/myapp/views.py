from django.shortcuts import render,redirect
from .models import Task
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
@login_required
def home(request):
    tasks=Task.objects.filter(user=request.user)
    return render(request,'home.html',{'tasks':tasks})
def add(request):
    if request.method == "POST":
        title=request.POST.get("title")
        description=request.POST.get("description")
        due_at=request.POST.get("due_date")
        Task.objects.create(user=request.user,title=title,description=description,due_at=due_at)
        return redirect('/')
    return render(request ,'add_task.html')
def edit(request,id):
    task=Task.objects.get(id=id)
    if request.method=="POST":
        task.title=request.POST.get("title")
        task.description=request.POST.get("description")
        task.save()
        return redirect('/')        

    return render(request,'edit_task.html',{'task':task})
def complete_task(request,id):
    task=Task.objects.get(id=id)
    task.is_completed=True
    task.save()
    return redirect('/')
def delete_task(request,id):
    task=Task.objects.get(id=id)
    task.delete()
    return redirect('/')

def register(request):
    if request.method=="POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/login/')
    else:
        form = UserCreationForm()
    
    return render(request, "register.html", {"form": form})