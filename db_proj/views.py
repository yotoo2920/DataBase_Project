from django.shortcuts import render
from django.utils import timezone
from .models import City
from .models import Person
from .models import Occupation
from .models import Language

def home_page(request):
	city = City.objects.using('default').get(name="Gainesville")
	return render(request, 'db_proj/home_page.html', { 'city': city })

def set_of_data(request):
	city = City.objects.using('default').get(name="Atlanta")
	return render(request, 'db_proj/home_page.html', { 'city': city })

def queries(request):
	city = City.objects.using('default').get(name="Miami")
	return render(request, 'db_proj/queries.html', { 'city': city })

def about_us(request):
	city = City.objects.using('default').get(name="Boston")
	return render(request, 'db_proj/about_us.html', { 'city': city })
