from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views.generic import CreateView


# Create your views here.
class SignUpView(CreateView):
    form_class = UserCreationForm  # built in Django form to register User
    # *after signup, user'll be redirected to Login page
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'
