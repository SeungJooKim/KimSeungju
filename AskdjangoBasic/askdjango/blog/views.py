from typing import List
from django.db import models
from django.shortcuts import render
from django.views.generic import ListView,DetailView
from .models import Post

post_list = ListView.as_view(model=Post)

post_detail = DetailView.as_view(model=Post)