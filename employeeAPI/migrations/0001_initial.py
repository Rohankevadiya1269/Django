# Generated by Django 5.0.2 on 2024-02-12 10:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserDetail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('emailId', models.EmailField(max_length=250)),
                ('age', models.IntegerField(max_length=3)),
            ],
        ),
    ]
