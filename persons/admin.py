from django.contrib import admin
from .models import StudentMap, PersonalMap, Feetback


class PersonalMapAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'stady_level', 'stady_course')
    list_filter = ('stady_level', 'stady_course')


class StudentMapAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'reiting', 'activiti')


admin.site.register(StudentMap, StudentMapAdmin)
admin.site.register(PersonalMap, PersonalMapAdmin)
admin.site.register(Feetback)
