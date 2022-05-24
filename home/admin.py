from django.contrib import admin

# Register your models here.
from .models import excel,beforefetch,status,statusdetails


class excelAdmin(admin.ModelAdmin):

    list_display = ['name','email']
admin.site.register(excel,excelAdmin)


class beforefetchAdmin(admin.ModelAdmin):

    list_display = ['uniquename','excel_file_upload','template_file_upload']
admin.site.register(beforefetch,beforefetchAdmin)

class statusAdmin(admin.ModelAdmin):

    list_display = ['statusname']
admin.site.register(status,statusAdmin)

class statusdetailsAdmin(admin.ModelAdmin):

    list_display = ['email','send']
admin.site.register(statusdetails,statusdetailsAdmin)