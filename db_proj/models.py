from django.db import models
from django.utils import timezone

class City(models.Model):
    name = models.CharField(primary_key=True, max_length=40)
    state = models.CharField(max_length=40)
    population = models.FloatField(blank=True, null=True)
    longitude = models.FloatField(blank=True, null=True)
    latitude = models.FloatField(blank=True, null=True)
    elevation = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'city'
        unique_together = (('name', 'state'),)


class Economy(models.Model):
    state = models.CharField(primary_key=True, max_length=40)
    gdp = models.FloatField(blank=True, null=True)
    agriculture = models.FloatField(blank=True, null=True)
    service = models.FloatField(blank=True, null=True)
    industry = models.FloatField(blank=True, null=True)
    inflation = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'economy'


class Ethnicgroup(models.Model):
    state = models.CharField(max_length=40)
    name = models.CharField(max_length=50)
    percentage = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ethnicgroup'
        unique_together = (('name', 'state'),)


class Industry(models.Model):
    name = models.CharField(primary_key=True, max_length=40)
    personid = models.FloatField(blank=True, null=True)
    number_of_emp = models.FloatField(blank=True, null=True)
    address = models.CharField(max_length=50, blank=True, null=True)
    type = models.CharField(max_length=25, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'industry'


class Ismember(models.Model):
    state = models.CharField(max_length=40)
    name = models.CharField(max_length=50)
    organization = models.CharField(max_length=12)

    class Meta:
        managed = False
        db_table = 'ismember'
        unique_together = (('state', 'name', 'organization'),)


class Jobs(models.Model):
    salary = models.FloatField(blank=True, null=True)
    occupatid = models.FloatField(blank=True, null=True)
    personid = models.FloatField()
    title = models.CharField(max_length=40)

    class Meta:
        managed = False
        db_table = 'jobs'
        unique_together = (('personid', 'title'),)


class Language(models.Model):
    state = models.CharField(max_length=40)
    city = models.CharField(max_length=40)
    name = models.CharField(max_length=50)
    percentage = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'language'
        unique_together = (('state', 'city', 'name'),)


class Occupation(models.Model):
    occupatid = models.FloatField()
    job_title = models.CharField(max_length=40)
    name = models.CharField(max_length=40)

    class Meta:
        managed = False
        db_table = 'occupation'
        unique_together = (('occupatid', 'job_title'),)


class Organization(models.Model):
    abbreviation = models.CharField(max_length=12)
    name = models.CharField(max_length=40)
    state = models.CharField(max_length=40, blank=True, null=True)
    city = models.CharField(max_length=40, blank=True, null=True)
    established = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'organization'
        unique_together = (('abbreviation', 'name'),)


class Person(models.Model):
    id = models.FloatField(primary_key=True)
    state = models.CharField(max_length=40, blank=True, null=True)
    city = models.CharField(max_length=25, blank=True, null=True)
    name = models.CharField(max_length=40)
    dob = models.DateField(blank=True, null=True)
    weight = models.FloatField(blank=True, null=True)
    height = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'person'
        unique_together = (('id', 'name'),)


class Population(models.Model):
    state = models.CharField(primary_key=True, max_length=40)
    state_population = models.FloatField(blank=True, null=True)
    percent_pop_in_college = models.FloatField(blank=True, null=True)
    emp_oversixteen = models.FloatField(blank=True, null=True)
    emp_inlaborforce = models.FloatField(blank=True, null=True)
    emp_notlaborforce = models.FloatField(blank=True, null=True)
    emp_armedforces = models.FloatField(blank=True, null=True)
    emp_unemployed = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'population'


class Religion(models.Model):
    state = models.CharField(max_length=40)
    city = models.CharField(max_length=40)
    name = models.CharField(max_length=50)
    percentage = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'religion'
        unique_together = (('name', 'state', 'city'),)


class Services(models.Model):
    name = models.CharField(max_length=20)
    govid = models.FloatField()
    budget = models.FloatField(blank=True, null=True)
    numofemp = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'services'
        unique_together = (('name', 'govid'),)


class State(models.Model):
    name = models.CharField(unique=True, max_length=40)
    capital = models.CharField(max_length=40)
    population = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'state'
        unique_together = (('name', 'capital'),)
