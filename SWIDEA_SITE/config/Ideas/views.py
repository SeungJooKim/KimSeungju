from typing import List
from django.db import models
from django.shortcuts import render,get_object_or_404,redirect
from django.views.generic import ListView,DetailView
from .models import Idea
from .forms import  IdeaForm 
from django.views.generic import CreateView,UpdateView
from django.http import HttpResponse,JsonResponse
import json

idea_list = ListView.as_view(model=Idea)

def idea_create(request):
    return render(request,'Ideas/idea_form.html')

idea_create = CreateView.as_view(model=Idea, form_class=IdeaForm)

def idea_detail(request,pk):
    idea = Idea.objects.get(pk=pk)
    ctx = {"idea": idea}
    return render(request, template_name="Ideas/idea_detail.html", context=ctx)

def idea_delete(request,pk):
    idea = Idea.objects.get(pk=pk)
    idea.delete()
    return redirect('Ideas:idea_list')


idea_update = UpdateView.as_view(model=Idea, form_class=IdeaForm,template_name="Ideas/idea_update.html")

def interest_add(request):
    if request.is_ajax():
        idea_pk= request.GET['pk']
        idea = Idea.objects.get(pk=idea_pk)
        idea.interest= idea.interest+1
        idea.save()
        context ={'interest': idea.interest}
    return HttpResponse(json.dumps(context), content_type='application/json')

def interest_minus(request):
    if request.is_ajax():
        idea_pk= request.GET['pk']
        idea = Idea.objects.get(pk=idea_pk)
        idea.interest= idea.interest-1
        idea.save()
        context ={'interest': idea.interest}
    return HttpResponse(json.dumps(context), content_type='application/json')