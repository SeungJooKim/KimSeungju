from django.shortcuts import redirect, render
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.views.generic import CreateView
from django.contrib.auth.models import User
from .forms import SignupForm
# def signup(request):
#     if request.method =="POST":
#         form = UserCreationForm(request.POST)
#         if form.is_valid:
#             user = form.save()
#             return redirect(settings.LOGIN_URL)
#     else :
#         form = UserCreationForm()
#     return render(request, 'accounts/signup.html',{
#         'form': form,
#     })
signup =CreateView.as_view(model=User,form_class=SignupForm, template_name="accounts/signup.html", success_url =settings.LOGIN_URL)

@login_required
def profile(request):
    return render(request, 'accounts/profile.html')
