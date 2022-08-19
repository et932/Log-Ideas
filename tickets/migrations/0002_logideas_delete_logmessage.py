# Generated by Django 4.0.5 on 2022-08-09 15:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tickets', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='LogIdeas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10)),
                ('description', models.CharField(max_length=60)),
                ('log_date', models.DateTimeField(verbose_name='date logged')),
            ],
        ),
        migrations.DeleteModel(
            name='LogMessage',
        ),
    ]
