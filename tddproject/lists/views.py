from django.shortcuts import render, redirect
from .models import Item, List


def index_page(request):
    return render(request, 'index.html')


def view_list(request, pk):
    list_ = List.objects.get(id=pk)
    return render(request, 'list.html', {'list': list_})


def new_list(request):
    list_ = List.objects.create()
    Item.objects.create(text=request.POST['item_text'], list=list_)
    return redirect(f'/lists/{list_.pk}')


def new_item(request, pk):
    list_ = List.objects.get(id=pk)
    Item.objects.create(text=request.POST['item_text'], list=list_)
    return redirect(f'/lists/{list_.id}/')