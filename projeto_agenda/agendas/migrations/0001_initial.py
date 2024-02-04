# Generated by Django 4.2.9 on 2024-01-31 14:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Agenda',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('disciplina', models.CharField(max_length=100)),
                ('assunto', models.TextField()),
                ('tempo_estudado', models.IntegerField(default=0)),
                ('dia_semana', models.CharField(choices=[('DOM', 'Domingo'), ('SEG', 'Segunda'), ('TER', 'Terça'), ('QUA', 'Quarta'), ('QUI', 'Quinta'), ('SEX', 'Sexta'), ('SAB', 'Sabado')], default='DOM', max_length=3)),
                ('foto', models.ImageField(upload_to='assuntos')),
            ],
        ),
    ]