from django.contrib import admin
from .models import Cryptocurrency, Portfolio, Holding



# Register your models here.
admin.site.register(Cryptocurrency)
admin.site.register(Portfolio)
admin.site.register(Holding)
