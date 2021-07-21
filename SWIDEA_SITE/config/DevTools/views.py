from django.shortcuts import render,redirect
from django.views.generic import ListView,DetailView,CreateView,UpdateView
from .models import Tool
from .forms import ToolForm
from Ideas.models import Idea

# Create your views here.
tool_list= ListView.as_view(model=Tool,template_name="DevTools/tool_list.html")

tool_create = CreateView.as_view(model=Tool, form_class=ToolForm)

def tool_detail(request,pk):
    tool = Tool.objects.get(pk=pk)
    tool_ideas = Idea.objects.filter(devtool=tool)
    ctx = {"tool": tool, "tool_ideas": tool_ideas}
    return render(request, template_name="DevTools/tool_detail.html", context=ctx)

def tool_delete(request,pk):
    tool = Tool.objects.get(pk=pk)
    tool.delete()
    return redirect('DevTools:tool_list')


tool_update = UpdateView.as_view(model=Tool, form_class=ToolForm,template_name="DevTools/tool_update.html")