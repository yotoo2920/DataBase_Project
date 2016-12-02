from django.contrib import admin
from .models import City
from .models import Industry
from .models import Jobs
from .models import Language
from .models import Occupation
from .models import Organization
from .models import Person
from .models import Services
from .models import State

admin.site.register(City)
admin.site.register(Industry)
admin.site.register(Jobs)
admin.site.register(Language)
admin.site.register(Occupation)
admin.site.register(Organization)
admin.site.register(Person)
admin.site.register(Services)
admin.site.register(State)
