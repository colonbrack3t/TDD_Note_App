from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Item, List

def view_lists(request, pk):
    list_ = List.objects.get(pk = pk)
    return render(request, 'list.html', {'list':list_})

def new_list(request):
    if request.POST:
        list_ = List.objects.create()
        Item.objects.create(text= request.POST['item_text'], list = list_)
        return redirect(f'/lists/{list_.pk}/')
    return redirect('/')

def add_item_to_list(request, pk):
    list_ = List.objects.get(pk=pk)
    Item.objects.create(text= request.POST['item_text'], list = list_)
    return redirect(f'/lists/{list_.pk}/')