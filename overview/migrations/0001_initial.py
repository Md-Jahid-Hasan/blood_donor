# Generated by Django 2.2.7 on 2020-07-17 17:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MonthlyTotalDonate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('month', models.CharField(max_length=20)),
                ('year', models.IntegerField()),
                ('total_donate', models.IntegerField()),
                ('total_op_donate', models.IntegerField()),
                ('total_on_donate', models.IntegerField()),
                ('total_ap_donate', models.IntegerField()),
                ('total_an_donate', models.IntegerField()),
                ('total_bp_donate', models.IntegerField()),
                ('total_bn_donate', models.IntegerField()),
                ('total_abp_donate', models.IntegerField()),
                ('total_abn_donate', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='MonthlyTotalJoin',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('month', models.CharField(max_length=20)),
                ('year', models.IntegerField()),
                ('total_user', models.IntegerField()),
                ('total_op', models.IntegerField()),
                ('total_on', models.IntegerField()),
                ('total_ap', models.IntegerField()),
                ('total_an', models.IntegerField()),
                ('total_bp', models.IntegerField()),
                ('total_bn', models.IntegerField()),
                ('total_abp', models.IntegerField()),
                ('total_abn', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Total',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total_user', models.IntegerField(default=0)),
                ('total_op', models.IntegerField(default=0)),
                ('total_on', models.IntegerField(default=0)),
                ('total_ap', models.IntegerField(default=0)),
                ('total_an', models.IntegerField(default=0)),
                ('total_bp', models.IntegerField(default=0)),
                ('total_bn', models.IntegerField(default=0)),
                ('total_abp', models.IntegerField(default=0)),
                ('total_abn', models.IntegerField(default=0)),
            ],
        ),
    ]
