# Generated by Django 4.2.16 on 2024-10-17 13:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('site_abrigo', '0008_alter_cadastroanimal_especie_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cadastroanimal',
            name='especie',
            field=models.CharField(max_length=8),
        ),
        migrations.AlterField(
            model_name='cadastroanimal',
            name='sexo',
            field=models.CharField(max_length=80),
        ),
    ]