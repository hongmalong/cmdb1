# Generated by Django 2.0.3 on 2019-01-11 09:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cmdb1_demo1_app1', '0032_auto_20190111_0930'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cabinettable',
            name='ctime',
            field=models.CharField(default='20190111093230', max_length=49, null=True),
        ),
        migrations.AlterField(
            model_name='companytable',
            name='ctime',
            field=models.CharField(default='20190111093230', max_length=49, null=True),
        ),
        migrations.AlterField(
            model_name='deploylogtable',
            name='ctime',
            field=models.CharField(default='20190111093230', max_length=49, null=True),
        ),
        migrations.AlterField(
            model_name='enviromenttable',
            name='ctime',
            field=models.CharField(default='20190111093230', max_length=49, null=True),
        ),
        migrations.AlterField(
            model_name='equipmenttable',
            name='ctime',
            field=models.CharField(default='20190111093230', max_length=49, null=True),
        ),
        migrations.AlterField(
            model_name='equipmenttypetable',
            name='ctime',
            field=models.CharField(default='20190111093230', max_length=49, null=True),
        ),
        migrations.AlterField(
            model_name='eventtable',
            name='eventId',
            field=models.CharField(max_length=255, unique=True),
        ),
        migrations.AlterField(
            model_name='historytable',
            name='ctime',
            field=models.CharField(default='20190111093230', max_length=49, null=True),
        ),
        migrations.AlterField(
            model_name='logpathtable',
            name='ctime',
            field=models.CharField(default='20190111093230', max_length=49, null=True),
        ),
        migrations.AlterField(
            model_name='nodetable',
            name='ctime',
            field=models.CharField(default='20190111093230', max_length=49, null=True),
        ),
        migrations.AlterField(
            model_name='occupationtable',
            name='ctime',
            field=models.CharField(default='20190111093230', max_length=49, null=True),
        ),
        migrations.AlterField(
            model_name='porttable',
            name='ctime',
            field=models.CharField(default='20190111093230', max_length=49, null=True),
        ),
        migrations.AlterField(
            model_name='privatetable',
            name='ctime',
            field=models.CharField(default='20190111093230', max_length=49, null=True),
        ),
        migrations.AlterField(
            model_name='projecttable',
            name='ctime',
            field=models.CharField(default='20190111093230', max_length=49, null=True),
        ),
        migrations.AlterField(
            model_name='providertable',
            name='ctime',
            field=models.CharField(default='20190111093230', max_length=49, null=True),
        ),
        migrations.AlterField(
            model_name='serverroomtable',
            name='ctime',
            field=models.CharField(default='20190111093230', max_length=49, null=True),
        ),
        migrations.AlterField(
            model_name='servicetable',
            name='ctime',
            field=models.CharField(default='20190111093230', max_length=49, null=True),
        ),
        migrations.AlterField(
            model_name='servicetypetable',
            name='ctime',
            field=models.CharField(default='20190111093230', max_length=49, null=True),
        ),
        migrations.AlterField(
            model_name='servicetypetable',
            name='portNumber',
            field=models.CharField(default='20190111093230', max_length=49, null=True),
        ),
    ]
