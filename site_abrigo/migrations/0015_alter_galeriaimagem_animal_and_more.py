# Generated by Django 4.2.16 on 2024-10-18 00:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('site_abrigo', '0014_alter_galeriaimagem_animal'),
    ]

    operations = [
        migrations.AlterField(
            model_name='galeriaimagem',
            name='animal',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='galeria', to='site_abrigo.cadastroanimal'),
        ),
        migrations.AlterField(
            model_name='galeriaimagem',
            name='titulo',
            field=models.CharField(blank=True, max_length=80, null=True),
        ),
    ]