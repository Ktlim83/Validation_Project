from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from .models import *


def index(request):
    context = {
        'shows': Show.objects.all()
    }
    return render(request, "shows.html", context)  


def new(request): 
    return render(request, "new.html")  


def create(request):
    # gets validation dictionary and holds it in request.post
    errors = Show.objects.basic_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/shows/new')
        
    # CREATE SHOW
    else:
        show = Show.objects.create(
        title = request.POST['title'],
        network = request.POST['network'],
        release_date = request.POST['release_date'],
        description = request.POST['description'],
    )
    print(request.POST)
    return redirect('/shows') 


def edit(request, show_id):
    # Querys a show with its show id
    # Capture the variable and object, then adding it back into context 
    one_show = Show.objects.get(id=show_id)
    context = {
         'show' : one_show
    }
    return render(request, "edit.html", context)   


def update(request, show_id):
    if request.method == "POST":
        errors = Show.objects.basic_validator(request.POST)
        if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request, value)
            print(show_id)
            return redirect(f'/shows/{show_id}/edit')
    #  UPDATES THE SHOW
        update_show = Show.objects.get(id=show_id)
        # UPDATE EACH FIELD
        update_show.title = request.POST['title']
        update_show.network = request.POST['network']
        update_show.release_date = request.POST['release_date']
        update_show.description = request.POST['description']
        update_show.save()
        
    
    return redirect('/shows/')
 

def delete(request, show_id):
    # DELETE SHOW
    delete_show = Show.objects.get(id=show_id)
    delete_show.delete()
    return redirect('/shows')  


def show(request, show_id):
    # Querys a show with its show id
    # Capture the variable and object, then adding it back into context 
    one_show = Show.objects.get(id=show_id)
    context = {
         'show' : one_show
    }
    return render(request, "show.html", context)  





# def modify(request, id):
#     # pass the post data to the method we wrote and save the response in a variable called errors
#     errors = Show.objects.basic_validator(request.POST)
#         # check if the errors dictionary has anything in it
#     if len(errors) > 0:
#         # if the errors dictionary contains anything, loop through each key-value pair and make a flash message
#         for key, value in errors.items():
#             messages.error(request, value)
#         # redirect the user back to the form to fix the errors
#         return redirect('/show/edit/'+id)
#     else:
#         # if the errors object is empty, that means there were no errors!
#         # retrieve the blog to be updated, make the changes, and save
#         show = Show.objects.get(id = id)
#         show.title = request.POST['title']
#         show.network = request.POST['network']
#         show.description = request.POST['description']
#         show.save()
#         messages.success(request, "Show successfully updated")
#         # redirect to a success route
#         return redirect('/shows')
    
    

