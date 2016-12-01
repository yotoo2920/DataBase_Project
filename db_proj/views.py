from django.shortcuts import render
from django.utils import timezone
from .models import City

def home_page(request):
	city = City.objects.using('default').get(name="Gainesville")
	return render(request, 'db_proj/home_page.html', { 'city': city })
