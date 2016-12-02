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
        managed = True
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
        managed = True
        db_table = 'economy'


class Ethnicgroup(models.Model):
    state = models.CharField(max_length=40)
    name = models.CharField(max_length=50)
    percentage = models.FloatField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'ethnicgroup'
        unique_together = (('name', 'state'),)


class Industry(models.Model):
    name = models.CharField(primary_key=True, max_length=40)
    personid = models.FloatField(blank=True, null=True)
    number_of_emp = models.FloatField(blank=True, null=True)
    address = models.CharField(max_length=50, blank=True, null=True)
    type = models.CharField(max_length=25, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'industry'


class Ismember(models.Model):
    state = models.CharField(max_length=40)
    name = models.CharField(max_length=50)
    organization = models.CharField(max_length=12)

    class Meta:
        managed = True
        db_table = 'ismember'
        unique_together = (('state', 'name', 'organization'),)


class Jobs(models.Model):
    jobid = models.BigIntegerField(primary_key=True)
    name = models.CharField(max_length=75, blank=True, null=True)
    company_name = models.CharField(max_length=40, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'jobs'


class Language(models.Model):
    id = models.BigIntegerField(primary_key=True)
    region = models.CharField(max_length=4, blank=True, null=True)
    language = models.CharField(max_length=20)
    percentage = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'language'
        unique_together = (('id', 'language'),)


class Occupation(models.Model):
    occupatid = models.FloatField(primary_key=True)
    job_title = models.CharField(max_length=40)
    name = models.CharField(max_length=40)

    class Meta:
        managed = True
        db_table = 'occupation'
        unique_together = (('occupatid', 'job_title'),)


class Organization(models.Model):
    oid = models.BigIntegerField(primary_key=True)
    name = models.CharField(max_length=40)
    url = models.CharField(max_length=40, blank=True, null=True)
    region = models.CharField(max_length=4, blank=True, null=True)
    address = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'organization'
        unique_together = (('oid', 'name'),)


class Person(models.Model):
    id = models.BigIntegerField(primary_key=True)
    name = models.CharField(max_length=30)
    region = models.CharField(max_length=4, blank=True, null=True)
    occupation = models.CharField(max_length=75, blank=True, null=True)
    weekly_salary = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = True
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
        managed = True
        db_table = 'population'


class Religion(models.Model):
    state = models.CharField(max_length=40)
    city = models.CharField(max_length=40)
    name = models.CharField(max_length=50)
    percentage = models.FloatField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'religion'
        unique_together = (('name', 'state', 'city'),)


class Services(models.Model):
    name = models.CharField(primary_key=True, max_length=20)
    govid = models.FloatField()
    budget = models.FloatField(blank=True, null=True)
    numofemp = models.FloatField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'services'
        unique_together = (('name', 'govid'),)


class State(models.Model):
    id = models.BigIntegerField(primary_key=True, blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    abbreviation = models.CharField(max_length=4, blank=True, null=True)
    country = models.CharField(max_length=255, blank=True, null=True)
    type = models.CharField(max_length=255, blank=True, null=True)
    sort = models.BigIntegerField(blank=True, null=True)
    status = models.CharField(max_length=255, blank=True, null=True)
    occupied = models.CharField(max_length=255, blank=True, null=True)
    notes = models.CharField(max_length=255, blank=True, null=True)
    fips_state = models.CharField(max_length=255, blank=True, null=True)
    assoc_press = models.CharField(max_length=255, blank=True, null=True)
    standard_federal_region = models.CharField(max_length=255, blank=True, null=True)
    census_region = models.CharField(max_length=255, blank=True, null=True)
    census_region_name = models.CharField(max_length=255, blank=True, null=True)
    census_division = models.CharField(max_length=255, blank=True, null=True)
    census_division_name = models.CharField(max_length=255, blank=True, null=True)
    circuit_court = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'state'
