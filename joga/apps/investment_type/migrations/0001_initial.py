# Generated by Django 3.1.6 on 2021-05-12 19:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='InvestmentType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('short_name', models.CharField(max_length=200)),
                ('full_name', models.CharField(blank=True, max_length=200, null=True)),
                ('description', models.CharField(blank=True, max_length=2000, null=True)),
            ],
            options={
                'verbose_name': 'Investment type',
                'verbose_name_plural': 'Investments type',
            },
        ),
    ]
