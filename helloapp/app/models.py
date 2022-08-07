from django.db import models

class Task(models.Model):
    pacient = models.ForeignKey(
        'Pacient',
        on_delete=models.SET_NULL,
        null=True,
    )
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    doctor = models.ForeignKey(
        'Doctors',
        on_delete=models.SET_NULL,
        null=True,
    )
    time = models.DateTimeField(null=True)
    status = models.BooleanField(default=False)



class Doctors(models.Model):
    name = models.CharField(max_length=200)
    birthday = models.DateField()
    phone = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    depart = models.CharField(max_length=200)
    cab = models.CharField(max_length=200)
    startwork = models.DateTimeField()
    endwork = models.DateTimeField()
    vacation = models.DateField()



class Pacient(models.Model):
    name = models.CharField(max_length=200)
    birthday = models.DateField()
    phone = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    depart = models.CharField(max_length=200)
    chamber = models.CharField(max_length=200)
    starttreament = models.DateTimeField()
    endtreament = models.DateTimeField()
    checkout = models.CharField(max_length=200)

