from django.shortcuts import render,redirect
from .models import Created
from django.contrib import messages

# Create your views here.


def index(request):
    output = ' '
    output  = request.POST.get('create1',' ')
    if output != ' ':

        output_created = Created(name = output)

        output_created.save()
        
    posts = Created.objects.all()[::-1]

    context = {
        'input':output,
        "posts":posts,
    }

    return render(request,'index.html',context)


def create(request):

    output  = request.POST.get('create1',' ')

    output_created = Created(name = output)

    output.save()
    

    return render(request,'create.html')


def edit(request,pk):

    # if input != 'None':

    output_id_check = Created.objects.get(id=pk)

    output  = request.POST.get('edit1','')
    if output == '':
        a = 1
    else:
        input = Created(id = pk ,name = output)
        input.save()
    
        messages.success(request, 'Updated successfully.')

    context = {
       'input12':output_id_check.name, 
    }
    
    return render(request,'edit.html',context)




def delete(request,id):

    post = Created.objects.get(id=id)

    if post:
        post.delete()
        messages.success(request, 'Succesfully deleted')
    else:
        messages.success(request, 'No exist')

    return redirect('/')
    
