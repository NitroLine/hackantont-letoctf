from django.forms.models import model_to_dict
from typing import Optional

from  app.models import Doctors, Pacient, Task
from django.core import serializers

def create_doctor(name, birthday, phone, email, depart, cab, startwork, endwork, vacation ) -> (Doctors, bool):
    return Doctors.objects.create(
        name=name,
        birthday = birthday,
        phone = phone,
        email = email,
        depart = depart,
        cab = cab,
        startwork = startwork,
        endwork = endwork,
        vacation = vacation,
    )

def create_pacient(name, birthday, phone, email, depart, chamber, starttreament, endtreament, checkout ) -> (Pacient, bool):
    return Pacient.objects.create(
        name=name,
        birthday = birthday,
        phone = phone,
        email = email,
        depart = depart,
        chamber = chamber,
        starttreament = starttreament,
        endtreament = endtreament,
        checkout = checkout,
    )

def create_task(pacient,title,description,doctor,time,status) -> (Task, bool):
    return Task.objects.create(
        pacient=Pacient.objects.filter(id=pacient).first(),
        title = title,
        description = description,
        doctor = Doctors.objects.filter(id = doctor).first(),
        time = time,
        status = status,

    )

def read_doctors() -> Optional[Doctors]:
    return  list(map(model_to_dict, list(Doctors.objects.all()) ))

def read_pacients() -> Optional[Pacient]:
    return  list(map(model_to_dict, list(Pacient.objects.all()) ))

def read_tasks() -> Optional[Task]:
    return  list(map(model_to_dict, list(Task.objects.all()) ))

def read_cur(base, param, value):
    if base == 'Doctors':
        base = Doctors.objects.filter(param=value).first()
        return model_to_dict(base)
    elif base == 'Pacient':
        Pacient.objects.filter(id=param).first()
        base = Pacient.objects.filter(param=value).first()
        return model_to_dict(base)
    elif base == 'Task':
        Task.objects.filter(id=param).first()
        base = Task.objects.filter(param=value).first()
        return model_to_dict(base)
    else:
        return {'False':'False'}

