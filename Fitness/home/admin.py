from dataclasses import fields
from home.views import contact
from django.contrib import admin
from home.models import Contact
# Register your models here.

# admin.site.register(Contact)

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ['name','phone','email','desc','date']