# models.py
from django.db import models

# titanic_app/models.py

# from django.db import models

class Titanic(models.Model):
    passenger_id = models.IntegerField(unique=True,primary_key=True)  # نام فیلدها با حروف کوچک
    survived = models.BooleanField()  # به صورت BooleanField تعریف شود
    pclass = models.IntegerField()
    name = models.CharField(max_length=255)
    sex = models.CharField(max_length=10)
    age = models.FloatField(null=True)
    sibsp = models.IntegerField()
    parch = models.IntegerField()
    ticket = models.CharField(max_length=50)
    fare = models.FloatField()
    cabin = models.CharField(max_length=50, null=True)
    embarked = models.CharField(max_length=100)


    def __str__(self):
        return self.name
