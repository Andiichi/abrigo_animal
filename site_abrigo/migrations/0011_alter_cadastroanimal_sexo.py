# Generated by Django 4.2.16 on 2024-10-17 17:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('site_abrigo', '0010_alter_cadastroanimal_especie_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cadastroanimal',
            name='sexo',
            field=models.CharField(choices=[('femea', 'Fêmea'), ('macho', 'Macho')], max_length=5),
        ),
    ]
