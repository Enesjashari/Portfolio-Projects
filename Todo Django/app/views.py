from multiprocessing import context
from django.shortcuts import render,redirect
from django.http import HttpResponse
# Create your views here.
from .forms import TodoForm
from .models import TodoModel
from django.views.decorators.http import require_POST








def main(request):
    return render(request,'main.html')

def index(request):
    forms = TodoForm
    todos = TodoModel.objects.all()[::-1]

    context = {
        "forms":forms,
        "todos":todos,
    }
    return render(request,'index.html',context)



def edit(request,pk):
    todos = TodoModel.objects.get(id=pk)
    
    forms = TodoForm(request.POST or None ,instance=todos)
    if request.method == "POST":
        if forms.is_valid():
            forms.save()
            return redirect('/')
        else:
            pass

    context = {
        "todos":todos,
        "forms":forms,

    }
    return render(request,'edit.html',context)

def delete(request,op):
    todos = TodoModel.objects.get(id=op)
    if todos:
        todos.delete()
    else:
        return HttpResponse('no currect id')
        

    return redirect('/')


@require_POST
def search(request):
    if request.method=='POST':
        
        search_query  = request.POST['search']
        # todo = TodoModel.objects.filter(title = search_query) #Strict query
        todos = TodoModel.objects.filter(title__contains = search_query) #Strict query
        if todos:
            context = {
                "todos":todos,
            }
            return render(request,'search.html',context)
        else:
            result = 'No Results !'
            context = {
                'todos':result,
            }
            return render(request,'no-result.html',context)


def create(request):
    form = TodoForm(request.POST)
    if form.is_valid():
        form.save()
    return redirect('/')



def mark_as_completed(request, id):
    todo = TodoModel.objects.get(id=id)
    todo.completed = True
    todo.save()
    return redirect('/')
