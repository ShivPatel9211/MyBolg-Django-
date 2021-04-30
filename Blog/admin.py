from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register((Profile ,Message,Post ,Comment))
# admin.site.register(Message)