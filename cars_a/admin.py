from multiprocessing.resource_tracker import register

from django.contrib import admin
from .models import Cars
# Register your models here.

admin.site.register(Cars)