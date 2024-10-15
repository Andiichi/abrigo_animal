# Generated by Django 4.2.16 on 2024-10-15 17:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('site_abrigo', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CadastroAnimal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=80)),
                ('idade', models.IntegerField()),
                ('sexo', models.CharField(choices=[('F', 'Fêmea'), ('M', 'Masculino')], max_length=1)),
                ('raca', models.CharField(blank=True, default='Viralata', max_length=80, null=True)),
                ('especie', models.CharField(choices=[('1', 'Cachorro'), ('2', 'Gato'), ('3', 'Outros')], max_length=1)),
                ('image_field', models.ImageField(upload_to='images/{nome}')),
            ],
        ),
        migrations.DeleteModel(
            name='Uploads',
        ),
    ]
