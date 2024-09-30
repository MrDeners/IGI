# Generated by Django 4.2.13 on 2024-09-14 12:00

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_partner_url'),
    ]

    operations = [
        migrations.CreateModel(
            name='History',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Name')),
                ('description', models.TextField(verbose_name='Description')),
                ('created', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Creation data')),
            ],
            options={
                'verbose_name': 'History',
                'verbose_name_plural': 'Histories',
            },
        ),
        migrations.CreateModel(
            name='Prop',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Name')),
                ('description', models.TextField(verbose_name='Description')),
            ],
            options={
                'verbose_name': 'Prop',
                'verbose_name_plural': 'Props',
            },
        ),
        migrations.AddField(
            model_name='about',
            name='certificate',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='about',
            name='logoUrl',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='about',
            name='videoReviewUrl',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='about',
            name='history',
            field=models.ManyToManyField(blank=True, null=True, related_name='abouts', to='main.history'),
        ),
        migrations.AddField(
            model_name='about',
            name='props',
            field=models.ManyToManyField(blank=True, null=True, related_name='abouts', to='main.prop'),
        ),
    ]
