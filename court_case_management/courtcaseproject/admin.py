from django.contrib import admin

from .models import Admin, ClientForm

# Register your models here.

admin.site.register(ClientForm)
admin.site.register(Admin)
