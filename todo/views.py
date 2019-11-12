from django.shortcuts import render, HttpResponse
from .models import Item

# Create your views here.
def get_todo(request):
    results = Item.objects.all()
    return render(request, "todo_list.html", {'items': results})