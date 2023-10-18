from django.contrib import admin

from .models import Pregunta, ElegirRespuesta

class ElegirRespuestaInLine(admin.TabularInline):
    model = ElegirRespuesta
    max_num = ElegirRespuesta.maximo_respuestas
    min_num = ElegirRespuesta.maximo_respuestas
    can_delete = False

class PreguntaAdmin(admin.ModelAdmin):
    model = Pregunta
    inlines = (ElegirRespuestaInLine, )
    list_display = ['texto', ]
    search_fields = ['texto', "preguntas__texto"]

admin.site.register(ElegirRespuesta)
admin.site.register(Pregunta, PreguntaAdmin)