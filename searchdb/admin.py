from django.contrib import admin
from .models import Student,Student2
from import_export.admin import ImportExportModelAdmin
# Register your models here.
# admin.site.register(Student)
# admin.site.register(Student2)

@admin.register(Student)
class StudentImportExport(ImportExportModelAdmin):
    pass

@admin.register(Student2)
class Studen2tImportExport(ImportExportModelAdmin):
    pass

