# Generated by Django 2.0.3 on 2018-03-21 23:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cmdb1_demo1_app1', '0013_auto_20180321_0406'),
    ]

    operations = [
        migrations.CreateModel(
            name='EnviromentTable',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, null=True)),
                ('ctime', models.CharField(default='20180321233604', max_length=49, null=True)),
            ],
        ),
        migrations.RenameField(
            model_name='nodetable',
            old_name='name',
            new_name='ip',
        ),
        migrations.RemoveField(
            model_name='porttable',
            name='company',
        ),
        migrations.AlterField(
            model_name='cabinettable',
            name='ctime',
            field=models.CharField(default='20180321233604', max_length=49, null=True),
        ),
        migrations.AlterField(
            model_name='companytable',
            name='ctime',
            field=models.CharField(default='20180321233604', max_length=49, null=True),
        ),
        migrations.AlterField(
            model_name='equipmenttable',
            name='ctime',
            field=models.CharField(default='20180321233604', max_length=49, null=True),
        ),
        migrations.AlterField(
            model_name='equipmenttypetable',
            name='ctime',
            field=models.CharField(default='20180321233604', max_length=49, null=True),
        ),
        migrations.AlterField(
            model_name='historytable',
            name='ctime',
            field=models.CharField(default='20180321233604', max_length=49, null=True),
        ),
        migrations.AlterField(
            model_name='logpathtable',
            name='ctime',
            field=models.CharField(default='20180321233604', max_length=49, null=True),
        ),
        migrations.AlterField(
            model_name='nodetable',
            name='ctime',
            field=models.CharField(default='20180321233604', max_length=49, null=True),
        ),
        migrations.AlterField(
            model_name='occupationtable',
            name='ctime',
            field=models.CharField(default='20180321233604', max_length=49, null=True),
        ),
        migrations.AlterField(
            model_name='porttable',
            name='ctime',
            field=models.CharField(default='20180321233604', max_length=49, null=True),
        ),
        migrations.AlterField(
            model_name='privatetable',
            name='ctime',
            field=models.CharField(default='20180321233604', max_length=49, null=True),
        ),
        migrations.AlterField(
            model_name='projecttable',
            name='ctime',
            field=models.CharField(default='20180321233604', max_length=49, null=True),
        ),
        migrations.AlterField(
            model_name='providertable',
            name='ctime',
            field=models.CharField(default='20180321233604', max_length=49, null=True),
        ),
        migrations.AlterField(
            model_name='serverroomtable',
            name='ctime',
            field=models.CharField(default='20180321233604', max_length=49, null=True),
        ),
        migrations.AlterField(
            model_name='servicetable',
            name='ctime',
            field=models.CharField(default='20180321233604', max_length=49, null=True),
        ),
        migrations.AlterField(
            model_name='servicetypetable',
            name='ctime',
            field=models.CharField(default='20180321233604', max_length=49, null=True),
        ),
        migrations.AddField(
            model_name='enviromenttable',
            name='company',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='cmdb1_demo1_app1.CompanyTable'),
        ),
    ]
