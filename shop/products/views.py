from django.shortcuts import render
from django.views.generic import View


# home page of site that shows products, categories  etc.
class Home(View):
  def get(self, request):
    return render(request, 'accounts/home.html')
