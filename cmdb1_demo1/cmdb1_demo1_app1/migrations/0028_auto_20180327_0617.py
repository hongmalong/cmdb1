# Generated by Django 2.0.3 on 2018-03-27 06:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cmdb1_demo1_app1', '0027_auto_20180326_0054'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cabinettable',
            name='ctime',
            field=models.CharField(default='20180327061730', max_length=49, null=True),
        ),
        migrations.AlterField(
            model_name='companytable',
            name='ctime',
            field=models.CharField(default='20180327061730', max_length=49, null=True),
        ),
        migrations.AlterField(
            model_name='enviromenttable',
            name='ctime',
            field=models.CharField(default='20180327061730', max_length=49, null=True),
        ),
        migrations.AlterField(
            model_name='equipmenttable',
            name='ctime',
            field=models.CharField(default='20180327061730', max_length=49, null=True),
        ),
        migrations.AlterField(
            model_name='equipmenttypetable',
            name='ctime',
            field=models.CharField(default='20180327061730', max_length=49, null=True),
        ),
        migrations.AlterField(
            model_name='historytable',
            name='ctime',
            field=models.CharField(default='20180327061730', max_length=49, null=True),
        ),
        migrations.AlterField(
            model_name='logpathtable',
            name='ctime',
            field=models.CharField(default='20180327061730', max_length=49, null=True),
        ),
        migrations.AlterField(
            model_name='logpathtable',
            name='node',
            field=models.CharField(max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='nodetable',
            name='ctime',
            field=models.CharField(default='20180327061730', max_length=49, null=True),
        ),
        migrations.AlterField(
            model_name='occupationtable',
            name='ctime',
            field=models.CharField(default='20180327061730', max_length=49, null=True),
        ),
        migrations.AlterField(
            model_name='porttable',
            name='ctime',
            field=models.CharField(default='20180327061730', max_length=49, null=True),
        ),
        migrations.AlterField(
            model_name='privatetable',
            name='ctime',
            field=models.CharField(default='20180327061730', max_length=49, null=True),
        ),
        migrations.AlterField(
            model_name='projecttable',
            name='ctime',
            field=models.CharField(default='20180327061730', max_length=49, null=True),
        ),
        migrations.AlterField(
            model_name='providertable',
            name='ctime',
            field=models.CharField(default='20180327061730', max_length=49, null=True),
        ),
        migrations.AlterField(
            model_name='serverroomtable',
            name='ctime',
            field=models.CharField(default='20180327061730', max_length=49, null=True),
        ),
        migrations.AlterField(
            model_name='servicetable',
            name='ctime',
            field=models.CharField(default='20180327061730', max_length=49, null=True),
        ),
        migrations.AlterField(
            model_name='servicetypetable',
            name='ctime',
            field=models.CharField(default='20180327061730', max_length=49, null=True),
        ),
        migrations.AlterField(
            model_name='servicetypetable',
            name='portNumber',
            field=models.CharField(default='20180327061730', max_length=49, null=True),
        ),
    ]
