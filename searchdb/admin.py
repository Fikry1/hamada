from django.contrib import admin
from .models import Student,Student2
from import_export.admin import ImportExportModelAdmin
# Register your models here.
# admin.site.register(Student)
# admin.site.register(Student2)


 


@admin.register(Student)
class StudentImportExport(ImportExportModelAdmin):
   list_display = ('seatNumber', 'name', 'arabic','math','english','social','sience','islamic','olenglish','computer','art')
   list_display_links =('seatNumber','name')
   search_fields = ('seatNumber','name')

@admin.register(Student2)
class Studen2tImportExport(ImportExportModelAdmin):
   list_display = ('seatNumber', 'name', 'arabic','math','english','social','sience','islamic','olenglish','computer','art')
   list_display_links =('seatNumber','name')
   search_fields = ('seatNumber','name')


admin.site.site_header ="Fikry Control panel"
admin.site.site_title = "Fikry Control panel"


