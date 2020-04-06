from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Item

def index_page(request):
    if request.method == 'POST':
        Item.objects.create(text=request.POST['item_text'])
        return redirect('/')
    items = Item.objects.all()
    return render(request, 'index.html', {'items': items})