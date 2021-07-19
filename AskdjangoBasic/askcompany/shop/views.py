from django.http.response import HttpResponse, JsonResponse
from django.shortcuts import get_list_or_404, get_object_or_404, render,redirect
from django.http import HttpResponse
from .models import Item
import re
from .forms import  ItemForm 
from django.views.generic import CreateView,UpdateView


def archives_year(request, year):
    return HttpResponse('{}년도에 대한 내용'.format(year))


def view1(request):
    return HttpResponse('HELLO, ASK COMPANY')


def view2(request):
    return render(request, 'template.html')


def view3(request):
    return JsonResponse({'hello': 'Ask company'})


def item_list(request):
    qs = Item.objects.all()

    q = request.GET.get('q', '')

    if q:
        qs.filter(name__icontains=q)

    return render(request, 'shop/item_list.html', {
        'item_list': qs,
        'q': q,
    })


def item_detail(request, pk):
    item = get_object_or_404(Item, pk=pk)
    return render(request, 'shop/item_detail.html', {
        'item': item
    })

def item_new(request):
    return render(request,'shop/item_form.html')

# def item_new(request, item=None):

#     if request.method == 'POST':
#         form = ItemForm(request.POST, request.FILES,instance=item)
#         if form.is_valid():
#             item = form.save()
#             return redire ct(item)
#     else :
#         form =ItemForm(instance=item)

#     return render(request, 'shop/item_form.html', {
#         'form': form,
#     })

# def item_edit(request, pk):
#     item = get_object_or_404(Item, pk=pk)
#     return item_new(request, item)

item_new = CreateView.as_view(model=Item, form_class=ItemForm)
item_edit = UpdateView.as_view(model=Item,form_class=ItemForm)