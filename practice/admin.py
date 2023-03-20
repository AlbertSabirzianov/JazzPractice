from django.contrib import admin
from .models import ChordChoice, Chord


class ChordChoiceAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'get_right_desigion', 'is_right')


admin.site.register(ChordChoice, ChordChoiceAdmin)
admin.site.register(Chord)
