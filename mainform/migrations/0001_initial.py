# Generated by Django 4.2.3 on 2023-08-23 10:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='studentdata',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fullname', models.CharField(max_length=100)),
                ('adds', models.TextField()),
                ('city', models.CharField(max_length=100)),
                ('state', models.CharField(max_length=100)),
                ('zip', models.CharField(max_length=100)),
                ('mob', models.CharField(max_length=100)),
                ('mail', models.CharField(max_length=250)),
                ('dob', models.CharField(max_length=100)),
                ('perimg', models.CharField(max_length=100)),
                ('education', models.CharField(max_length=100)),
                ('field', models.CharField(max_length=250)),
                ('university', models.CharField(max_length=250)),
                ('passyr', models.CharField(max_length=100)),
                ('oneradio', models.CharField(max_length=100)),
                ('applicationdate', models.CharField(max_length=100)),
                ('secradio', models.CharField(max_length=100)),
                ('itservice', models.CharField(max_length=250)),
                ('langservice', models.CharField(max_length=250)),
                ('thirdradio', models.CharField(max_length=100)),
                ('feedata', models.CharField(max_length=100)),
            ],
        ),
    ]