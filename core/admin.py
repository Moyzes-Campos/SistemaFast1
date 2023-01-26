from django.contrib import admin

from .models import Regulamento, Event, AtividadeIndex, ObjetivosArea, Integrantes

# Register your models here.


@admin.register(Regulamento)
class RegulamentoAdmin(admin.ModelAdmin):
    list_display = ('t1', 't3', 'resumo',)


@admin.register(Event)
class CalendarioFastAdmin(admin.ModelAdmin):
    list_display = ('day', 'start_time','notes')


@admin.register(AtividadeIndex)
class AtividadeIndexAdmin(admin.ModelAdmin):
    list_display = ('area', 'situacao', 'descricao',)


@admin.register(ObjetivosArea)
class ObjetivosAreaAdmin(admin.ModelAdmin):
    list_display = ('area', 'titulo', 'descricao',)


@admin.register(Integrantes)
class Integrantes(admin.ModelAdmin):
    list_display = ('nome', 'funcao', 'area', 'foto',)
