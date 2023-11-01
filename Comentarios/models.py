from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.fields import GenericRelation
from django.conf import settings
from django.urls import reverse

# Create your models here.
class ComentariosManager(models.Manager):
    def filtro_por_instancia(self, instance):
        content_type = ContentType.objects.get_for_model(instance.__class__)
        obj_id = instance.id
        qs = super(ComentariosManager, self).filter(content_type=content_type, object_id=obj_id).filter(padre=None)
        return qs

class Comentarios(models.Model):
    usuario = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, default=1)
    texto = models.TextField(verbose_name='Comentario')

    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_objects = GenericForeignKey('content_type', 'object_id')
    
    padre = models.ForeignKey('self', null= True, blank=True, on_delete=models.CASCADE)
    
    tiempo = models.DateTimeField(auto_now_add=True)

    objects = ComentariosManager()

    class Meta:
        ordering = ['-tiempo']

    def __str__(self):
        return self.texto[:15]

    def get_absolute_url(self):
        return reverse('comentario_id', kwargs={'pk': self.pk})

    def Hijo(self):
        return Comentarios.objects.filter(padre=self)

    
