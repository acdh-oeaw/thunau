from django.contrib import admin
from .models import Institution, Person, Document

admin.site.register(Institution)
admin.site.register(Person)
admin.site.register(Document)

# Register your models here.
