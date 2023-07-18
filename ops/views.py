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
        context['message'] = "New Book added succesfully"
    return render(request, 'add_book.html', context)


def one_book_delete(request, pk):
    try:
        instance = Book.objects.get(pk=pk)
        instance.delete()
        mess = f"Book with id={instance.id} has been deleted."
    except:
        mess = f"Cannot find book with id={pk}."
    context = {
        'books': Book.objects.all(),
        'message' : mess
    }
    return render(request, 'all_books.html', context)

