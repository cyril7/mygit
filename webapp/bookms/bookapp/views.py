
# Create your views here.

from django import forms
from django.template import RequestContext
from django.http import HttpResponse, HttpResponseRedirect
from django.template.loader import get_template
from django.core.paginator import Paginator
from django.core.urlresolvers import reverse

# app specific files

from models import *
from forms import *


def create_book(request):
    form = BookForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = BookForm()

    t = get_template('bookapp/create_book.html')
    c = RequestContext(request,locals())
    return HttpResponse(t.render(c))



def list_book(request):
  
    list_items = Book.objects.all()
    paginator = Paginator(list_items ,10)


    try:
        page = int(request.GET.get('page', '1'))
    except ValueError:
        page = 1

    try:
        list_items = paginator.page(page)
    except :
        list_items = paginator.page(paginator.num_pages)

    t = get_template('bookapp/list_book.html')
    c = RequestContext(request,locals())
    return HttpResponse(t.render(c))



def view_book(request, id):
    book_instance = Book.objects.get(id = id)

    t=get_template('bookapp/view_book.html')
    c=RequestContext(request,locals())
    return HttpResponse(t.render(c))

def edit_book(request, id):

    book_instance = Book.objects.get(id=id)

    form = BookForm(request.POST or None, instance = book_instance)

    if form.is_valid():
        form.save()

    t=get_template('bookapp/edit_book.html')
    c=RequestContext(request,locals())
    return HttpResponse(t.render(c))
