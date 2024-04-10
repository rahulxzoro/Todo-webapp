from django.shortcuts import render,redirect
from . models import Todo
# Create your views here.
def todo_list(request):
    obj=Todo.objects.all()
    if request.method=='POST':
        task=request.POST.get('task')
        date=request.POST.get('date')
        todo=Todo(task=task,date=date)
        todo.save()
    return render(request,'index.html',{'todo':obj})

def edit(request,id):
    obj=Todo.objects.get(id=id)
    
    if request.method=='POST':
        task=request.POST['task']
        date=request.POST['date']
        Todo.objects.filter(id=id).update(task=task,date=date)
        
        return redirect('/')
    
    return render(request,'edit.html',{'todo':obj})

def delete(request,id):
    if request.method=='POST':
        todo=Todo.objects.get(id=id)
        todo.delete()
        return redirect('/')
    return render(request,'index.html')