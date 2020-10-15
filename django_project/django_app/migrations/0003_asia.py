# Generated by Django 3.1.2 on 2020-10-15 12:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('django_app', '0002_delete_asia'),
    ]

    operations = [
        migrations.CreateModel(
            name='Asia',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city', models.CharField(max_length=30)),
                ('country', models.CharField(max_length=30)),
                ('population', models.IntegerField()),
            ],
        ),
    ]