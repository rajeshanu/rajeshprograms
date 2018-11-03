from django.contrib import admin

from .models import course
from .models import faculity
from .models import newclass

admin.site.register(course)
admin.site.register(faculity)
admin.site.register(newclass)
