# Generated by Django 5.0.1 on 2024-01-24 19:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PontoTuristico',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120)),
                ('description', models.TextField()),
                ('aproved', models.BooleanField(default=False)),
                ('comments', models.TextField()),
                ('address', models.CharField(max_length=150)),
                ('photo', models.ImageField(blank=True, null=True, upload_to='pontos_turisticos')),
                ('valuation', models.DecimalField(decimal_places=2, max_digits=2)),
                ('cad_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
