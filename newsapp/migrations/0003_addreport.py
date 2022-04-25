# Generated by Django 4.0 on 2022-03-16 07:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newsapp', '0002_rplogin'),
    ]

    operations = [
        migrations.CreateModel(
            name='AddReport',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.FileField(upload_to='images/users')),
                ('Date', models.DateField(max_length=100)),
                ('Title', models.CharField(max_length=100)),
                ('Description', models.CharField(max_length=10000)),
            ],
            options={
                'db_table': 'addreport',
            },
        ),
    ]
