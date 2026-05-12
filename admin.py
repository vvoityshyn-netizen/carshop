from django.contrib import admin
from .models import Request, Purchase # type: ignore

admin.site.register(Request)
admin.site.register(Purchase)