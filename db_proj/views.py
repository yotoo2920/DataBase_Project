from django.shortcuts import render
from django.utils import timezone
from .models import City
from .models import Person
from .models import Occupation
from .models import Language
from django.db.models import Avg

def home_page(request):
	city = City.objects.using('default').get(name="Gainesville")
	return render(request, 'db_proj/home_page.html', { 'city': city })

def set_of_data(request):
	city = City.objects.using('default').get(name="Atlanta")
	return render(request, 'db_proj/home_page.html', { 'city': city })

def queries(request):
	sal = Person.objects.using('default').aggregate(Avg('weekly_salary'))
	return render(request, 'db_proj/queries.html', { 'Avg Weekly Salary': sal })
	# person = Person.objects.raw('SELECT  TRUNC(AVG(WEEKLY_SALARY)*12, 2) AS AVERAGE_SALARY FROM PERSON')
	# return render(request, 'db_proj/queries.hmtl', {'AVERAGE_SALARY' : person})

def about_us(request):
	city = City.objects.using('default').get(name="Boston")
	return render(request, 'db_proj/about_us.html', { 'city': city })
