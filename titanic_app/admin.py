# titanic_app/admin.py
from django.contrib import admin
from .models import Titanic

class TitanicDataAdmin(admin.ModelAdmin):
    list_display = ('passenger_id', 'name', 'age', 'sex', 'survived', 'pclass', 'sibsp', 'parch', 'ticket', 'fare', 'cabin', 'embarked')
    list_filter = ('survived', 'pclass', 'sex')
    search_fields = ('name', 'ticket')
    ordering = ('passenger_id',)

admin.site.register(Titanic, TitanicDataAdmin)
