# Generated by Django 2.2.3 on 2019-08-15 11:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crowdfunding', '0002_auto_20190815_2012'),
    ]

    operations = [
        migrations.AlterField(
            model_name='crfproject',
            name='pImage',
            field=models.ImageField(default='cf/default', upload_to='cf/%Y%M%d', verbose_name='이미지'),
        ),
    ]
