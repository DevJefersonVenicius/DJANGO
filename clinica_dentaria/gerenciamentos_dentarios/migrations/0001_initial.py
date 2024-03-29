# Generated by Django 4.2.9 on 2024-02-07 12:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='GerenciamentoDentario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=150)),
                ('data_nascimento', models.DateField()),
                ('cpf', models.CharField(max_length=14)),
                ('data_tempo_cadastro', models.DateTimeField(auto_now_add=True)),
                ('idade', models.IntegerField(default=0)),
                ('dia_consulta', models.CharField(choices=[('SEG', 'Segunda'), ('TER', 'Terça'), ('QUA', 'Quarta'), ('QUI', 'Quinta'), ('SEX', 'Sexta')], default='SEG', max_length=3)),
                ('horario', models.CharField(choices=[('H1', '8:00h ás 11:00h'), ('H2', '13:00h ás 17:00h'), ('H3', '19:00 ás 22:00')], default='H1', max_length=2)),
                ('descricao', models.TextField()),
                ('email', models.EmailField(max_length=254)),
                ('numero', models.CharField(max_length=20)),
                ('imagem', models.ImageField(upload_to='imagens')),
            ],
        ),
    ]
