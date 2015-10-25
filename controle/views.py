from django.shortcuts import render
from django.views.generic import ListView
from .models import Produto

class homeView(ListView):
	model = Produto
	template_name = 'home.html'
	paginate_by = 9