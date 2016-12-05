from django.shortcuts import render
from django.utils import timezone
from .models import City
from .models import Person
from .models import Occupation
from .models import Language
from django.db.models import Avg

from django.db import connection

def home_page(request):
	city = City.objects.using('default').get(name="Gainesville")
	return render(request, 'db_proj/home_page.html', { 'city': city })

def set_of_data(request):
	city = City.objects.using('default').get(name="Atlanta")
	return render(request, 'db_proj/set_of_data.html', { 'city': city })

def queries(request):
	sal = Person.objects.using('default').aggregate(Avg('weekly_salary'))
	return render(request, 'db_proj/queries.html', { 'Avg Weekly Salary': sal })

def query1(request):
	with connection.cursor() as cursor:
		cursor.execute("SELECT  TRUNC(AVG(WEEKLY_SALARY)*12, 2) AS AVERAGE_SALARY FROM PERSON")
		row = cursor.fetchone()

	return render(request, 'db_proj/query1.html', { 'average': row[0] })

def query2(request):
	with connection.cursor() as cursor:
		cursor.execute("SELECT OCCUPATION, TRUNC(AVG(WEEKLY_SALARY)*12, 2) AS AVERAGE_SALARY FROM PERSON WHERE WEEKLY_SALARY = (SELECT MAX(WEEKLY_SALARY) FROM PERSON) AND ROWNUM = 1 GROUP BY OCCUPATION ")
		rows = dictfetchall(cursor)

	return render(request, 'db_proj/query2.html', { 'rows': rows })

def query3(request):
	with connection.cursor() as cursor:
		cursor.execute("SELECT * FROM (SELECT STATE.NAME AS STATE, TRUNC(AVG(WEEKLY_SALARY)*12, 2) AS AVERAGE_SALARY FROM STATE JOIN PERSON ON STATE.ABBREVIATION = PERSON.REGION WHERE ROWNUM <= 15 GROUP BY STATE.NAME) ORDER BY AVERAGE_SALARY DESC")
		rows = dictfetchall(cursor)

	return render(request, 'db_proj/query3.html', { 'rows': rows })

def query4(request):
	with connection.cursor() as cursor:
		cursor.execute("SELECT * FROM(SELECT NAME, TRUNC(GDP/POPULATION,2) AS WEALTH_PER_CITIZEN FROM(SELECT STATE.NAME AS NAME, COUNT(PERSON.NAME) AS POPULATION, SUM(PERSON.WEEKLY_SALARY)*12 AS GDP FROM PERSON JOIN STATE ON STATE.ABBREVIATION = PERSON.REGION GROUP BY STATE.NAME) ORDER BY WEALTH_PER_CITIZEN DESC) WHERE ROWNUM < 6")
		rows = dictfetchall(cursor)

	return render(request, 'db_proj/query4.html', { 'rows': rows })


def query5(request):
	with connection.cursor() as cursor:
		cursor.execute("SELECT COMPANY, AVG_WEEKLY_SAL*12 AS AVG_SALARY FROM(SELECT ORGANIZATION.NAME AS COMPANY, AVG(PERSON.WEEKLY_SALARY) AS AVG_WEEKLY_SAL FROM ORGANIZATION JOIN JOBS ON ORGANIZATION.NAME = JOBS.COMPANY_NAME JOIN PERSON ON JOBS.NAME = PERSON.OCCUPATION GROUP BY ORGANIZATION.NAME ORDER BY AVG_WEEKLY_SAL DESC) WHERE ROWNUM < 11")
		rows = dictfetchall(cursor)

	return render(request, 'db_proj/query5.html', { 'rows': rows })

def about_us(request):
	city = City.objects.using('default').get(name="Boston")
	return render(request, 'db_proj/about_us.html', { 'city': city })

def dictfetchall(cursor):
	"Return all rows from a cursor as a dict"
	columns = [col[0] for col in cursor.description]
	return [
		dict(zip(columns, row))
		for row in cursor.fetchall()
	]
