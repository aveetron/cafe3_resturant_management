from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib import messages
from .forms import * 
from .models import *
# Create your views here.
def home(request):
    allItem = Item.objects.all().order_by('-pk')
    context = {
        'allItem': allItem
    }
    return render(request, 'item.html', context)


def addItem(request):
    if request.method == 'POST':
        request.POST = request.POST.copy()
        request.POST['name'] = request.POST.get('name')
        request.POST['price'] = request.POST.get('price')
        form = ItemForm(request.POST)
        if form.is_valid():
            form.save()
            message = 'Item added successfully'
            messages.success(request, message)
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
        else:
            message = 'Item cannot be added'
            messages.warning(request, message)
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    else:
        message = 'Item cannot be added'
        messages.warning(request, message)
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

def deleteItem(request, id):
    try:
        getItem = Item.objects.get(id = id)
        getItem.delete()
        message = 'Item deleted successfully'
        messages.success(request, message)
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    except:
        message = 'Item cannot be Deleted'
        messages.warning(request, message)
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))