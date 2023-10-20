from django.contrib import admin

from .models import Pregunta, ElegirRespuesta, PreguntasRespondidas

from .forms import ElegirInlineFormset

class ElegirRespuestaInLine(admin.TabularInline):
    model = ElegirRespuesta
    max_num = ElegirRespuesta.maximo_respuestas
    min_num = ElegirRespuesta.maximo_respuestas
    can_delete = False
    formset = ElegirInlineFormset

class PreguntaAdmin(admin.ModelAdmin):
    model = Pregunta
    inlines = (ElegirRespuestaInLine, )
    list_display = ['texto', ]
    search_fields = ['texto', "preguntas__texto"]

class PreguntasRespondidasAdmin(admin.ModelAdmin):
    list_display=['pregunta', 'respuesta', 'correcta', 'puntaje_obtenido']
    
    class Meta:
        model = PreguntasRespondidas

admin.site.register(PreguntasRespondidas)
admin.site.register(ElegirRespuesta)
admin.site.register(Pregunta, PreguntaAdmin)