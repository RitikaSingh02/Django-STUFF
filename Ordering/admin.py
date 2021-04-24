from django.contrib import admin
from . models import *


# registering the custom models to the admin panel
admin.site.register(Pizza)
admin.site.register(Size)


# Register your models here.
