# Generated by Django 2.2.3 on 2019-07-30 16:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='cfuser',
            fields=[
                ('email', models.CharField(max_length=30, primary_key=True, serialize=False)),
                ('uname', models.CharField(max_length=10)),
                ('pswd', models.CharField(max_length=10)),
            ],
            options={
                'db_table': 'cfuser',
                'managed': False,
            },
        ),
    ]
