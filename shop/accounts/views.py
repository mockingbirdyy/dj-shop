from django.shortcuts import render
from django.views.generic import View
from .forms import UserCreationForm

class RegisterView(View):
  form_class = UserCreationForm
  def get(self, request):
    form = self.form_class
    return render(request, 'accounts/register.html', {'form': form})
  
  def post(self, request):
    pass