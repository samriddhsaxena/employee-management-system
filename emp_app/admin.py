from django.contrib import admin
from .models import Employees,Role,Department

admin.site.register(Employees)
admin.site.register(Role)
admin.site.register(Department)