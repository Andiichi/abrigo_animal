# Generated by Django 4.2.16 on 2024-10-17 23:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('site_abrigo', '0012_galeriaimagem'),
    ]

    operations = [
        migrations.AlterField(
            model_name='galeriaimagem',
            name='animal',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='galeria', to='site_abrigo.cadastroanimal'),
        ),
    ]
