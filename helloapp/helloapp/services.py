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

def create_task(title,description,doctor,time) -> (Task, bool):
    return Task.objects.create(
        title = title,
        description = description,
        doctor = Doctors.objects.filter(id = doctor).first(),
        time = time,

    )

def read_doctors() -> Optional[Doctors]:
    return  list(map(model_to_dict, list(Doctors.objects.all()) ))

def read_pacients() -> Optional[Pacient]:
    return  list(map(model_to_dict, list(Pacient.objects.all()) ))

def read_tasks() -> Optional[Task]:
    return  list(map(model_to_dict, list(Task.objects.all()) ))