# Generated by Django 2.0.3 on 2018-08-25 02:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cmdb1_demo1_app1', '0015_auto_20180825_0232'),
    ]

    operations = [
        migrations.AlterField(
            model_name='companytable',
            name='ctime',
            field=models.CharField(default='20180825023301', max_length=49, null=True),
        ),
    ]