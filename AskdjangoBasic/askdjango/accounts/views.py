from django.shortcuts import redirect, render,resolve_url
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.views.generic import CreateView
from django.contrib.auth.models import User
from .forms import SignupForm
from django.contrib.auth import login as auth_login
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
#signup =CreateView.as_view(model=User,form_class=SignupForm, template_name="accounts/signup.html", success_url =settings.LOGIN_URL)

class SignupView(CreateView):
    model = User
    form_class = SignupForm
    template_name = 'accounts/signup.html'

    def get_success_url(self):
        return resolve_url('profile')

    def form_valid(self, form):
        user = form.save()
        auth_login(self.request, user)
        return redirect(self.get_success_url())

signup = SignupView.as_view()

@login_required
def profile(request):
    return render(request, 'accounts/profile.html')
