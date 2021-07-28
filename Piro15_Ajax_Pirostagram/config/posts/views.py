from django.shortcuts import render,redirect
from django.urls import reverse_lazy
from .models import Post, Comment
from posts.forms import PostForm
from django.views.generic import CreateView
import json
from django.http.response import JsonResponse
from django.views.decorators.csrf import csrf_exempt

def post_list(request):
    posts = Post.objects.all()
    comments = Comment.objects.all()
    context ={
        'posts': posts,
        'comments': comments,
    }
    return render(request, template_name="posts/post_list.html", context= context)

@csrf_exempt
def delete_comment(request):
    print("views")
    req = json.loads(request.body)
    comment_pk = req['pk']
    comment = Comment.objects.get(pk=comment_pk )
    comment.delete()
    return JsonResponse({'pk': comment_pk})

@csrf_exempt
def add_comment(request):
    req = json.loads(request.body)
    post_pk = req['pk']
    post= Post.objects.get(pk=post_pk)

    newComment= req['newComment']
    comment = Comment.objects.create(post = post, content=newComment)
    comment.save()

    return JsonResponse({'post_pk': post_pk, 'comment_pk': comment.pk, "content": comment.content})

@csrf_exempt
def like(request):
    req = json.loads(request.body)
    post_pk = req['post_pk']
    post= Post.objects.get(pk=post_pk)
    
    if post.like :
        post.like = False
    else:
        post.like = True
    
    post.save()

    return JsonResponse({'post_pk':post_pk, 'post_like':post.like})

    

class PostCreateView(CreateView):
    model = Post						
    form_class = PostForm 
    success_url = reverse_lazy('posts:post_list')
    template_name = 'posts/post_form.html'