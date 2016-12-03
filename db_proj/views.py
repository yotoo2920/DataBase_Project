from django.shortcuts import render
from django.utils import timezone
from .models import City
from .models import Person
from .models import

def home_page(request):
	city = City.objects.using('default').get(name="Gainesville")
	return render(request, 'db_proj/home_page.html', { 'city': city })

def set_of_data(request):
	# person = Person.objects.using('default').get(region="MA  ")
	# return render(request, 'db_proj/set_of_data.html', { 'person': person})
	city = City.objects.using('default').get(name="Gainesville")
	return render(request, 'db_proj/home_page.html', { 'city': city })

def queries(request):
	city = City.objects.using('default').get(name="Gainesville")
	return render(request, 'db_proj/queries.html', { 'city': city })
