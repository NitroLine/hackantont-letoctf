from django.contrib import admin

# Register your models here.
from app.models import Task, Doctors, Pacient

models = [Task, Doctors, Pacient]
admin.site.register(models)