# Generated by Django 4.2.3 on 2023-08-23 11:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mainform', '0003_services_alter_studentdata_dob'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='services',
            options={'verbose_name': 'services', 'verbose_name_plural': 'Checkbox services'},
        ),
        migrations.AlterModelOptions(
            name='studentdata',
            options={'verbose_name': 'studentdata', 'verbose_name_plural': 'Student Details'},
        ),
        migrations.RemoveField(
            model_name='services',
            name='langser',
        ),
    ]