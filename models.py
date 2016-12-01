# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models


class AuthGroup(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    name = models.CharField(unique=True, max_length=160, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    name = models.CharField(max_length=510, blank=True, null=True)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    password = models.CharField(max_length=256, blank=True, null=True)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=60, blank=True, null=True)
    first_name = models.CharField(max_length=60, blank=True, null=True)
    last_name = models.CharField(max_length=60, blank=True, null=True)
    email = models.CharField(max_length=508, blank=True, null=True)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class City(models.Model):
    name = models.CharField(max_length=40)
    state = models.CharField(max_length=40)
    population = models.FloatField(blank=True, null=True)
    longitude = models.FloatField(blank=True, null=True)
    latitude = models.FloatField(blank=True, null=True)
    elevation = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'city'
        unique_together = (('name', 'state'),)


class DjangoAdminLog(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=400, blank=True, null=True)
    action_flag = models.IntegerField()
    change_message = models.TextField(blank=True, null=True)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    app_label = models.CharField(max_length=200, blank=True, null=True)
    model = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    app = models.CharField(max_length=510, blank=True, null=True)
    name = models.CharField(max_length=510, blank=True, null=True)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=80)
    session_data = models.TextField(blank=True, null=True)
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


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
    jobid = models.BigIntegerField(primary_key=True)
    name = models.CharField(max_length=75, blank=True, null=True)
    company_name = models.CharField(max_length=40, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'jobs'


class Language(models.Model):
    id = models.BigIntegerField()
    region = models.CharField(max_length=4, blank=True, null=True)
    language = models.CharField(max_length=20)
    percentage = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'language'
        unique_together = (('id', 'language'),)


class Occupation(models.Model):
    occupatid = models.FloatField()
    job_title = models.CharField(max_length=40)
    name = models.CharField(max_length=40)

    class Meta:
        managed = False
        db_table = 'occupation'
        unique_together = (('occupatid', 'job_title'),)


class Organization(models.Model):
    oid = models.BigIntegerField()
    name = models.CharField(max_length=40)
    url = models.CharField(max_length=40, blank=True, null=True)
    region = models.CharField(max_length=4, blank=True, null=True)
    address = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'organization'
        unique_together = (('oid', 'name'),)


class Person(models.Model):
    id = models.BigIntegerField()
    name = models.CharField(max_length=30)
    region = models.CharField(max_length=4, blank=True, null=True)
    occupation = models.CharField(max_length=75, blank=True, null=True)
    weekly_salary = models.BigIntegerField(blank=True, null=True)

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
    id = models.BigIntegerField(blank=True, null=True)
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
        managed = False
        db_table = 'state'
