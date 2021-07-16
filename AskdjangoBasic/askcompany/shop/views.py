from django.http.response import HttpResponse, JsonResponse
from django.shortcuts import render
from django.http import HttpResponse
from .models import Item


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
