from django.shortcuts import render 
from django.http import HttpResponse, Http404, JsonResponse, HttpResponseRedirect
from django.template.loader import render_to_string 
from .models import Book

def all_book_view(request):
    if request.method == "POST":
        pass 
    if request.method == "GET":
        context = {
            'books': Book.objects.all()
        }
        return HttpResponse(render_to_string('all_books.html', context))
    
def one_book_view(request, pk):
    instance = Book.objects.get(pk=pk)
    context = {
        'book' : instance
    }
    return HttpResponse(render_to_string('one_book.html', context))

def add_book_view(request):
    context = {'message':""}
    if request.method == 'POST':
        data = request.POST
        new = Book(name=data.get('name'), description=data.get('desc'), price=data.get('price'))
        if data.get('number_of_pages'):
            new.number_of_pages = data.get('number_of_pages')
        new.save()
        context['message'] = f"Book with UID:{new.id} has been added to the library succesfully."
    return render(request, 'add_book.html', context)


def one_book_delete(request, pk):
    try:
        instance = Book.objects.get(pk=pk)
        instance.delete()
        mess = f"Book with UID:{pk} has been deleted."
    except:
        mess = f"Book with UID:{pk} does not exists."
    context = {
        'books': Book.objects.all(),
        'message' : mess
    }
    return render(request, 'all_books.html', context)

def update_book_view(request):
    context = {'message':''}
    if request.method == 'POST':
        data = request.POST
        pk = request.POST.get('id')
        print("Reached HERE: ", pk)
        try:
            instance = Book.objects.get(pk=pk)
            mess = f"Book with UID:{pk} has been updated."
            if data.get('name'): instance.name = data.get('name')
            if data.get('price'): instance.price = data.get('price')
            if data.get('number_of_pages'): instance.number_of_pages = data.get('number_of_pages')
            if data.get('desc'): instance.description = data.get('desc')
            instance.save()
        except:
            mess = f"Book with UID:{pk} does not exists."
        context['message'] = mess
    return render(request, 'update_book.html', context)

