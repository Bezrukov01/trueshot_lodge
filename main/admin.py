from django.contrib import admin
from .models import Character, Specialization


class CharactersAdmin(admin.ModelAdmin):
    list_display = ('name', 'icon', 'description',)


class SpecializationsAdmin(admin.ModelAdmin):
    list_display = ('name', 'character', 'icon', 'description', 'acronyms', 'stats_gems_enchants', 'talents',
                    'rotation_priority', 'legendaries', 'gear', 'trinkets', 'weak_auras', )

admin.site.register(Character, CharactersAdmin)
admin.site.register(Specialization, SpecializationsAdmin)
