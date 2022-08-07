from django.forms.models import model_to_dict
from typing import Optional
import sqlite3
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

def read_tasks_by_patient(id) -> Optional[Pacient]:
    return  list(map(model_to_dict, list(Task.objects.filter(pacient__id=id))))

def read_tasks() -> Optional[Task]:
    return  list(map(model_to_dict, list(Task.objects.all()) ))

def read_cur(base, param, value):
    if base == 'Task':
        base = Task.objects.filter(id=value).first()
        return model_to_dict(base)
    else:
        return {'False':'False'}


def edit_cur(base, param, valueforsearch, value, filterparam):
    if base == 'Doctors':
        sqliteConnection = sqlite3.connect('db.sqlite3')
        cursor = sqliteConnection.cursor()
        sql_update_query = f"Update app_doctors set {param} = {value} where {param} = {valueforsearch}"
        cursor.execute(sql_update_query)
        sqliteConnection.commit()
        cursor.close()
        return {'True':'True'}
    elif base == 'Pacient':
        sqliteConnection = sqlite3.connect('db.sqlite3')
        cursor = sqliteConnection.cursor()
        sql_update_query = f"Update app_pacient set {param} = {value} where {param} = {valueforsearch}"
        cursor.execute(sql_update_query)
        sqliteConnection.commit()
        cursor.close()
        return {'True':'True'}
    elif base == 'Task':
        sqliteConnection = sqlite3.connect('db.sqlite3')
        cursor = sqliteConnection.cursor()
        sql_update_query = f"Update app_task set {param} = {value} where {filterparam} = {valueforsearch}"
        cursor.execute(sql_update_query)
        sqliteConnection.commit()
        cursor.close()
        return {'True':'True'}
    else:
        return {'False':'False'}