# Generated by Django 4.2.13 on 2024-05-15 20:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categore',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timeit', models.CharField(max_length=60, verbose_name='title')),
                ('avatar', models.ImageField(blank=True, upload_to='Categore/', verbose_name='avatar')),
                ('is_enble', models.BooleanField(default=True, verbose_name='is_enble')),
                ('creat_time', models.DateTimeField(auto_now_add=True, verbose_name='creat_time')),
                ('updat_time', models.DateTimeField(auto_now=True, verbose_name='uplod_time')),
                ('parinrt', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='prodact.categore', verbose_name='parint')),
            ],
        ),
        migrations.CreateModel(
            name='Prodact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timeit', models.CharField(max_length=60, verbose_name='title')),
                ('avatar', models.ImageField(blank=True, upload_to='prodqct/', verbose_name='avatar')),
                ('is_enble', models.BooleanField(default=True, verbose_name='is_enble')),
                ('creat_time', models.DateTimeField(auto_now_add=True, verbose_name='creat_time')),
                ('updat_time', models.DateTimeField(auto_now=True, verbose_name='uplod_time')),
                ('categoris', models.ManyToManyField(blank=True, to='prodact.categore', verbose_name=' Categore')),
            ],
        ),
        migrations.CreateModel(
            name='Fali',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(upload_to='file/%Y/%m/%d/', verbose_name='file')),
                ('timeit', models.CharField(max_length=60, verbose_name='title')),
                ('is_enble', models.BooleanField(default=True, verbose_name='is_enble')),
                ('creat_time', models.DateTimeField(auto_now_add=True, verbose_name='creat_time')),
                ('updat_time', models.DateTimeField(auto_now=True, verbose_name='uplod_time')),
                ('parinrt', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='prodact.prodact', verbose_name='parint')),
            ],
        ),
    ]
