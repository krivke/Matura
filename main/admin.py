from django import db
from django.contrib import admin
from .models import Predmet
from .models import Razred

from .models import Naslov

admin.site.register(Predmet)
admin.site.register(Razred)
admin.site.register(Naslov)