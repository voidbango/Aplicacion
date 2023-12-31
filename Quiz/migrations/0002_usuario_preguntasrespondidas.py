# Generated by Django 4.2.6 on 2023-10-20 19:06

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Quiz', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('puntaje_total', models.DecimalField(decimal_places=2, default=0, max_digits=10, verbose_name='Puntaje Total')),
                ('usuario', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='PreguntasRespondidas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('correcta', models.BooleanField(default=False, verbose_name='¿Es esta la respuesta correcta?')),
                ('puntaje_obtenido', models.DecimalField(decimal_places=2, default=0, max_digits=6, verbose_name='Puntaje Obtenido')),
                ('pregunta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Quiz.pregunta')),
                ('respuesta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='intentos', to='Quiz.elegirrespuesta')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Quiz.usuario')),
            ],
        ),
    ]
