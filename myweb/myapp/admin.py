from django.contrib import admin

# Register your models here.
from myapp.models import student

class StudentAdmin(admin.ModelAdmin):
    list_display=('id','cName','cSex','cBirthday','cEmail','cPhone',)
    list_filter=('cSex',)
    search_fields=('cName','cEmail','cPhone',)
    ordering=('id','cName',)

admin.site.register(student, StudentAdmin)