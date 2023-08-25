# Generated by Django 4.2.3 on 2023-08-23 11:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainform', '0004_alter_services_options_alter_studentdata_options_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='langservices',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('langser', models.CharField(max_length=300)),
            ],
            options={
                'verbose_name': 'services',
                'verbose_name_plural': 'Checkbox Lang services',
            },
        ),
        migrations.RenameModel(
            old_name='services',
            new_name='itservices',
        ),
        migrations.AlterModelOptions(
            name='itservices',
            options={'verbose_name': 'itservices', 'verbose_name_plural': 'Checkbox IT services'},
        ),
    ]